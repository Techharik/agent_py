# for token in range(1,11):
#     print(token)

order_names={
    "1":'hari',
    "2":'sabari',
    "3":'prasath',
}
order_list = ['hitesh', 'aman','becky']

for order in order_names:
    print(order_names[order])

for list in order_list:
    print(list)

# enumerate basically the return the tuples of array:
for idx,item in enumerate(order_list , start=1):
    print(f"the list {idx}, {item}")

# zip - combine 2 list and for looping and return the tuples 

names = ['hari', 'prasath']
bills = [120, 321]

for name, amt in zip(names , bills):
    print(f"{name} --- {amt}")

# while loop in python 

start = 40;

while start <= 100:
    print(f'Increased the temperature to 15 {start}')
    start +=15


# break , continue  --- break the lopp and continue leave that process.


stocks = [1,2,3,4,3,4,34]

for num in stocks:
    if num == 2:
        continue
    if num == 4:
        break
    print(num)

# warlus operator := ; in if class we need to store the value and do the expression we can use it

# if(variable := value /12)  -- here it not using comparision oferato we use walru it do the tasks and store in varibale


# Dictionary in place in Match case:
customers = [
     { "id":1 , "total" :100, "coupon":"p20"},
     { "id":2 , "total" :200 ,"coupon":"p50"},
     { "id":3 , "total" :200 ,"coupon":'null'}
 ]

discounts ={
    "p20":20,
    "p50":50,
}
applied_cust = {

}
for cust in customers:
    if cust["coupon"] in discounts:
        cust["total"] -= discounts[cust["coupon"]]
        applied_cust[cust["id"]] = cust["total"]
    else:
        applied_cust[cust["id"]] = 0

print(applied_cust)