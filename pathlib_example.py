import pathlib

p = pathlib.Path("")

txt_files = p.glob("*.txt")
print("*.txt: ", list(txt_files)) 

#should list all the txt files in the folders leading up to the cwd but it doesnt.
print("**/*.txt: ", list(p.glob("**/*.txt")))
# should print all t he txt files one level down form the cwd.
print("*/*.txt: ", list(p.glob("*/*.txt")))

# get all the hidden files that start with a dot. dot files

p2 = pathlib.Path.home()

print(list(p.glob(".*")))