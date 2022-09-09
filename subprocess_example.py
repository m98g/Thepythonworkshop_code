import subprocess

#example does only work on linux with the ln instead of dir arguemnt. Here 
# it does only produce an error.

result = subprocess.run(["dir"], capture_output=True)
print("stdout", result.stdout)
print("stderr", result.stderr)