# Generator python:

# Generating a things a stream of data 
# save the meeory and we dont need the data immediately like a lazy executions

def get_generator():
    yield 'Functions1'
    yield 'Functions2'

value  = get_generator()
print(next(value))
print(next(value))