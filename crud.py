from sqlalchemy.orm import Session
from datetime import datetime, timedelta
import models

def save_cycle(db: Session, start_date, cycle_type, period_duration):
    #a fn that uses activated sessio to apply queries...
    cycle = models.Cycle(
        start_date=start_date,
        cycle_type=cycle_type,
        period_duration=period_duration
    )
    db.add(cycle)  #insertion
    db.commit()    #saving
    db.refresh(cycle)  #syncing db with python
    return cycle

def save_prediction(db: Session, cycle_id: int, start_date: datetime.date, cycle_length: int, period_duration: int):
    # real prediction calculations based on cycle info
    predicted_start_date = start_date + timedelta(days=cycle_length)
    ovulation_date = start_date + timedelta(days=cycle_length // 2)
    luteal_phase_start = ovulation_date + timedelta(days=1)
    luteal_phase_end = predicted_start_date - timedelta(days=1)
    period_start = start_date
    period_end = start_date + timedelta(days=period_duration - 1)

    # determine current phase based on today's date, example logic:
    today = datetime.utcnow().date()
    if period_start <= today <= period_end:
        current_phase = "Period"
    elif luteal_phase_start <= today <= luteal_phase_end:
        current_phase = "Luteal"
    elif ovulation_date == today:
        current_phase = "Ovulation"
    else:
        current_phase = "Follicular"

    prediction = models.Prediction(
        cycle_id=cycle_id,
        predicted_start_date=predicted_start_date,
        ovulation_date=ovulation_date,
        luteal_phase_start=luteal_phase_start,
        luteal_phase_end=luteal_phase_end,
        period_start=period_start,
        period_end=period_end,
        current_phase=current_phase
    )
    db.add(prediction)  #insertion
    db.commit()         #saving
    db.refresh(prediction)  #sync
    return prediction

def get_prediction_by_id(db: Session, prediction_id: int):
    return db.query(models.Prediction).filter(models.Prediction.id == prediction_id).first()
