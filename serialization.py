from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pin: str
 
class Patient(BaseModel):
    name: str
    gender: str
    age: int
    address:Address

address_dict={'city':'Ludhiana','state':'Punjab','pin':'415624'}
address1 = Address(**address_dict)

patient_dict = {'name':'manav','gender':'male','age':'22','address':address1}

patient1 = Patient(**patient_dict)

temp = patient1.model_dump_json()
print(temp)
print(type(temp))