# Lab 1: Python Basics

Short functions from the textbook's R-1 exercises.

| Function | Problem | Approach |
|----------|---------|----------|
| `is_multiple(n, m)` | R-1.1 | Modulo: `n % m == 0` |
| `is_even(k)` | R-1.2 | No `*`, `/`, or `%` allowed, so it checks the last bit with `k & 1` |
| `minmax(data)` | R-1.3 | One pass tracking the smallest and largest values, without `min`/`max` |
| `sum_of_squares(n)` | R-1.4 | Loop adding `i * i` for every positive integer below `n` |

## Running

The functions have test cases as comments under each one. Uncomment them, or import the functions:

```bash
python3 -c "from main import *; print(is_even(6), minmax([3, 68, 1, 99]), sum_of_squares(5))"
```
