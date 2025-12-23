/*
Before running this file make sure you have timescale extension installed (https://www.tigerdata.com/docs/self-hosted/latest/install/installation-linux#install-timescale_db-on-linux)
and enabled (if not, use CREATE EXTENSION IF NOT EXISTS timescaledb).
Check with "\dx" in psql CLI 
The resulting table should look something like this:
                                                List of installed extensions
    Name     | Version |   Schema   |                                      Description
-------------+---------+------------+---------------------------------------------------------------------------------------
 plpgsql     | 1.0     | pg_catalog | PL/pgSQL procedural language                                                          
 timescaledb | 2.22.0  | public     | Enables scalable inserts and complex queries for time-series data (Community Edition) 

Phase 1 */
create table if not exists bitcoin_ohlc (
	ts timestamp primary key,
	open double precision,
	high double precision,
	low double precision,
	close double precision
)
with (
	timescaledb.hypertable,
	timescaledb.orderby = ts,
	timescaledb.partition_column = ts
)
tablespace "external";


create table if not exists nasdaq_ohlc (
	ts timestamp primary key,
	open double precision,
	high double precision,
	low double precision,
	close double precision
)
with (
	timescaledb.hypertable,
	timescaledb.orderby = ts,
	timescaledb.partition_column = ts
)
tablespace "external";


create table if not exists snp_ohlc (
	ts timestamp primary key,
	open double precision,
	high double precision,
	low double precision,
	close double precision
)
with (
	timescaledb.hypertable,
	timescaledb.orderby = ts,
	timescaledb.partition_column = ts
)
tablespace "external";


create table if not exists dow_jones_ohlc (
	ts timestamp primary key,
	open double precision,
	high double precision,
	low double precision,
	close double precision
)
with (
	timescaledb.hypertable,
	timescaledb.orderby = ts,
	timescaledb.partition_column = ts
)
tablespace "external";


create table if not exists oil_ohlc (
	dt date primary key,
	open double precision,
	high double precision,
	low double precision,
	close double precision
)
with (
	timescaledb.hypertable,
	timescaledb.orderby = dt,
	timescaledb.partition_column = dt
)
tablespace "external";


create table if not exists gold_ohlc (
	dt date primary key,
	open double precision,
	high double precision,
	low double precision,
	close double precision
)
with (
	timescaledb.hypertable,
	timescaledb.orderby = dt,
	timescaledb.partition_column = dt
)
tablespace "external";


create table if not exists cpi (
	dt date primary key,
	value double precision
)
with (
	timescaledb.hypertable,
	timescaledb.orderby = dt,
	timescaledb.partition_column = dt
)
tablespace "external";


/* Phase 2*/
create table if not exists bitcoin_trading_metadata (
	dt date primary key,
	outstanding_supply double precision constraint valid_outstanding_supply check (outstanding_supply is null or outstanding_supply > 0),
	trading_volume double precision constraint valid_trading_volume check (trading_volume is null or trading_volume > 0)
)
with (
	timescaledb.hypertable,
	timescaledb.orderby = dt,
	timescaledb.partition_column = dt
)
tablespace "external";


create table if not exists snp_trading_metadata (
	dt date primary key,
	outstanding_supply double precision constraint valid_outstanding_supply check (outstanding_supply is null or outstanding_supply > 0),
	trading_volume double precision constraint valid_trading_volume check (trading_volume is null or trading_volume > 0)
)
with (
	timescaledb.hypertable,
	timescaledb.orderby = dt,
	timescaledb.partition_column = dt
)
tablespace "external";


create table if not exists nasdaq_trading_metadata (
	dt date primary key,
	outstanding_supply double precision constraint valid_outstanding_supply check (outstanding_supply is null or outstanding_supply > 0),
	trading_volume double precision constraint valid_trading_volume check (trading_volume is null or trading_volume > 0)
)
with (
	timescaledb.hypertable,
	timescaledb.orderby = dt,
	timescaledb.partition_column = dt
)
tablespace "external";


create table if not exists dow_jones_trading_metadata (
	dt date primary key,
	outstanding_supply double precision constraint valid_outstanding_supply check (outstanding_supply is null or outstanding_supply > 0),
	trading_volume double precision constraint valid_trading_volume check (trading_volume is null or trading_volume > 0)
)
with (
	timescaledb.hypertable,
	timescaledb.orderby = dt,
	timescaledb.partition_column = dt
)
tablespace "external";


create table if not exists oil_trading_metadata (
	dt date primary key,
	outstanding_supply double precision constraint valid_outstanding_supply check (outstanding_supply is null or outstanding_supply > 0),
	trading_volume double precision constraint valid_trading_volume check (trading_volume is null or trading_volume > 0)
)
with (
	timescaledb.hypertable,
	timescaledb.orderby = dt,
	timescaledb.partition_column = dt
)
tablespace "external";


create table if not exists gold_trading_metadata (
	dt date primary key,
	outstanding_supply double precision constraint valid_outstanding_supply check (outstanding_supply is null or outstanding_supply > 0),
	trading_volume double precision constraint valid_trading_volume check (trading_volume is null or trading_volume > 0)
)
with (
	timescaledb.hypertable,
	timescaledb.orderby = dt,
	timescaledb.partition_column = dt
)
tablespace "external";

