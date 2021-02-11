# Open a file, read it and print its length, then close it
file = open("filename.txt", "r")

contents = file.read()

print(len(contents))

file.close()