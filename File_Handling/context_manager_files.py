# Context managers
# Allows us to manage using and closing of the resources
# with key word is used

with open('hello.txt','r') as f:
    print(f.readlines())

print(f)

# Its an effective way of using files
# No need to close file 
# try except classes are not required


