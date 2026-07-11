from pydantic import BaseModel, EmailStr, Field
from typing import Optional
import json

# enforces output data type
class Student(BaseModel):
    name:str = 'nome'
    age:Optional[int] = 69 # or use None
    email: EmailStr
    cgpa: float = Field(gt=0,lt=10,description='Decimal value reepping the CGPA of Student') 


new_student ={'age':'34', # coercing to int by pydantic,
              'cgpa':5,# coercing to float by pydantic,
              'email':"abc@na98beel.com"} 
# = {'name':"nabeel"}

stud = Student(**new_student)
dic_stud = dict(stud)
json_stud = stud.model_dump_json()
data = json.loads(json_stud)

print(stud)
print(dic_stud['cgpa'])
print(data["cgpa"])# print(stud.name) #nome