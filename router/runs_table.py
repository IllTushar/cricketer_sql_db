from sqlalchemy.exc import SQLAlchemyError

from table.tables import RunTable, UserProfile
from fastapi import APIRouter, Depends, status, HTTPException
from engine.database import SessionLocal
from sqlalchemy.orm import Session
from typing import Annotated, List
from model.cricketer_runs import CreateRuns, RunWithName

router = APIRouter()


def connection_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_Session = Annotated[Session, Depends(connection_db)]


@router.post("/create-runs/{player_id}", status_code=status.HTTP_201_CREATED)
def create_user(player_id: int, request: CreateRuns, db: db_Session):
    player = db.query(UserProfile).filter(UserProfile.id == player_id).first()
    if not player:
        raise HTTPException(status_code=404, detail="Player is not found!!")
    else:
        try:
            create_runs = RunTable(user_id=player_id, **request.dict())
            db.add(create_runs)
            db.commit()
            db.refresh(create_runs)
            return create_runs

        except SQLAlchemyError:
            db.rollback()
            raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/player-runs/{player_id}", response_model=List[RunWithName], status_code=status.HTTP_200_OK)
def get_player_with_runs(player_id: int, db: db_Session):
    player = db.query(RunTable).filter(RunTable.user_id == player_id).first()
    if not player:
        raise HTTPException(status_code=404, detail="Player is not found!!")
    else:
        player_list: List[RunWithName] = []
        player_data = db.query(UserProfile).filter(UserProfile.id == player_id).first()
        if not player_data:
            raise HTTPException(status_code=404, detail="Data not found!!")

        player_list.append(RunWithName(name=player_data.name, ODI=player.ODI, T20=player.T20, Test=player.Test))
        return player_list
