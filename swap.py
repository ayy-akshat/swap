def swapFiles(file1, file2):
    f1 = open(file1, "r")
    f2 = open(file2, "r")
    f1c = f1.read()
    f2c = f2.read()
    f1w = open(file1, "w")
    f2w = open(file2, "w")
    f1w.write(f2c)
    f2w.write(f1c)
swapFiles("example1.txt", "example2.txt")