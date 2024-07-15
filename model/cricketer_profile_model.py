from pydantic import BaseModel


class ProfileModel(BaseModel):
    name: str
    country: str
    age: str


class ProfileResponse(BaseModel):
    id: int
    name: str
    country: str
    age: str

    class Config:
        orm_mode = True
