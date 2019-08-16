# File handling using Python using try-catch block

try:
    file = open("C:\PythonFile.txt", "w")
    file.write("Hello World\n")
    file.write("This is our new text file\n") 
    file.write("This is another line.\n")
    file.close()
except:
    print("C:\PythonFile.txt not created successfuly")

try:
    print("Printing the content of file -> C:\PythonFile.txt\n")
    readfile = open("C:\PythonFile.txt", "r")
    print(readfile.read())
    readfile.close()
except:
    print("Unable to read the file -> C:\PythonFile.txt")
