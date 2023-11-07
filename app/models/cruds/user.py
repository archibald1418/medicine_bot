from .. import User, Medicine, Recipe
from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.sql.expression import text
from utils.decorators import session_is_active

# TODO: orm service context-manager class which encapsulates db session and cruds

# TODO: test cascade deletions (use db brower for viewing)


# TODO: create user_takes_medicine table and test cascades on user delete (should delete all assocs of that user)
# NOTE: do we have to delete all the medicines if it was the last user?


def get_user_by_name(name: str, db: Session) -> Optional[User]:
    # NOTE: db should be open
    # with db:
    try:
        user: Optional[User] = (
            db.query(User)
            .filter(User.name == name)  # NOTE: is nullable
            .one()
        )
    except NoResultFound:
        print(f"No user named {name}")
        return None
    return user


def get_user_by_id(id: int, db: Session) -> Optional[User]:
    try:
        user: Optional[User] = (
            db.query(User)
            .filter(User.id == id)
            .one()
        )
    except NoResultFound:
        print(f"No user with id {id}")
        return None
    return user




# NOTE: may be wise to add a dto here (after parsing)
def add_user(name: str, db: Session) -> User:
    # with db:
    user: User = User(name=name)
    # print(id(user))
    # NOTE: all writes are queued into the session and executed later altogher (=unit of work)
    db.add(user)
    # db.commit()
    return user


def delete_user(name: str, db: Session) -> None:
    user: Optional[User] = get_user_by_name(name, db)
    if user:
        db.delete(user)
        # Exceptions are handled by outer ctx - rollback is done in case of uncatched exception
