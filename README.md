# Margin-Calculator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A simple Python tool to calculate profit margins based on cost and selling price.

## Features

- Calculate gross profit margin.
- Handle multiple calculations.
- Command-line interface.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Margin-Calculator.git
   ```
2. Navigate to the directory:
   ```bash
   cd Margin-Calculator
   ```
3. Install dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script:
```bash
python margin_calculator.py
```

Enter the cost price and selling price when prompted.

### Example

```python
# Sample code snippet
def calculate_margin(cost, selling):
    if cost == 0:
        return 0
    margin = ((selling - cost) / cost) * 100
    return margin

cost = 50
selling = 75
print(f"Margin: {calculate_margin(cost, selling)}%")
```

Output:
```
Margin: 50.0%
```

## Contributing

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`.
3. Commit your changes: `git commit -m 'Add feature'`.
4. Push to the branch: `git push origin feature-branch`.
5. Submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
