from sqlalchemy.orm import Session
from sqlalchemy import Table, MetaData

def truncate_all(db: Session, meta: MetaData) -> None:
    for table in reversed(meta.sorted_tables):
        table: Table
        db.execute(table.delete())