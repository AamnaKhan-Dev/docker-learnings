# def adding_to_db(name, age):
#     if type(name) == str and type(age) == int:
#         print(name)
#         print(age)
#     else:
#         raise TypeError("Give right data type")
    
# # data_patient = {"name": "Aamna", "age": 30}
# data_patient = {"name": "Aamna", "age": [1,2,3,4]} #PROBLLEM! needs validation

# adding_to_db(**data_patient)

from pydantic import BaseModel, EmailStr, Field, AnyUrl, BeforeValidator, field_validator
from typing import List, Dict, Optional, Annotated

class contact_validate(BaseModel):
    phNo: str
    address: str
    email: EmailStr
    
    @field_validator('email')
    def email_validator(cls, input_email):
        if input_email:
            input_lower_case = input_email.lower()
            input_domain = input_email.split('@')[1]
            valid_domain = ["gmail.com", "nust.edu.pk", "yahoo.com"]
            if input_domain in valid_domain:
                return input_lower_case
            else:
                raise ValueError("Domain doesn't match")
            
    @field_validator('phNo')
    def normalize(cls, phone):
        phone.strip()
        
        #pythonic ways
        clean_number = "".join(filter(lambda X:X.isdigit(), phone))
        if clean_number.startswith("+92"):
            return clean_number
        elif clean_number.startswith("92"):
            return '+'+clean_number
        if clean_number.startswith('0'):
            return "+92" + clean_number[1:]
        
        #generator expression/comprehenion
        # return "".join(ch for ch in phone if ch.isdigit())
        
        # return "".join(filter(str.isdigit, phone))
        
        #!pythonic way
        # only_digits = []
        # for char in phone:
        #     if char.isdigit():
        #         only_digits.append(char) 
        # return "".join(only_digits)
            
class Valid_Patient(BaseModel):
    # name: Annotated[Optional[str], Field(max_length=50), BeforeValidator(lambda X:X.title())]
    name: str
    age: Optional[int] = Field(None, gt=10, lt=50, 
                               description="Give only integer value greater than 10", examples=[30, 45])
    allergies: List[str]
    contact_details: contact_validate
    # linkedIn: AnyUrl
    
    @field_validator('name')
    def case_setting(cls, n):
        return n.title().strip()
    
    
    
def adding_to_db(data: Valid_Patient):
    print(data.name)
    print(data.age)
    print(data.contact_details.email)
    print(data.allergies)
    print(data.contact_details)
    print(data.contact_details.phNo)
    # print(data.linkedIn)
    
# data_patient = {"name": "Aamna", "age": 30}
data_patient = {"name": "aamna khan", "age": 48, "linkedIn": "https://chatgpt.com/c/687d36ab-1844-8013-a752-d383e1bf36ee", "allergies": ["pollen", "dust"], "contact_details": {"phNo": "    0317581--3294", "address": "xyz, abc", "email": "xyz@gmail.com"}} 
validated_data = Valid_Patient(**data_patient)
adding_to_db(validated_data)
    
