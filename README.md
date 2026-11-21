# go-thistle

![CI](https://img.shields.io/github/actions/workflow/status/gregsextonziz/go-thistle/ci.yml?branch=main&label=CI) ![Python](https://img.shields.io/badge/python-3.10+-blue) ![Jupyter](https://img.shields.io/badge/jupyter-notebook-F37626) ![License](https://img.shields.io/github/license/gregsextonziz/go-thistle?color=blue)

An exploratory data analysis toolkit with Jupyter notebooks and a CLI pipeline. go-thistle covers the full workflow: load CSV data, clean and deduplicate, compute summary statistics, and generate plots (time-series, distribution). Uses pandas, NumPy, Matplotlib, Seaborn, and Plotly. Results are cached for reproducibility.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Running Tests](#running-tests)
- [Contributing](#contributing)
- [Changelog](#changelog)
- [License](#license)

## Features

- CLI entry point: `python scripts/run_analysis.py --data data/ --output results/`
- Matplotlib time-series plot with configurable figsize and DPI
- Plotly for optional interactive charts
- Data cleaning pipeline: dedup, dropna, type coercion, timestamp parsing
- Summary statistics: count, mean, std, min, max

## Prerequisites

- Python 3.10 or higher
- Jupyter Notebook or JupyterLab
- pip for installing dependencies

## Installation

```bash
git clone https://github.com/gregsextonziz/go-thistle.git
cd go-thistle
pip install -r requirements.txt
jupyter notebook
```

## Usage

```bash
# Run the full analysis pipeline
python scripts/run_analysis.py --data data/raw/ --output results/
# => Loading data from data/raw/...
# => Loaded 10000 rows
# => Stats: count=10000, mean=42.5, std=15.3, min=0.0, max=100.0
# => Plots saved to results/

# Or open the interactive notebook
jupyter notebook notebooks/analysis.ipynb

# View generated plots
ls results/*.png
# results/timeseries.png  results/distribution.png
```

## Project Structure

```
go-thistle/
├── scripts/run_analysis.py
├── notebooks/analysis.ipynb
├── data/  results/
├── requirements.txt
├── README.md  LICENSE  CHANGELOG.md  CONTRIBUTING.md  CODE_OF_CONDUCT.md
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   └── PULL_REQUEST_TEMPLATE.md
└── .gitignore
```

## Running Tests

```bash
# Verify the pipeline runs end-to-end
python scripts/run_analysis.py --data data/ --output results/

# Or run the notebook
jupyter notebook notebooks/analysis.ipynb
```

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

Quick start:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Make your changes and run tests (see [Running Tests](#running-tests) above)
4. Commit with a clear message: `git commit -am 'Add: my feature'`
5. Push to your fork: `git push origin feature/my-feature`
6. Open a Pull Request

Please ensure all tests pass before submitting a pull request.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for a list of changes and version history.

## License

This project is licensed under the GPL-3.0 -- see the [LICENSE](LICENSE) file for details.

Copyright (c) 2026 kenji silva.

## Acknowledgements

- Built with pandas, NumPy, Matplotlib, Seaborn, and Plotly
- CI/CD powered by [GitHub Actions](https://github.com/features/actions)
- Badges by [shields.io](https://shields.io)
- Inspired by best practices from the open-source community
