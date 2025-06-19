# 📈 AlphaSage: Quant Stock Screener & Backtest Framework

**AlphaSage** is a senior-level Python-based platform for developing, evaluating, and publishing quantitative equity strategies. Built for real-world alpha generation, it includes a modular simulation engine, formal research publishing via Quarto, and an optional Streamlit dashboard for visualizing and interacting with results.

---

## 🚀 Key Features

- **Strategy Scoring Engine** – Create and test strategies like momentum, value, or factor blends.
- **Backtest Framework** – Simulate historical performance with custom rebalancing, metrics, and logs.
- **Streamlit Dashboard** – Run parameterized simulations, view equity curves, and explore top picks.
- **Quarto Research Hub** – Publish professional-grade reports with inline charts, formulas, and logic.
- **Robinhood-Ready** – Export signals for paper trading or future integration with real-world brokerage.

---

## 📂 Project Structure

```
AlphaSage/
├── data/                # Raw, processed, and external data sources
├── src/                 # Core logic: data, scoring, backtesting, metrics
├── streamlit_app/       # Interactive dashboard components
├── quarto/              # Modular Quarto research docs (not a book-style site)
├── docs/                # Internal dev notes and implementation details
├── tests/               # Unit tests for major modules
├── outputs/             # Backtest results and CSV trade signals
├── run_pipeline.py      # Main entry point to run the full pipeline
└── README.md            # This file
```

---

## 🧠 Strategy Types

You can build and test strategies such as:

- **Momentum**: Buy what’s going up.
- **Value**: Buy what’s cheap.
- **Mean Reversion**: Bet on bouncebacks.
- **Factor Combo**: Blend multiple scoring signals.

---

## 📊 Performance Metrics

Each backtest will produce:

- Cumulative returns
- Alpha vs benchmark
- Sharpe ratio
- Max drawdown
- Rolling metrics
- Monthly return heatmaps

---

## 📖 Live Research Reports (via Quarto)

Navigate to the [`quarto/`](quarto/) folder and run:

```bash
quarto preview
```

Or render individual strategy reports using:

```bash
quarto render strategy_momentum.qmd
```

---

## 🛠 Setup Instructions

1. Clone this repository:
```bash
git clone https://github.com/your-user/AlphaSage.git
cd AlphaSage
```

2. Install dependencies:
```bash
pip install -r requirements.txt
# or
conda env create -f environment.yml
```

3. Run the pipeline:
```bash
python run_pipeline.py
```

---

## 📃 License

MIT License. See `LICENSE` file for details.

---

## 🔍 SEO Metadata

> Keywords: quantitative finance, stock screener, alpha generation, backtest engine, financial modeling, portfolio optimization, momentum strategy, value investing, streamlit, quarto, python finance, robinhood quant, factor models

---

## 👤 Author

**Brice A. Nelson**  
[LinkedIn](https://www.linkedin.com/in/brice-a-nelson-p-e-mba-36b28b15/) | [Website](https://www.devbybrice.com/) | [Medium](https://medium.com/@quantshift)

---

AlphaSage: Because alpha doesn’t find itself. 📊