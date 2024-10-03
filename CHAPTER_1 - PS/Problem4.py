import os

# Get the current working directory
current_directory = os.getcwd()

# List the contents of the directory
directory_contents = os.listdir('f:/python/')

# Print the contents
print(f"Contents of the directory '{current_directory}':")
for item in directory_contents:
    print(item)
