# Labs 3 and 4: Console Programs

| File | Problem | Interactive |
|------|---------|-------------|
| `problem_29.py` | P-1.29: print every arrangement of the letters c, a, t, d, o, g (720 strings) | No |
| `problem_30.py` | P-1.30: count how many times a number can be halved before it drops below 2 | Yes |
| `problem_31.py` | P-1.31: make change in bills and coins for an amount charged and an amount given | Yes |
| `problem_32.py` | P-1.32: a line-by-line console calculator (number, operator, number, `=`) | Yes |

```bash
python3 problem_31.py
```

## What I learned

- Building permutations iteratively by inserting each letter into every position
- Working in cents so `0.1 + 0.2` style float errors don't break the change math
- Keeping state across inputs for the calculator
