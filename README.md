# trading-algo
# 📈 EMA Crossover Strategy Simulation for NIFTY 50

This Python script simulates a basic **EMA crossover trading strategy** for the **NIFTY 50** index using historical data. It demonstrates **buy/sell logic** based on 5-day and 9-day EMA crossovers, with a fixed **target profit** and **stop loss** mechanism.

---

## 🧰 Requirements

- Python 3.x
- `yfinance`
- `pandas`
- `matplotlib`

Install dependencies:

```bash
pip install yfinance pandas matplotlib
```

---

## 📊 Strategy Logic

- **Buy Signal:** When 5 EMA crosses above 9 EMA.
- **Sell Signals:**
  - Target profit of **1.5%** reached.
  - Stop loss of **0.5%** triggered.
  - 5 EMA crosses back below 9 EMA (manual exit).

---

## 📌 Key Parameters

| Parameter         | Value         | Description                          |
|------------------|---------------|--------------------------------------|
| `ticker`         | `^NSEI`       | NIFTY 50 Index                       |
| `start`          | `2023-01-01`  | Start date for data                 |
| `end`            | `2024-12-31`  | End date for data                   |
| `interval`       | `1d`          | Daily data interval                  |
| `EMA spans`      | 5, 9          | Short-term EMAs used for crossover  |
| `target_pct`     | `0.015`       | 1.5% target                          |
| `stop_loss_pct`  | `0.005`       | 0.5% stop loss                       |
| `initial_balance`| `₹100,000` | Starting capital                     |

---

## 📊 Output

- **Trade Log:** Date-wise log of BUY and SELL actions.
- **Final Portfolio Value:** Net value after all trades.
- **Total Profit/Loss:** Total gain or loss in ₹.
- **Price Chart:** Visual representation with EMA lines and close price.

---

## 📌 Example Output

```bash
Trade Log:
2023-02-10 - BUY at ₹17865.40
2023-02-14 - SELL (TARGET) at ₹18133.38

Final Portfolio Value: ₹101500.00
Total Profit/Loss: ₹1500.00
```

---

## 📉 Visualization

- Plots the **Close Price**, **EMA 5**, and **EMA 9**.
- Highlights trend direction and crossover points.

---

## 🧐 How It Works (Behind the Scenes)

1. Downloads historical NIFTY 50 data using `yfinance`.
2. Computes 5-day and 9-day EMAs.
3. Simulates trades based on crossover logic:
   - Entry on bullish crossover.
   - Exit on target, stop loss, or bearish crossover.
4. Maintains a trade log and calculates portfolio performance.
5. Plots the results for visual analysis.

---

## 📝 Notes

- This is a **simulation**, not connected to any live trading platform.
- No trading fees/slippage are considered.
- Can be extended to real trading via broker APIs like **Dhan**, **Zerodha**, etc.

---

## 🚀 Future Enhancements (Optional Ideas)

- Add **backtesting metrics** (Win rate, Sharpe ratio, etc.)
- Highlight buy/sell points on the chart.
- Use **candlestick** charts.
- Add **position sizing** and **risk management**.


backtesting:
[*********************100%***********************]  1 of 1 completed

Trade Log:
2023-01-18 - BUY at ₹18165.35
2023-01-20 - SELL (STOP LOSS) at ₹18027.65
2023-02-09 - BUY at ₹17893.45
2023-02-13 - SELL (STOP LOSS) at ₹17770.90
2023-03-08 - BUY at ₹17754.40
2023-03-09 - SELL (STOP LOSS) at ₹17589.60
2023-03-31 - BUY at ₹17359.75
2023-04-10 - SELL (TARGET) at ₹17624.05
2023-09-04 - BUY at ₹19528.80
2023-09-11 - SELL (TARGET) at ₹19996.35
2023-10-11 - BUY at ₹19811.35
2023-10-18 - SELL (STOP LOSS) at ₹19671.10
2023-11-06 - BUY at ₹19411.75
2023-11-16 - SELL (TARGET) at ₹19765.20
2024-01-31 - BUY at ₹21725.70
2024-02-12 - SELL (STOP LOSS) at ₹21616.05
2024-02-13 - BUY at ₹21743.25
2024-02-19 - SELL (TARGET) at ₹22122.25
2024-03-28 - BUY at ₹22326.90
2024-04-08 - SELL (TARGET) at ₹22666.30
2024-04-25 - BUY at ₹22570.35
2024-04-26 - SELL (STOP LOSS) at ₹22419.95
2024-05-17 - BUY at ₹22466.10
2024-05-23 - SELL (TARGET) at ₹22967.65
2024-06-03 - BUY at ₹23263.90
2024-06-04 - SELL (STOP LOSS) at ₹21884.50
2024-06-06 - BUY at ₹22821.40
2024-06-07 - SELL (TARGET) at ₹23290.15
2024-08-19 - BUY at ₹24572.65
2024-08-26 - SELL (TARGET) at ₹25010.60
2024-09-12 - BUY at ₹25388.90
2024-09-20 - SELL (TARGET) at ₹25790.95
2024-11-25 - BUY at ₹24221.90
2024-11-28 - SELL (STOP LOSS) at ₹23914.15

Final Portfolio Value: ₹104959.18
Total Profit/Loss: ₹4959.18
