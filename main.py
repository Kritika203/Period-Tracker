from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import schemas, crud, models
from database import engine, SessionLocal, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins for now
    allow_methods=["*"],
    allow_headers=["*"],
)

#This is a generator function FastAPI uses to give each request its own DB session, and close it properly when done
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def cycle_type_to_length(cycle_type: str) -> int:
    # convert input like short/normal/long to fixed numbers
    ct = cycle_type.lower().strip()
    if ct == "short":
        return 24
    elif ct == "normal":
        return 28
    elif ct == "long":
        return 36
    else:
        return None

@app.post("/submit", response_model=schemas.PredictionOut)
def submit_cycle(data: schemas.CycleCreate, db: Session = Depends(get_db)):
    cycle_length = cycle_type_to_length(data.cycle_type)
    if not cycle_length:
        raise HTTPException(status_code=400, detail="Invalid cycle_type, use short/normal/long")

    # save cycle info, then save prediction based on it
    saved_cycle = crud.save_cycle(db, data.start_date, data.cycle_type, data.period_duration)

    prediction = crud.save_prediction(db, saved_cycle.id, saved_cycle.start_date, cycle_length, saved_cycle.period_duration)
    return prediction

@app.get("/prediction/{prediction_id}", response_model=schemas.PredictionOut)
def get_prediction(prediction_id: int, db: Session = Depends(get_db)):
    prediction = crud.get_prediction_by_id(db, prediction_id)
    if not prediction:
        raise HTTPException(status_code=404, detail="Prediction not found")
    return prediction

@app.get("/")
def welcome():
    return {"message": "Welcome to the PeriodTracker API :P"}
