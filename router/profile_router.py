from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from engine.database import SessionLocal
from table.tables import UserProfile
from model.cricketer_profile_model import ProfileModel, ProfileResponse
from typing import Annotated, List

router = APIRouter()


def connection_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_Session = Annotated[Session, Depends(connection_db)]


@router.post("/create-profile", status_code=status.HTTP_201_CREATED)
def create_user_profile(request: ProfileModel, db: db_Session):
    try:
        create_user = UserProfile(**request.dict())
        db.add(create_user)
        db.commit()
        db.refresh(create_user)
        return create_user
    except:
        raise HTTPException(status_code=402, detail="Not Created!!")


@router.get("/get_all-players", response_model=List[ProfileResponse], status_code=status.HTTP_200_OK)
def get_all_user(db: db_Session):
    users = db.query(UserProfile).all()
    if not users:
        raise HTTPException(status_code=404, detail="Not Found!!")
    return users


@router.get("/get-specific-player/{player_id}", status_code=status.HTTP_200_OK)
def specific_player(player_id: int, db: db_Session):
    data = db.query(UserProfile).filter(UserProfile.id == player_id).first()
    if not data:
        raise HTTPException(status_code=404, detail="Not Found!!")
    else:
        return {"data": data}


