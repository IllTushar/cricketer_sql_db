from pydantic import BaseModel


class CreateRuns(BaseModel):
    ODI: int
    T20: int
    Test: int


class RunResponse(BaseModel):
    id: int
    user_id: int
    ODI: int
    T20: int
    Test: int

    class Config:
        orm_mode = True


class RunWithName(BaseModel):
    name: str
    ODI: int
    T20: int
    Test: int


class ODIRuns(BaseModel):
    name: str
    ODI: int
