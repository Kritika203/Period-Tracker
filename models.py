from sqlalchemy import Column, Integer, Date, String, DateTime, ForeignKey
from database import Base  # Base=declarative_base()...each class will be a table,and attributes = column
from datetime import datetime

class Cycle(Base):
    __tablename__ = "cycles"

    id = Column(Integer, primary_key=True, index=True)  # id-pk-autoincrement by default..index=true for faster lookups
    start_date = Column(Date, nullable=False)
    cycle_type = Column(String(10), nullable=False) 
    period_duration = Column(Integer, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    cycle_id = Column(Integer, ForeignKey("cycles.id"), nullable=False)
    predicted_start_date = Column(Date, nullable=False)
    ovulation_date = Column(Date, nullable=False)
    luteal_phase_start = Column(Date, nullable=False)
    luteal_phase_end = Column(Date, nullable=False)
    period_start = Column(Date, nullable=False)
    period_end = Column(Date, nullable=False)
    current_phase = Column(String(50), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
