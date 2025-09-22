import arrow


sugar_value =2 
print(f"Initial sugar :{sugar_value}");
print(f"Initial sugar :{id(sugar_value)}"); #store in refernce
sugar_value = 18
print(f"Initial sugar :{id(sugar_value)}"); # store in another refernce means the value not changed only reference

# mutable object the value can be changed like objects 
# immuntable object the valye is not changeble their referenc change;

#numbers :
# inte numbers - itergers
black_grams = 14
ginger = 3
totoal_grams = 14+3;
print(f"{totoal_grams}")
#  + , - , / , % , *  , **
#  //  return only the whole numbers;

# Boolean - true and false:
# true - 1 and false 0 casting;   Help full in Logical Operations and , or , not;

# string ;

new_string = 'mystring';
print(f"{new_string[(len(new_string) - 1)]}") #last number
new_string[0:8] # slice the string
new_string[0:8:2] # slice the string from 0 to 8 and take every 2 char
new_string[8:] # from 8 index to everything.
new_string[::-1] # reverse the string;

# when we have the speical characters like non english words we need to encode and decode the string to get the 
# result 

encode = "harià" #consider the encode varibale has a special char
after_encode = encode.encode("utf-8"); #conver other variable to utf encoded
afetr_decode = after_encode.decode("utf-8") # convert back to actual string
print(after_encode)

# string indexing , slicing, encodeing core features.

#Tuples and Membership Testing .

my_tuples = ('hello', 'bye', 'masala') #immutable 

#destructiong :
(speice1, speice2, speice3) = my_tuples

print(my_tuples[1])  # access

# in -- keyword helps whethere the value includes in the tuples or not.


#muttable datattypes :

#List (array) -- order , changable , allow dublicates,

my_list = [1,2,3,3,4,10]  # order , changeable , allow dublicates.
# append - add , pop - remove , extend , insert -(add at a sepcific index), reverse() the result , max , min 


#operator Overloading and bytearray in python ;
# operator doing coming extra then what we think for example using + in concat two 2 arrays;


# bytearray -> takes every byte of the char and return a new array example:

mybyte_array = bytearray(b"hari"); # hari 
print(mybyte_array.replace(b"h",b"k")); #kari changed to beacuse it uses byte array


# set  ---> order , changable , dont allow dublicates;

# | - or pipe know as the union pipe means that the concat two  {};
#  & - return the intersection means the common array value;
# -  -- return the only in one {} not in another {};
# in  -- check whether in the {};


# Dictonary  - key value pair ;

person = {
    "name":'Hari',
    "lastName" : 'Prasath',
    "age":'24',
}
print(person.pop("age"))
print(person)

# obj.keys - returns the keyes and obj.values is return all values
# obj.get('key', 'default value if not present');


# Advance for DataTypes in Python like collections;


my = arrow.utcnow();
print(my)