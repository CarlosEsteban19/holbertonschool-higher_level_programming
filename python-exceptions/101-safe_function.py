#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        result = fct(*args)
    except (ZeroDivisionError, IndexError, ValueError, TypeError) as e:
        print("Exception:", e, file=sys.stderr)
        return None
    return result
