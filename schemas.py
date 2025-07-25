from pydantic import BaseModel
from datetime import date

# schema-structure for data
# skeletal structure representing logical view of the db
# What data types are allowed-What fields are required-How data flows between frontend - backend - database
# it's the file where we define Pydantic models, which = data schemas
# pydantic - data validation and parsing library used in FastAPI
# BaseModel is the base class from Pydantic and inheriting it enforces  types, auto-validation, and parsing of data

class CycleCreate(BaseModel):  # input data for cycle
    start_date: date
    cycle_type: str        
    period_duration: int

class PredictionOut(BaseModel):  # output format for predicted stuffs

    predicted_start_date: date
    ovulation_date: date
    luteal_phase_start: date
    luteal_phase_end: date
    period_start: date
    period_end: date
    current_phase: str

    class Config:
        from_attributes = True  # Lets you convert SQLAlchemy model → Pydantic model Avoids errors
