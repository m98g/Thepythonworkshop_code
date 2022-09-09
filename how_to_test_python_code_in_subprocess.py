import subprocess
import sys

# Is suppoesed to crash and retrun the "-11" value which stands for aborted process
# however i get 3221225725.
code = 'compile("1" + "+1" * 10 ** 6, "string", "exec")'

# the code has to be in parentheses because it has to be passed as a string to
# the subprocess and gets then run in it as python code.
# sys.executable is the python exe or interpreter used. "-c" is the option to run
# python code inline.
result = subprocess.run([
    sys.executable, 
    "-c", code
])

print(result.returncode)