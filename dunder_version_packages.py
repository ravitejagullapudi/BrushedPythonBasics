# Every .py file is a module 
import sys

# here we have imported module and one thing we
# need notice is that when we imported a module
# module is totally executed so it is not good one to
# place print statements in it.
import some_module
# As some_module.py has printed name dunder and we have imported
# here it means it is executing from another module
# in these cases the name dendogram prints module name

# Version of python
print(sys.version)

# dunder name it is in this module and this file is executed
# so it prints as main
print(__name__)

# so here this below line meant that if the current
# module is running then call main else if it is imported
# then dont execute the below one
if __name__ == '__main__':
    # main()
    pass

# to make a directory as package __init__.py should be there
# when ever we imported a package __init__.py module is executed always