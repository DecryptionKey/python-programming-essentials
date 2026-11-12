# Lab 2: Exception Handling

Ten programs that each trigger and handle a specific built-in exception.

| File | Exception | Interactive |
|------|-----------|-------------|
| `problem_01.py` | `ZeroDivisionError` | Yes, enter a number and 0 |
| `problem_02.py` | `ValueError` on non-integer input | Yes |
| `problem_03.py` | `FileNotFoundError` | No |
| `problem_04.py` | `TypeError` on non-numeric input | Yes |
| `problem_05.py` | `PermissionError` | No (see note) |
| `problem_06.py` | `IndexError` | Yes |
| `problem_07.py` | `KeyboardInterrupt` | Yes, press Ctrl+C at the prompt |
| `problem_08.py` | `ArithmeticError` | Yes |
| `problem_09.py` | `UnicodeDecodeError` (UTF-16BE vs UTF-8 test files) | No |
| `problem_10.py` | `AttributeError` | No |

**Note:** `problem_05.py` needs `permission_test.txt` to be unreadable to show the error. Git doesn't keep that, so run `chmod 000 permission_test.txt` first (and `chmod 644` afterward).

Run from this folder so the test files are found:

```bash
cd lab-02-exception-handling
python3 problem_09.py
```

## What I learned

Catching the specific exception (not a bare `except`) and giving the user a useful message instead of a traceback.
