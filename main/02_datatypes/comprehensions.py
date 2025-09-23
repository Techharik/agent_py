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