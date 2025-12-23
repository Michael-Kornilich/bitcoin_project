import psycopg
from tabulate import tabulate
from pydantic import validate_call, ConfigDict
import numpy as np

validate_call_config = ConfigDict(arbitrary_types_allowed=True)

# prepare for insert function
@validate_call(config=validate_call_config)
def _prepare_for_insert(
    data:np.ndarray,
    string_array:bool = False
) -> str:
    """
    Prepares given for a bulk insert.
    WARNING: Not secure against SQL injections

    Params:
        - data: the data to be inserted

    Returns:
        - string of the form: '(a, b, c,...), (d, e, f, g,...)'
    """
    assert len(data.shape) == 2, f"Data must be 2-dimensional. Given: {data.shape} ({len(data.shape)}-dimensional)"
    
    if string_array:
        data_:np.ndarray = ("'" + data + "'").copy()
    else:
        data_:np.ndarray = data.copy()

    insert_values = ", ".join( # set separator between rows
        map(
            lambda x: "(" + ", ".join(x) + ")", # Wrap each row in parens
            data_.astype(str) # cast each value to string
        )
    )
    return insert_values

@validate_call(config=validate_call_config)
def insert_into_db(
    conn_str: str,
    table: str,
    data: np.ndarray,
    string_array: bool = False
) -> None:
    """
    Inserts given 2D data into the `table` in the bitcoin database.

    ASSUMPTION: PostgeSQL database
    WARNING: Homogenous arrays are not supported - will resolve in unexpected behavior

    Params:
        - conn_string: connection sting to the database
        - table: name of the table in the database
        - data: 2D array of data to be inserted. With columns = table columns and rows = rows to be inserted
        - string_array=False: set to True if the data is string-like. If set improperly will result in corruption of data in the database table and / or an error

    Raises:
        - AssertionError: if input(s) are invalid
        - Whatever psycopg.Connection.execute can raise
    """
    assert len(data.shape) == 2, (
        f"Data must be 2-dimensional. Given: {data.shape} ({len(data.shape)}-dimensional)"
    )

    insert_values = _prepare_for_insert(data=data, string_array=string_array)

    with psycopg.connect(conn_str) as conn:
        # whatever errors might result in this operation will be propagated
        conn.execute(f"INSERT INTO {table} VALUES {insert_values}")
    return


# dry insert function
@validate_call(config=validate_call_config)
def dry_insert_into_db(
    conn_str:str, 
    table:str, 
    data:np.ndarray
) -> None:
    """
    Mocks insert (dry-run) of the given 2D data into the `table` in the database.

    ASSUMPTION: PostgeSQL database
    WARNING: Homogenous arrays are not supported - will resolve in unexpected behavior
    
    Params:
        - conn_string: connection sting to the database
        - table: name of the table in the database
        - data: 2D array of data to be inserted. With columns = table columns and rows = rows to be inserted
        - string_array=False: set to True if the data is string-like. If set improperly will result in corruption of data in the database table and / or an error
    
    Raises:
        - AssertionError: if input(s) are invalid
        - ValueError: if there is a shape mismatch between data-array and number of columns in the target table
        - ValueError: if table does not exist
    """
    assert len(data.shape) == 2, f"Data must be 2-dimensional. Given: {data.shape} ({len(data.shape)}-dimensional)"
    
    with psycopg.connect(conn_str) as conn:
            res = conn.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table}';")
    cols = np.array(res.fetchall()).flatten()
    
    if len(cols) == 0:
        raise ValueError(f"The table '{table}' does not exist")
    elif len(cols) != data.shape[1]:
        raise ValueError(f"Number of columns ({len(cols)}) does not match the number of columns in data ({data.shape[1]})")
    
    string = np.concat(
        [data.astype(str)[:3], np.full((1,len(cols)),"...")],
        axis=0
    )
    print(
        f"Insert values into {table}:\n"
        f"{tabulate(string, headers=cols, tablefmt="pipe")}\n\n"
        f"Insertion shape is valid."
    )
    return 

@validate_call(config=validate_call_config)
def describe_table(
    conn_str:str, 
    table:str, 
    order_column:str
) -> str:
    """
    Returns a table desciption:
        - Table name
        - Columns, data types, is nullable
        - Number of entires
        - First and last enties
    """
    with psycopg.connect(conn_str) as conn:
        res = conn.execute(f"""
            SELECT 
               column_name, 
               data_type,
               is_nullable
            FROM
               information_schema.columns
            WHERE
               table_name = '{table}';
        """)
        arr = np.array(res.fetchall())
        cols = arr[...,0]
        
        table_info = tabulate(
            arr, 
            headers=["column_name", "data_type", "is_nullable"],
            tablefmt="pipe"
        )
    
        res = conn.execute(f'SELECT COUNT(*) FROM "{table}"')
        enties_count = np.array(res.fetchall()).flatten()[0]
    
        res = conn.execute(f"""
            (SELECT 
                *
            FROM "{table}"
            ORDER BY "{order_column}" ASC
            LIMIT 1)
        
            UNION ALL
        
            (SELECT 
                *
            FROM "{table}"
            ORDER BY "{order_column}" DESC
            LIMIT 1)
        """)
        first_last = tabulate(
            np.array(res.fetchall()),
            headers=cols,
            tablefmt="pipe"
        )
    
        return (
            f"Table summary: {table}\n\n"
            f"{table_info}\n\n"
            f"With {enties_count} entiries\n\n"
            f"First & last being:\n"
            f"{first_last}"
        )

