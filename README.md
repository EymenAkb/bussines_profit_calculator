# Bussines_profit_calculator

This repository was developed by **EymenAkb** as part of summarizing the business profit and tax.

## Description

This program takes dataset and summarizes it with adjustable information.
This program is about understanding details about your business.

Some of the interactive sections and descriptions are given below:

- `Analysis Peripd` : Used for chosing which years you want to summarize and get details on.
- `MarkUp Rate (%)` : Given the cost value of the product it will calculate the MarkUp Rate.
- `Product Tax (%)` : The tax as percentage 
- `Net profit Tax (%)` : Tax amount you pay after your cost got out of the gross profit.

*Note:* This program is also going to include margin rate and expenses, right now they are at the developement phase.

---

Other checkbox display options and their descriptions are given below:

- `Round prices` : When it is true the program will round up the prices, however this might show wrong information about earnings.
- `Smooth Charts (spline)` : This is for showcasing better the data, however this might also show wrong information about data but it will not effect anything except visual part.

#### Note

This program takes normal csv files for developing phase but it will be updated. The dataset must have to contain two columns given below:

- `Date` : Year based date column it can only contain years without months and days. formatting must have to be as YYYY.
- `Cost` : The cost only for one unit, based on MarkUp rate program will calculate profit automatically
- `Sales` : This is the quantity of the unit sold for a year.

## Required libraries

Some libraries which are essential for business profit calculator:

- `Pandas` : Interpreting, importing and everything about data.
- `Plotly` : Making the charts interactive, detailed and more modern.
- `Streamlit` : For putting an UI and UX on top of the plots.

## Usage

You can copy or fork the code for changing any details and usage.
If you want any details and visualizing about it [Business Profit Calculator](https://businessprofitcalculator.streamlit.app/) can give you visual details about it.

## Note

*This app doesn't have margin rate currently but it is in progress*
