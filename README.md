# Python Programming Essentials

Coursework from **CYBR108: Programming Essentials for Cybersecurity** (University at Albany, Fall 2026). This is intro-level work from my first Python course: functions, exception handling, loops, string and number manipulation, lists, and basic classes. Several problems come from *Data Structures and Algorithms in Python* (Goodrich, Tamassia, Goldwasser).

## Contents

| Folder | Topic | Problems |
|--------|-------|----------|
| [lab-01-python-basics](lab-01-python-basics) | Functions, modulo, bitwise operators, loops | R-1.1 to R-1.4 |
| [lab-02-exception-handling](lab-02-exception-handling) | `try`/`except` for common built-in exceptions | 10 problems |
| [lab-03-04-console-programs](lab-03-04-console-programs) | Permutations, loops, making change, a console calculator | P-1.29 to P-1.32 |
| [lab-05-number-exercises](lab-05-number-exercises) | Digit manipulation, palindromes, factorial, Collatz | Exercises 14 to 18 |
| [lab-07-list-problems](lab-07-list-problems) | List algorithms | 7 problems |
| [midterm](midterm) | Functions, permutations, classes, input type checks | 4 problems |

## Running

Python 3.9 or newer, standard library only.

```bash
cd lab-07-list-problems
python3 problem_02_average.py
```

Programs that read input prompt for it in the terminal. Each folder's README says which ones are interactive.

## What I learned

- Validating input and handling exceptions instead of letting a program crash
- Breaking a problem into small functions and testing edge cases (negative numbers, zero, empty input)
- Avoiding floating-point errors with money by working in cents
- Basic classes: constructors, accessors, and type checks on method arguments

## License

[MIT](LICENSE)
