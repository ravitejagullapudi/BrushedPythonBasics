# Files
# Open files
# Perform Read/Write operations
# Close the file

fhandle = open('hello.txt', 'r')

# Files are stored in secondary memory
# handle = open(filename,mode) modes- read,write,append...
# this file handle of open can be treated as a sequence of strings where
# each line in the file is a string in sequence(ordered set)

# Default is read mode and when opened it returns _io.TextIOWrapper object
# which is The handle is a connection to the file's data
print(fhandle, f'type of file is {type(fhandle)}')

'''
Reading file
'''

# To read first 7 characters
print(fhandle.read(7))


# To read the current file pointer location
print(fhandle.tell())

# to read a single line 
print(fhandle.readline())

# We can see that line has missing first 7 chars 
# It means if we read the data the once and if we read again
# it directly starts from the next character after previous read
# It's because the file pointer will shift to that char


# To read the current file pointer location
print(fhandle.tell())

# To move the file pointer from current location 
# to some where or to start we use seek() method

# Parameters:
# 1st param is offset and 2nd one is whence
# Whence param has 3 values and default is 0
# 0 -> seek_absolute: Seeks to an offset from the beginning of the file.
# 1 -> seek_relative: Seeks to an offset from the current
# position of the file pointer
# 2 -> seek_end: Seeks to an offset from the end of the stream.
fhandle.seek(0)
print(fhandle.tell())
for i in fhandle:
    # File lines have already an endline character
    print(i, end='')

fhandle.seek(0)
print(fhandle.readlines())

# if we called again already file pointer alreached end so nothing will be

print(fhandle.readlines())



''' Writing into files '''

# It will creates a file if not exists
# If file exists, it overrides the content
fhandle = open("file_write_examp.txt",'w')

fhandle.write("Line 1 in demo write file\n")
fhandle.write("Line 2 in demo write file\n")
fhandle.write("Line 3 in demo write file\n")
fhandle.write("Line 4 in demo write file\n")
fhandle.write("Line 5 in demo write file\n")
fhandle.write("Line 6 in demo write file\n")
fhandle.write("Line 7 in demo write file\n")
fhandle.write("Line 8 in demo write file\n")


# Every time after opening file it should be closed
# It is required to free up the resource
# Even though there is some garbage collector in python
# but it will perform its operation in some interval
# based on platform
fhandle.close()





# Opening file which does not exist in read mode
# Then it will raise as an File not found error
# We need to make sure that to handle this by exceptions
error_occured = False
try:
    # Instructions that may raise error
    f = open("hello1.txt", 'r')

except Exception as e:
    # Catch error
    error_occured = True
    print(type(e))
finally:
    if not error_occured:
        f.close()


