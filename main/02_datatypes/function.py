# # function in python

# def my_function():
#     print('This is my functions')

# my_function()

# fake_db={
   
# }
# count = 1
# def get_input():
#   value = input("Enter the user name\n")
#   return value

# def validate_value(value):
#    validate = type(value) == str
#    return validate 

# def db(value):
#    global fake_db
#    fake_db[count] = value; 
#    return fake_db

# def register_user():
#    global count
#    user = get_input()
#    print(user)
#    validated_value = validate_value(user)
#    print(validated_value)
#    if validated_value:
#       dbs = db(user)
#       print(dbs)
#       count +=1
#       return dbs
#    else:
#       return False

# register_user()

# # scopes and name resolution 


def update():
    bucker = 'hari'
    def another_update():
        bunker =bucker+ 'j'
        print(bunker)
    another_update()

update()

# non local - function inside functionw we need to update the varibale
#  global variable we need to update we need to use globals varibale
#  access variable we can use without the keyword itself


# aruguments 
# keyword arguments and normal one.
# argue *ingredients -no name comes herer , **kewywoard -- keyword arug comes here
# default value can be provide.
# Handle multiple return in python.
# pass - None will we return
# return multiple value ,,,
# Types of fucntion pure return somthing not affect outer world vs impure functions --- side effects no return, recursive function a function call itself.
# lamda function - anonimous 
# lamda chai:chai =="kadak "