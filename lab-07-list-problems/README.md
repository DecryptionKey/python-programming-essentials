# Lab 7: List Problems

Seven list algorithm problems. Each file runs its own examples, no input needed.

| File | Problem |
|------|---------|
| `problem_01_less_than.py` | Return the numbers less than `k` |
| `problem_02_average.py` | Floor of the mean |
| `problem_03_separate_even_odd.py` | Sorted evens first, then sorted odds, in place |
| `problem_04_second_largest.py` | Distinct second largest, or -1 |
| `problem_05_third_largest.py` | Third largest, or -1 if fewer than three elements |
| `problem_06_maximum_triplet_product.py` | Largest product of any three elements (handles negatives) |
| `problem_07_move_zeroes.py` | Move zeroes to the end in place, keeping order |

```bash
for f in *.py; do python3 "$f"; done
```

## What I learned

Single-pass solutions, in-place list changes without extra lists, and why two large negatives can beat the three largest positives in a product.
