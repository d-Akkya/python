with open("old.txt") as f:
    content = f.read()

with open("rename_by_python.txt", "w") as f:
    f.write(content)

#Now delete the old.txt file by importing os/sh module