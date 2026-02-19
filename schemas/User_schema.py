from pydantic import BaseModel

class UserSchema(BaseModel):
    email:str
    password:str

class UserUpdateAPI_KEY(BaseModel):
    API_KEY:str
    