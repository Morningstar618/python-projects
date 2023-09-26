try:
    file = open("/home/j4297/code/python/angela/testdir/try-except/a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("/home/j4297/code/python/angela/testdir/try-except/a_file.txt", "w")
    file.write("something")
except KeyError as error_message:
    print("The key {} does not exist".format(error_message))
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("file was closed")
    raise TypeError("This is an error that I made up")


