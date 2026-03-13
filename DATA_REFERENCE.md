# Data Dictionary

Scope: This document lists the data sources used in the project, structured by Phase 1 (Prices / OHLC) and Phase 2 (Trading Metadata: Supply & Volume).  

---

# Phase 1 — Prices (OHLC)

## Bitcoin (BTC/USD, Hourly OHLC)
- Kaggle:  
  https://www.kaggle.com/datasets/mczielinski/bitcoin-historical-data

## NASDAQ Composite (Daily OHLC)
- Yahoo Finance (^IXIC):  
  https://finance.yahoo.com/quote/%5EIXIC

## S&P 500 (Daily OHLC)
- Yahoo Finance (^GSPC):  
  https://finance.yahoo.com/quote/%5EGSPC

## Dow Jones Industrial Average (Daily OHLC)
- Yahoo Finance (^DJI):  
  https://finance.yahoo.com/quote/%5EDJI

## Crude Oil — WTI (Daily OHLC)
- U.S. Energy Information Administration (EIA):  
  https://www.eia.gov/dnav/pet/hist/RWTCD.htm

## Gold — COMEX Futures (Daily OHLC)
- Yahoo Finance (GC=F):  
  https://finance.yahoo.com/quote/GC=F

## CPI (Monthly)
- FRED — CPIAUCSL:  
  https://fred.stlouisfed.org/series/CPIAUCSL
  (Adjust timeframe on the site to match the one in the project)

---

# Phase 2 — Trading Metadata (Supply & Volume)

## Bitcoin

### Supply
- Blockchain.com — Total Bitcoins in Circulation:  
  https://www.blockchain.com/explorer/charts/total-bitcoins

### Trading Volume
- The Block Data Portal:  
  https://www.theblock.pro/#data
- CME Group — Bitcoin Futures (contract specs & reports):  
  https://www.cmegroup.com/markets/cryptocurrencies/bitcoin/bitcoin.html

## S&P 500

### Supply (ETF proxy)
- iShares Core S&P 500 UCITS ETF (IE00B5BMR087):  
  https://www.ishares.com/uk/individual/en/products/253743/ishares-sp-500-b-ucits-etf-acc-fund

### Trading Volume (ETF listings)
- Yahoo Finance (various tickers from listings table + ad-hoc for invalid tickers):  
  https://finance.yahoo.com/

## NASDAQ (Nasdaq 100)

### Supply (ETF proxy)
- iShares Nasdaq 100 UCITS ETF (IE00B53SZB19):  
  https://www.ishares.com/uk/individual/en/products/253741/ishares-nasdaq-100-ucits-etf

### Trading Volume
- Yahoo Finance (various tickers from listings table):  
  https://finance.yahoo.com/

## Dow Jones

### Supply (ETF proxy)
- iShares Dow Jones Industrial Average UCITS ETF (IE00B53L4350):  
  https://www.ishares.com/uk/individual/en/products/253713/ishares-dow-jones-industrial-average-ucits-etf

### Trading Volume
- Yahoo Finance (various tickers from listings table):  
  https://finance.yahoo.com/

## Gold

### Supply
- World Gold Council — Gold Demand & Supply Data:  
  https://www.gold.org/goldhub/data/gold-demand-by-country

### Trading Volume
- CME Group Monthly Reports (COMEX):  
  https://www.cmegroup.com/ftp/webmthly/
- Shanghai Futures Exchange (SHFE):  
  https://www.shfe.com.cn/eng/reports/StatisticalData/MonthlyData/
- Japan Exchange Group (JPX) Monthly Statistics:  
  https://www.jpx.co.jp/english/markets/statistics-equities/misc/index.html

## Oil

### Supply
- EIA — OPEC Revenues / Production Data:  
  https://www.eia.gov/international/analysis/special-topics/OPEC-Revenues-Fact-Sheet

### Trading Volume
- CME Group Monthly Reports (NYMEX):  
  https://www.cmegroup.com/ftp/webmthly/
- ICE Futures Europe Statistics:  
  https://ir.theice.com/home/default.aspx

