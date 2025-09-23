# shotcut for single line code for loops if etc

# List comperhensions :

my_list = [1,2,3,4] #iterable items ;


validated_items = [x*2 for x in my_list if x > 2 ]

print(validated_items)

recipes = {
    "masala1": ['ginger', "cardoman"],
    "masala2": ['tea', "cardoman"],
    "masala3": ['ginger', "coffee"]
}

unqiue_sets = { lists for key in recipes  for lists in recipes[key] };


print(unqiue_sets)

# Dictionary comperhensions
pairs = {
    "one":1,
    "two":2,
    "three":3
}

paris_multiply = { pairs* 2 for k, pairs in pairs.items() }
print(paris_multiply)

# Generator Comphrehensions for memory Optimizations:

# Generator are used to care about the memory ;

# (expression for item in iterable if condition); generator object uses the streams to store the data;


