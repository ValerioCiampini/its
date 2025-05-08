PATH:str = "Python/Lezione_15/file_example.txt"
mode:str = "w"
encoding:str = "utf-8"

file = open(PATH, mode)

print(file)

output:str = file.write("SSSSSSSS")
print(output)