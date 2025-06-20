from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List ,Dict,Optional,Annotated
class Patient(BaseModel):
    name :Annotated[str , Field(max_length =50,title ='Name of patient',description='name of patient must be less than 50 chars',examples=['bittu','sukha'])]
    email: EmailStr
    linkdin_url: AnyUrl
    age: int
    weight : Annotated[float , Field(gt=0,lt=120,strict = True)]
    allergies : Annotated[Optional[List[str]] , Field(default = None,max_length = 5)]
    married : Annotated[bool , Field(default =None,description='is patient married or not')]
    contact_details: Dict[str,str]

def Insert_Patient_detail(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('inserted')

def Update_Patient_detail(patient: Patient):
    print(patient.name)
    print(patient.allergies)
    print(patient.married)
    print(patient.age)
    print('updated')

Patient_info = {'name':'Manav','age':22,'email':'bassi@gmail.com','weight': 56, 'allergies': ['Dust'],'married':False,'linkdin_url':'http://linkdin.com','contact_details':{'phone':'456786189'}}

patient1 = Patient(**Patient_info)

Insert_Patient_detail(patient1)
Update_Patient_detail(patient1)