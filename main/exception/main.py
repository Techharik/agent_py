# Execptional Handling in Pythons.

# index error -out index in list
# key error - in dict
# zero division error - 0 division
# type error - tring mixed with error
# name error - some naming rules missed.

try:
    # do somethin
    leter =['d']
except ValueError as e:
    print('Error'+e.message)
finally:
    print('done')


# The try block lets you test a block of code for errors.

# The except block lets you handle the error.

# The else block lets you execute code when there is no error.

# The finally block lets you execute code, regardless of the result of the try- and except blocks

# Multiple exception in Python:

# raise -- throw or own Errors in the programs

def my_functions():
    try:
        print('hhhh')
        raise ValueError('my own error') #my won Error
    except ValueError:
        print(ValueError)
    except KeyError:
        print(KeyError)
    else:
        print('Everything is fine')
    finally:
        print('All done')
    

