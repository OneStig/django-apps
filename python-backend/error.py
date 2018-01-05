try:
    f = open('file.txt', 'w'
    f.write("Test write")
except IOError:
    print("error")
else:
    print("Successfully wrote to file")
    f.close()
