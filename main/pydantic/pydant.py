# a statci type for python code a development 
#  A schema Validation setting mangements: init , type , config files for setting mangements.
# Data parsing and validation , api development , config management, Data serlization/deserilization

from pydantic import BaseModel, Field , field_validator , model_validator , computed_field , ConfigDict

class User(BaseModel):
    id:int
    name:str
    is_active:bool

data = {"id":1,"name":'s',"is_active":True}

OBJ = User(**data)

# print(OBJ)

# Advance typing & datatype in python , int , str , bool 
from typing import List , Dict , Optional

# combaining the typing with pydantic
class cart(BaseModel):
    user_id : int
    items : List[str]
    quanity : Dict [str , int]
    image :Optional[str] = None
# option field


class Employee(BaseModel):
    id:int
    name:str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Employee Name",
        examples="Hitesh Choudhary"
    )
    salary:float = Field(
        ..., #required
        ge = 10000 #gether than
    )

# ge , gt , le , lt - geterthan equal, lessthan equal

empolyeeObj = Employee(id =1 , name='hari', salary=10000) #Input should be greater than or equal to 10000
print(empolyeeObj)

# Filed validation vs Model Validations
# from pydantic import BaseModel, Field

# filed validator - is basically validate a filed in runtime

class Valuedator(BaseModel):
   username:str

   @field_validator("username")
   def validate_username(cls,v): #while adding the data to the field
            if(len(v) < 5):
                raise ValueError('Minimum Length should be 5')
            return v
   
   @model_validator(mode='after')  #execute the after the data added
   def model_val(cls, values):
        if(values.username != 'prasath'):
             raise ValueError('Errrr Matching')

user = Valuedator(username='prasath')
print(user)


# computed Property in pydantic
# do computational work in the pydantic itself

class computed(BaseModel):
     price:float
     quantity: int

     @computed_field
     @property            # for doing the computation work in pydantic itself
     def total_price(self)->float:
           return self.price * self.quantity

my_compute = computed(price=12.00, quantity=12);

print(my_compute.total_price) #access it like a property.

# serilization
print(my_compute.model_dump())   #{'price': 12.0, 'quantity': 12, 'total_price': 144.0} add the compute and to obj instance

# Advance Validators:

# from pydantic import BaseModel, Field , field_validator , model_validator , computed_field

# BaseModel  - alwasy the satrting pint of clreating a types
# Field - add the addition checks like required max , min ,gt
# field_Validator - validate the filed if the entry is incorrect throw a custom error
# model_validor - have before and after access to the proerty before and after for type data checks
# computed_filed - doing a computed work in the class
#  model.dump() - serlization version of the dump
# typing - combaining the typing with baseModel List(str), Optionals


# Nested Models in Pydantic:
# Nested models allows the complex model structue one inside one

# user model inside address

class Address(BaseModel):
     street:str
     pincode:int

class User (BaseModel):
     id:int
     name:str
     address:Address
 


user = {
     "id":1,
     "name":'Hari',
     "address":{
          "street":'Hello street',
          "pincode":323234
     }
}

user = User(**user)
print(user)

# self refereenceing model in pydantic , recursive model in python
# Like Command refers to the reply of the commands.

class Comment(BaseModel):
     id:int
     content:str
     replies:Optional[List['Comment']] = None


# once create a self referencing model create use .model_rebuid();

Comment.model_rebuild()

my_comment = Comment(
     id=1,
     content='About the streams',
     replies=[
          Comment(id=3,content='About the nn'),
          Comment(id=3,content='About the nn'),
          Comment(id=3,content='About the nn'),
     ]
)


print(my_comment)

# Advance nested Models in Pydantic: Deeply nested structure

# country --> state --> city --> Address --> Oragnization.

# Best Practise of Pydantic Examples:
# Define the leaf model first
# build upward
# use clear naming
# lazy Loading

# Model dump and Model dump json in serlizations


