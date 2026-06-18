# 📈 ohlcpattern

**ohlcpattern** is a modern, high-performance Python library for detecting candlestick patterns in financial data. Built with `pandas` and designed for speed and ease of use, it helps traders and quantitative analysts model and identify over 40+ different market signals.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Linting: Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

---

## ✨ Key Features

- 🚀 **Fast Pattern Detection**: Optimized with `pandas` for handling large historical datasets.
- 🧩 **Comprehensive Coverage**: Support for 40+ single, double, and triple candlestick patterns.
- 🛠️ **Modern Package Structure**: Uses `src` layout and `pyproject.toml` for standard installation.
- 🧪 **Test-Driven Development**: High reliability with `pytest` integration.
- 🧹 **Clean Code**: Linted and formatted with `ruff` for maximum readability.

---

## 📦 Installation

To install the library with `pip`:

```bash
pip install ohlcpattern
```

To install the library with `uv`:

```bash
uv sync
```

For development, install with optional dependencies using `pip`:

```bash
git clone https://github.com/yourusername/ohlcpattern.git
cd ohlcpattern
pip install -e ".[dev]"
```

Or use `uv`:

```bash
git clone https://github.com/yourusername/ohlcpattern.git
cd ohlcpattern
uv sync --extra dev
```

---

## 🚀 Quick Start

Ensure your `pandas` DataFrame contains the standard `Open`, `High`, `Low`, and `Close` columns.

```python
import pandas as pd
from ohlcpattern.candlestick import CandlestickPatterns

# 1. Load your dataset
df = pd.read_csv('market_data.csv', index_col='Date', parse_dates=True)

# 2. Initialize pattern detector
csp = CandlestickPatterns(df)

# 3. Add detection categories (reversal, continue, or full)
csp._add('reversal')

# 4. Generate modeling result
modeling_data = csp.pattern_modeling()

# 5. Filter for detected patterns
detected = modeling_data[modeling_data.model != '']
print(detected[['Open', 'High', 'Low', 'Close', 'model']])
```

---

## 🖥️ CLI

The package exposes a command-line interface named `ohlcpattern`.

```bash
ohlcpattern --help
ohlcpattern --version
ohlcpattern extract market_data.csv --output patterns.csv
ohlcpattern extract --help
```

If you prefer running it through `uv`:

```bash
uv run ohlcpattern --help
uv run ohlcpattern --version
uv run ohlcpattern extract market_data.csv --output patterns.csv
uv run ohlcpattern extract --help
```

The `extract` command expects a CSV file with `Open`, `High`, `Low`, and `Close` columns. If `--output` is omitted, it prints a preview of detected patterns to the terminal.

---

## 🕯️ Supported Patterns

We support a wide variety of patterns across multiple categories:

### Reversal Patterns
| Bullish | Bearish |
| :--- | :--- |
| Hammer | Shooting Star |
| Inverted Hammer | Hanging Man |
| Bullish Engulfing | Bearish Engulfing |
| Morning Star | Evening Star |
| Piercing Pattern | Dark Cloud Cover |
| Bullish Harami | Bearish Harami |
| Tweezers Bottom | Tweezers Top |

### Continuation Patterns
- **Gaps**: Bullish Gap, Bearish Gap
- **Advanced**: Rising/Falling Three Methods, Fair Value Gaps (FVG)
- **Lines**: Separating Lines, Neck Patterns

---

## 🛠️ Development

We use `ruff` and `pytest` for quality insurance.

### Running Tests
```bash
uv run pytest src tests
```

### Linting & Formatting
```bash
uv run ruff check src
uv run ruff format src
```

---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.

---
