# Generator python:

# Generating a things a stream of data 
# save the meeory and we dont need the data immediately like a lazy executions

def get_generator():
    yield 'Functions1'
    yield 'Functions2'

value  = get_generator()
print(next(value))
print(next(value))

# infinte Generators in python 
# Helps in streams when we need a constant access the data realtime updates

def infinite_chai():
    count =1
    while True:
        yield f"refil {count}"
        count+=1

refill = infinite_chai()

for _ in range(3):
    print(next(refill))

# Send Value to the generators
def chai_customer():
    print("Welcone what chai would you like !")
    order = yield
    while True:
        print(f'We are Preparing: {order}' )
        order = yield

stall = chai_customer()
next(stall)
stall.send("Masala")
stall.send("COLD")
stall.send("Ginger")