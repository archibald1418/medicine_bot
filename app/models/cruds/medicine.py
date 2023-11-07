from typing import Optional, List
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from app.models import Medicine


def get_medicine_by_name(name: str, db: Session) -> None:
    
    search: str = "%{}" # start of name can overlap
    
    try:
        medicine: List[Medicine] = (
            db.query(Medicine)
            .filter(Medicine.name.like(search)
            .all()
            )
        )
    except NoResultFound:
        print("No medicine {name} found")
        return []
    return medicine 


def add_medicine(name: str, db: Session) -> Medicine:
    # with db:
    medicine: Medicine = Medicine(name=name)
    # print(id(user))
    # NOTE: all writes are queued into the session and executed later altogher (=unit of work)
    db.add(medicine)
    # db.commit()
    return medicine
    
