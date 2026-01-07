# variable and datatypes:

# str , it , float , boolean , complex ,
#  tupels , list , sets , range
# bytes , bytessarray
# dictinory

# type() - return the data type of the variable

# casting int, float ,str

my_string = 'Hello world'

my_string[1]  #access

for x in my_string:
    print(x)

if 'H' in my_string:
    print(True)

if "w" not in my_string:
    print(False)

# Slicing a string:

print(my_string[0:3])  #from 0 to 3 exclusive

# methods
# upper, lower, stripe, replace , split
# concat ,+
# formated string useing f

# age = 36
# #This will produce an error:
# txt = "My name is John, I am " + age   #through as a Error
# print(txt)
# escaping charaters \

# Boolean:

# The falsy values are , FALSE, NONE, 0 , "", () , {} , []

# OPERATIONS

# lIST - ORDER - CHANGABLE - ALLOW DUPLICATES - []

mylist = ["apple", "banana", "cherry"]

# len(mylist)
# slice(mylist[2:4])
# check if "applie " in list
# change the itesm mylitst[2]='32'
# insert menthod to insert the value in the speicif index.
# add append(), insert(), extend()
# delete pop() clear() emty the list
# for loops , while , range() , len()

# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#   print(thislist[i])

# Comperhension of loops [x*2 for x in range(len(my_list))]

# sort method - ascending sort(reverse=true) -- decending

# tuple - unchangable () Tuple items are ordered, unchangeable, and allow duplicate values.

# fruits = ("apple", "banana", "cherry")

# (green, yellow, red) = fruits  unpack a tuple

# A set is a collection which is unordered, unchangeable*, and unindexed.

# Though the sets are onuindexed we need to loop to access the sets
# add() , update() - concat another sets
# remove('bananan) , pop(), clear(), del

# joins - use join , update for join 2 sets
# intersection - allow only duplicates
# difference -keep only the item from first sets not include in second stes
# symmentric_difference() - keep all items except the duplicates

set1 = {"1", '2', 3}
set2 = {3, 2, 1}
# print(set1 | set2)  {'1', 1, 2, 3, '2'} join without duplicates
# print(set1.intersection(set2)) {3}
# print(set1.difference(set2)) {1,2}
# print(set1.symmetric_difference(set2)) {1, 2, '2', '1'}

# Unlike sets, elements cannot be added or removed from a frozenset.
# x = frozenset({"apple", "banana", "cherry"})
# print(x)
# print(type(x))

# dict - {key:value};
# access obj.key obj['key'] , obj.keys() , obj.values() , obj.items()
# obj['key'] =12
# obj.update({'year':22})
# remove ---> pop() , clear() , popitems()
# copy()

# conditional statement

# if else match elif/ continue, break - contine skip and break breakit

# function def name(prams): return pass , keyword args and args
# Any argument before the / , are positional-only, and any argument after the *, are keyword-only.

# def my_function(a, b, /, *, c, d):
#   print(a + b + c + d)

# my_function(5, 6, c = 7, d = 8)

# def changecase(func):
#   def myinner():
#     return func().upper()
#   return myinner

# @changecase
# def myfunction():
#   return "Hello Sally"

# print(myfunction())

# in decorators the python if we ask fro a name with dundor__name__ it returns the wraper functin we use
# funtools.wraps
# lambda arguments : expression

# oops - class , inheritance , static methods ,

# mystr = "banana"    //iterable object
# myit = iter(mystr)   //making it iternation

# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().

# scope accessing globle scope anywhere to modify we need globals
# local scope or bounded to the local functions
# access the nested pareent valiable , to modify use the nonlocal
