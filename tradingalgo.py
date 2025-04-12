import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Fetch NIFTY 50 historical data
ticker = '^NSEI'
df = yf.download(ticker, start='2023-01-01', end='2024-12-31', interval='1d')

# Calculate EMA
df['EMA5'] = df['Close'].ewm(span=5, adjust=False).mean()
df['EMA9'] = df['Close'].ewm(span=9, adjust=False).mean()

# Initialize trading parameters
in_trade = False
target_pct = 0.015  # 1.5% target
stop_loss_pct = 0.005  # 0.5% stop loss

# Simulate trades
initial_balance = 100000
balance = initial_balance
holding = 0
trade_log = []

# Loop through data
for i in range(1, len(df)):
    today = df.iloc[i]
    prev = df.iloc[i - 1]
    
    price = today['Close']
    ema5 = today['EMA5']
    ema9 = today['EMA9']
    prev_ema5 = prev['EMA5']
    prev_ema9 = prev['EMA9']
    
    # Crossover BUY signal
    if not in_trade and prev_ema5.item() < prev_ema9.item() and ema5.item() > ema9.item():  
        buy_price = price.item() 
        holding = balance / price.item()
        balance = 0
        in_trade = True
        trade_log.append((df.index[i], 'BUY', price.item())) 
    
    # If in trade, check for:
    if in_trade:
        # Target hit
        if price.item() >= buy_price * (1 + target_pct):
            balance = holding * price.item()
            holding = 0
            in_trade = False
            trade_log.append((df.index[i], 'SELL (TARGET)', price.item()))
        
        # Stop loss hit
        elif price.item() <= buy_price * (1 - stop_loss_pct): 
            balance = holding * price.item()
            holding = 0
            in_trade = False
            trade_log.append((df.index[i], 'SELL (STOP LOSS)', price.item()))
        
        # EMA crossover down (manual exit)
        elif prev_ema5.item() > prev_ema9.item() and ema5.item() < ema9.item():  
            balance = holding * price.item()
            holding = 0
            in_trade = False
            trade_log.append((df.index[i], 'SELL (CROSSOVER)', price.item()))

# Final value
final_value = balance if not in_trade else holding * df['Close'].iloc[-1]
profit = final_value - initial_balance

# Print results
print("\nTrade Log:")
for t in trade_log:
    print(f"{t[0].date()} - {t[1]} at ₹{t[2]:.2f}")

print(f"\nFinal Portfolio Value: ₹{final_value:.2f}")
print(f"Total Profit/Loss: ₹{profit:.2f}")

# Plotting
plt.figure(figsize=(14, 6))
plt.plot(df['Close'], label='Close Price', color='black')
plt.plot(df['EMA5'], label='EMA 5', color='blue', linestyle='--')
plt.plot(df['EMA9'], label='EMA 9', color='red', linestyle='--')
plt.title('EMA Crossover with Target and Stop Loss')
plt.xlabel('Date')
plt.ylabel('Price')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
