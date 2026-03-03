# Asset Market Structure & Speculativeness Study

This repository contains the data pipeline and computational framework for a cross‑asset market structure analysis.

The empirical findings and economic interpretation are documented in a separate research report.  
Design documents are provided separately as PDFs.

## Structure

```
phase1/        # OHLC price construction
phase2/        # Supply & volume construction
preprocessing/ # Cleaning & harmonization
analysis/      # Statistical evaluation
database/      # Schema & SQL utilities
data_reference.md
```


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

Output: normalized time‑series tables in PostgreSQL / TimescaleDB.

### Phase 2 — Trading Metadata
Monthly series of:
- Outstanding supply (or proxy)
- Trading volume

Used to compute turnover and speculativeness metrics.

## Database

- PostgreSQL + TimescaleDB
- Separate tables for:
  - `*_ohlc`
  - `*_trading_metadata`
- Interpolation based on all-time averages
- Units normalized before storage

## Reproducibility

1. Install Python ≥ 3.10 and dependencies  
2. Configure database  
3. Add your Postgres passcode in `/secrets/secrets.json`  
4. Run Phase 1 preprocessing → Run analysis for the phase 1 → Run Phase 2 preprocessing → Run analysis for the phase 2

## Scope

This repository focuses on:
- Data provenance
- Deterministic aggregation
- Reproducible time‑series construction

All methodological discussion and conclusions are presented in the accompanying report.
