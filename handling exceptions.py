# Exception handling
import sys

try:
    f = open('filename.txt') # let's say we want to open a file

except FileNotFoundError as e: # if the file doesnt exist raise the exception. we can also use custom error message
    print (e)

except Exception as e: # a vague exception which is often used in the end after specific/relevant exceptions have been defined
    print(e)

else: # executes when try no exceptions are raised
    print(f.read())
    f.close

finally: # executes regardless of try, except output
    print('opening file')
