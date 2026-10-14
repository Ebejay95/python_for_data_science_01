# ft_package

A sample test package.

## Build

```bash
pip install build
python -m build
```

This creates:

- `dist/ft_package-0.0.1.tar.gz`
- `dist/ft_package-0.0.1-py3-none-any.whl`

## Install

```bash
pip install ./dist/ft_package-0.0.1.tar.gz
# or
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

## Usage

```python
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))  # output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu"))  # output: 0
```
