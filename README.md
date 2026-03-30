# Asset Market Structure & Trading Intensity Study

This repository contains the data pipeline and computational framework for a cross‑asset market structure analysis.

The empirical findings and economic interpretation are documented in a separate research report.  
Design documents are provided separately as PDFs.

The results are composed in FINAL_REPORT.pdf

## Structure
=> PROJECT_TREE.md

## Architecture

### Phase 1 — Prices (OHLC)
Assets:
- Bitcoin (hourly)
- S&P 500
- NASDAQ
- Dow Jones
- Gold
- Crude Oil
- CPI

Output: 
* normalized time‑series tables in PostgreSQL / TimescaleDB.
* Analysis of different comparative metrics (such as correlation or inflation adjusted returns)

### Phase 2 — Trading Metadata
Monthly series of:
- Outstanding supply (or proxy)
- Trading volume

Used to compute trading intensity.

## Database

- PostgreSQL + TimescaleDB
- Separate tables for:
  - `*_ohlc`
  - `*_trading_metadata`

## Reproducibility

1. Install Python (3.14.4) and poetry (2.3.2)
2. Install dependencies with `cd the/project/directory` and `poetry install`
3. Configure database  
4. Add your Postgres passcode in `/secrets/secrets.json`  
5. Run Phase 1 preprocessing → Run analysis for the phase 1 → Run Phase 2 preprocessing → Run analysis for the phase 2

## Scope

This repository focuses on:
- Data provenance
- Deterministic aggregation
- Reproducible time‑series construction

All methodological discussion and conclusions are presented in the accompanying report.
