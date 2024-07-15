from fastapi import FastAPI
from engine.database import Base, engine
from router import profile_router

app = FastAPI()

Base.metadata.create_all(bind=engine)
app.include_router(profile_router.router)
