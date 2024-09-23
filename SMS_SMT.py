{\rtf1\ansi\ansicpg936\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\froman\fcharset0 TimesNewRomanPSMT;\f1\froman\fcharset0 Times-Roman;\f2\fnil\fcharset134 STSongti-SC-Regular;
}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
\margl1440\margr1440\vieww30040\viewh17760\viewkind0
\deftab720
\pard\pardeftab720\sa240\partightenfactor0

\f0\fs32 \cf0 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 #Calculate the RSI
\f1\fs24 \

\f0\fs32 file_path = '/mnt/data/
\f2 \'b9\'c9\'bc\'db
\f0 .xlsx'
\f1\fs24 \

\f0\fs32 data = pd.read_excel(file_path)
\f1\fs24 \

\f0\fs32 data.columns = data.columns.str.strip()
\f1\fs24 \

\f0\fs32 data = data.set_index('
\f2 \'c8\'d5\'c6\'da
\f0 ')
\f1\fs24 \

\f0\fs32 def calculate_rsi(data, window=14):
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0delta = data.diff(1)
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0rs = gain / loss
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0rsi = 100 - (100 / (1 + rs))
\f1\fs24 \

\f0\fs32 return rsi
\f1\fs24 \

\f0\fs32 rsi_data = data.apply(calculate_rsi)
\f1\fs24 \

\f0\fs32 tools.display_dataframe_to_user(name="RSI
\f2 \'d6\'b5
\f0 ", dataframe=rsi_data)
\f1\fs24 \

\f0\fs32 rsi_data.tail()
\f1\fs24 \

\f0\fs32 \'a0
\f1\fs24 \

\f0\fs32 #The rest processes are handled in Excel
\f1\fs24 \
\

\f0\fs32 import pandas as pd
\f1\fs24 \

\f0\fs32 import numpy as np
\f1\fs24 \

\f0\fs32 import matplotlib.pyplot as plt
\f1\fs24 \

\f0\fs32 \'a0
\f1\fs24 \

\f0\fs32 # Define the file paths for the initial and new data
\f1\fs24 \

\f0\fs32 initial_file_paths = [
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0'/mnt/data/600028_
\f2 \'d6\'d0\'b9\'fa\'ca\'af\'bb\'af
\f0 (2).csv',
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0'/mnt/data/600030_
\f2 \'d6\'d0\'d0\'c5\'d6\'a4\'c8\'af
\f0 (2).csv',
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0'/mnt/data/600031_
\f2 \'c8\'fd\'d2\'bb\'d6\'d8\'b9\'a4
\f0 .csv',
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0'/mnt/data/600036_
\f2 \'d5\'d0\'c9\'cc\'d2\'f8\'d0\'d0
\f0 .csv',
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0'/mnt/data/600050_
\f2 \'d6\'d0\'b9\'fa\'c1\'aa\'cd\'a8
\f0 (1).csv',
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0'/mnt/data/600104_
\f2 \'c9\'cf\'c6\'fb\'bc\'af\'cd\'c5
\f0 .csv',
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0'/mnt/data/600196_
\f2 \'b8\'b4\'d0\'c7\'d2\'bd\'d2\'a9
\f0 .csv',
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0'/mnt/data/600111_
\f2 \'b1\'b1\'b7\'bd\'cf\'a1\'cd\'c1
\f0 .csv'
\f1\fs24 \

\f0\fs32 ]
\f1\fs24 \

\f0\fs32 \'a0
\f1\fs24 \

\f0\fs32 new_file_paths = [
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0'/mnt/data/600519_
\f2 \'b9\'f3\'d6\'dd\'c3\'a9\'cc\'a8
\f0 (1).csv',
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0'/mnt/data/600522_
\f2 \'d6\'d0\'cc\'ec\'bf\'c6\'bc\'bc
\f0 .csv',
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0'/mnt/data/600606_
\f2 \'c2\'cc\'b5\'d8\'bf\'d8\'b9\'c9
\f0 .csv',
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0'/mnt/data/600760_
\f2 \'d6\'d0\'ba\'bd\'c9\'f2\'b7\'c9
\f0 .csv',
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0'/mnt/data/600958_
\f2 \'b6\'ab\'b7\'bd\'d6\'a4\'c8\'af
\f0 .csv',
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0'/mnt/data/601066_
\f2 \'d6\'d0\'d0\'c5\'bd\'a8\'cd\'b6
\f0 .csv',
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0'/mnt/data/601216_
\f2 \'be\'fd\'d5\'fd\'bc\'af\'cd\'c5
\f0 .csv',
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0'/mnt/data/601318_
\f2 \'d6\'d0\'b9\'fa\'c6\'bd\'b0\'b2
\f0 (1).csv',
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0'/mnt/data/601600_
\f2 \'d6\'d0\'b9\'fa\'c2\'c1\'d2\'b5
\f0 .csv',
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0'/mnt/data/601628_
\f2 \'d6\'d0\'b9\'fa\'c8\'cb\'ca\'d9
\f0 (1).csv',
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0'/mnt/data/601633_
\f2 \'b3\'a4\'b3\'c7\'c6\'fb\'b3\'b5
\f0 .csv',
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0'/mnt/data/601668_
\f2 \'d6\'d0\'b9\'fa\'bd\'a8\'d6\'fe
\f0 .csv',
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0'/mnt/data/601766_
\f2 \'d6\'d0\'b9\'fa\'d6\'d0\'b3\'b5
\f0 (1).csv',
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0'/mnt/data/601899_
\f2 \'d7\'cf\'bd\'f0\'bf\'f3\'d2\'b5
\f0 .csv',
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0'/mnt/data/601985_
\f2 \'d6\'d0\'b9\'fa\'ba\'cb\'b5\'e7
\f0 .csv',
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0'/mnt/data/603288_
\f2 \'ba\'a3\'cc\'ec\'ce\'b6\'d2\'b5
\f0 .csv'
\f1\fs24 \

\f0\fs32 ]
\f1\fs24 \

\f0\fs32 \'a0
\f1\fs24 \

\f0\fs32 # Load all CSV files into a single dataframe
\f1\fs24 \

\f0\fs32 dataframes = []
\f1\fs24 \

\f0\fs32 for file_path in initial_file_paths + new_file_paths:
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0df = pd.read_csv(file_path)
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0df['Stock'] = file_path.split('/')[-1].split('_')[1]
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0dataframes.append(df)
\f1\fs24 \

\f0\fs32 \'a0
\f1\fs24 \

\f0\fs32 # Concatenate all dataframes
\f1\fs24 \

\f0\fs32 combined_df = pd.concat(dataframes, ignore_index=True)
\f1\fs24 \

\f0\fs32 \'a0
\f1\fs24 \

\f0\fs32 # Convert the date column to datetime format
\f1\fs24 \

\f0\fs32 combined_df['
\f2 \'c8\'d5\'c6\'da
\f0 '] = pd.to_datetime(combined_df['
\f2 \'c8\'d5\'c6\'da
\f0 '], format='%Y-%m-%d')
\f1\fs24 \

\f0\fs32 \'a0
\f1\fs24 \

\f0\fs32 # Calculate daily returns for each stock
\f1\fs24 \

\f0\fs32 combined_df['Daily_Return'] = combined_df.groupby('Stock')['
\f2 \'bc\'db\'b8\'f1
\f0 '].pct_change()
\f1\fs24 \

\f0\fs32 \'a0
\f1\fs24 \

\f0\fs32 # Drop rows with NaN values (resulting from pct_change calculation)
\f1\fs24 \

\f0\fs32 combined_df = combined_df.dropna(subset=['Daily_Return'])
\f1\fs24 \

\f0\fs32 \'a0
\f1\fs24 \

\f0\fs32 # Calculate cumulative return for each stock
\f1\fs24 \

\f0\fs32 combined_df['Cumulative_Return'] = (1 + combined_df['Daily_Return']).groupby(combined_df['Stock']).cumprod() - 1
\f1\fs24 \

\f0\fs32 \'a0
\f1\fs24 \

\f0\fs32 # Calculate volatility (annualized standard deviation of daily returns)
\f1\fs24 \

\f0\fs32 volatility = combined_df.groupby('Stock')['Daily_Return'].std() * np.sqrt(252)
\f1\fs24 \

\f0\fs32 \'a0
\f1\fs24 \

\f0\fs32 # Calculate the annualized return
\f1\fs24 \

\f0\fs32 annualized_return = combined_df.groupby('Stock')['Daily_Return'].mean() * 252
\f1\fs24 \

\f0\fs32 \'a0
\f1\fs24 \

\f0\fs32 # Assume a risk-free rate (e.g., 3% or 0.03 for this example)
\f1\fs24 \

\f0\fs32 risk_free_rate = 0.03
\f1\fs24 \

\f0\fs32 \'a0
\f1\fs24 \

\f0\fs32 # Calculate the Sharpe Ratio
\f1\fs24 \

\f0\fs32 sharpe_ratio = (annualized_return - risk_free_rate) / volatility
\f1\fs24 \

\f0\fs32 \'a0
\f1\fs24 \

\f0\fs32 # Calculate Value at Risk (VaR) at 95% confidence interval
\f1\fs24 \

\f0\fs32 z_score_95 = -1.645 \'a0# 95% confidence interval
\f1\fs24 \

\f0\fs32 mean_daily_return = combined_df.groupby('Stock')['Daily_Return'].mean()
\f1\fs24 \

\f0\fs32 std_daily_return = combined_df.groupby('Stock')['Daily_Return'].std()
\f1\fs24 \

\f0\fs32 VaR_95 = mean_daily_return + std_daily_return * z_score_95
\f1\fs24 \

\f0\fs32 \'a0
\f1\fs24 \

\f0\fs32 # Create a summary dataframe with all calculated metrics
\f1\fs24 \

\f0\fs32 pnl_summary_final = pd.DataFrame(\{
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0'Annualized_Return': annualized_return,
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0'Volatility': volatility,
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0'Sharpe_Ratio': sharpe_ratio,
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0'VaR_95': VaR_95
\f1\fs24 \

\f0\fs32 \}).reset_index()
\f1\fs24 \

\f0\fs32 \'a0
\f1\fs24 \

\f0\fs32 # Display the summary dataframe
\f1\fs24 \

\f0\fs32 import ace_tools as tools; tools.display_dataframe_to_user(name="PnL Summary of Stocks (Final Data)", dataframe=pnl_summary_final)
\f1\fs24 \

\f0\fs32 \'a0
\f1\fs24 \

\f0\fs32 # Plot the final PnL graph showing cumulative returns for each stock
\f1\fs24 \

\f0\fs32 plt.figure(figsize=(14, 8))
\f1\fs24 \

\f0\fs32 \'a0
\f1\fs24 \

\f0\fs32 for stock in combined_df['Stock'].unique():
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0stock_data = combined_df[combined_df['Stock'] == stock]
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0plt.plot(stock_data['
\f2 \'c8\'d5\'c6\'da
\f0 '], stock_data['Cumulative_Return'], label=stock)
\f1\fs24 \

\f0\fs32 \'a0
\f1\fs24 \

\f0\fs32 plt.title('Cumulative Returns of Different Stocks (Final Data)')
\f1\fs24 \

\f0\fs32 plt.xlabel('Date')
\f1\fs24 \

\f0\fs32 plt.ylabel('Cumulative Return')
\f1\fs24 \

\f0\fs32 plt.legend()
\f1\fs24 \

\f0\fs32 plt.grid(True)
\f1\fs24 \

\f0\fs32 plt.xticks(rotation=45)
\f1\fs24 \

\f0\fs32 plt.tight_layout()
\f1\fs24 \

\f0\fs32 \'a0
\f1\fs24 \

\f0\fs32 # Show the plot
\f1\fs24 \

\f0\fs32 plt.show()
\f1\fs24 \

\f0\fs32 ( The dataset are using the same with other group members)
\f1\fs24 \
}