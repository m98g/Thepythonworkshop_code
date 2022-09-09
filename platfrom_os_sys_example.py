import platform
import os
import sys

print("Process id: ", os.getpid())
print("Parent process id: ", os.getppid())

print("Machine network name: ", platform.node())
print("Python version: ", platform.python_version())
print("System: ", platform.system())

print("Python module loojup path: ", sys.path)
print("Command to run Python: ", sys.argv)

print("USERNAME environment variable:", os.environ["USERNAME"])