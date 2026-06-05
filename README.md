# 🔐 Password Strength Analyzer

A simple Python program that evaluates the strength of a password using common security rules.

## Features

- Minimum length check (8+ characters)
- Uppercase letter detection
- Lowercase letter detection
- Number detection
- Special character detection
- Classifies passwords as Weak, Medium, or Strong

## Code

```python
import re

print("Password Strength Analyzer")

password = input("Enter password: ")

score = sum([
    len(password) >= 8,
    bool(re.search(r'[A-Z]', password)),
    bool(re.search(r'[a-z]', password)),
    bool(re.search(r'\d', password)),
    bool(re.search(r'[^A-Za-z0-9]', password))
])

print("Strong" if score >= 5 else "Medium" if score >= 3 else "Weak")
```

## Requirements

- Python 3.x

## Run

```bash
python main.py
```

## Concepts Used

- Python Input/Output
- Regular Expressions (`re`)
- Boolean Logic
- Conditional Expressions

---

Made with Python 🐍
