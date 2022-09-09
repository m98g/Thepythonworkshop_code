import sys
import functools

print_stderr = functools.partial(print, file=sys.stderr)

print_stderr("MAIN")