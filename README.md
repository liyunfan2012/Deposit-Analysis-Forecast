# FDIC Insured Financial Institution Deposit Analysis and Forecast Model



## Overview

This project builds a predictive model to forecast quarterly 
deposit balances at FDIC-insured financial institutions using macroeconomic 
indicators from the Federal Reserve Economic Data (FRED) database. 
The model leverages historical economic data and engineered features to predict deposit trends.


## Repository Contents
-  **0.Extract Raw Data**

    Data extraction pipeline that extract quarterly economic data from two sources:

    FRED API: Downloads 25+ macroeconomic indicators (GDP, employment, interest rates, inflation, etc.) from 2000-present → `raw_FRED.csv`.
    
    FDIC Excel File: Extracts bank deposit data from quarterly reports → `raw_FDIC_deposits.csv`.
    
    Both datasets use a timekey index `(year-1980)×4+(quarter-1)` for time-series alignment.


- **1.Data Preparation**

    Feature engineering pipeline transforms raw economic data into modeling-ready data.
  - **FRED Macroeconomic variables**:
    
      - Growth rates (QoQ, YoY) for economic indicators.
      - Interest rate changes and spreads (yield curve, credit spreads, mortgage spreads).
      - Ratios (savings/income, credit/income, debt/GDP).
      - Lagged variables (1-12 quarters) and rolling averages.
      - Momentum indicators (rate of change).
    
  - **FDIC Target Variables**: 

      Processes FDIC deposit data to calculate quarterly average balances and growth ratios for domestic, 
  interest-bearing, non-interest-bearing, and time deposits.
    
  - **Output**:

      Merges all features into full_modeling.csv with 86 quarterly samples (Q4 2000 onwards) 
  and 256 driver variables for predictive modeling.


- **2.Data Exploration**

    Preliminary rexploration of data, plot trend of target variables and major drivers.


- **3.1 Model building linear**
    
    Builds linear regression models to predict deposit balances, conducted model diagnosis and backtesting.


- **3.2 Model building parceling**

    Builds logistic regression models to predict deposit balances, conducted model diagnosis and backtesting.


- **3.3 Model building IB**

    Builds linear regression models to predict interest bearing deposit balances, conducted model diagnosis and backtesting.


- **3.4 Model building NIB**

    Builds linear regression models to predict non-interest bearing deposit balances, conducted model diagnosis and backtesting.


- **3.5 Model building Timedeposit**

    Builds linear regression models to predict time deposit balances, conducted model diagnosis and backtesting.


- **`data`**

    Raw data and processed modeling data are in thi repository.

- **`figures`**

    Figures for data exploration and model performance are saved here.