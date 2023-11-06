from .. import User, Medicine, Recipe
from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound


def get_user_by_name(name: str, open_session: Session) -> Optional[User]:
    # with open_session:
    try:
        user: Optional[User] = (
            open_session.query(User)
            .filter(User.name == name) # NOTE: is nullable
            .one()
        )
        return user
    except NoResultFound:
        print(f"No user named {name}")
        return None


def get_user_by_id(id: int, open_session: Session) -> Optional[User]:
    try:
        user: Optional[User] = (
            open_session.query(User)
            .filter(User.id == id)
            .one()
        )
        return user
    except NoResultFound:
        print(f"No user with id {id}")
        return None


# def get_medicines_by_user(name: str, db: Session) -> List[Medicine]:
#     user: Optional[User] = get_user_by_name(name, db)
#     if user is None:
#         return []
#     with db:
#         meds: List[Medicine] = list(
#             db.query(Medicine)
#             .filter(Medicine.users.contains(user))
#             .all()
#         )
#     return meds


def get_recipes_by_user(name: str, open_session: Session) -> List[Recipe]:
    user: Optional[User] = get_user_by_name(name, open_session)
    if user is None:
        return []
    with open_session:
        recipes: List[Recipe] = list(
            open_session.query(Recipe)
            .filter(Recipe.user.id == user.id)
            .all()
        )
    return recipes



# NOTE: may be wise to add a dto here (after parsing)
def add_user(name: str, db: Session) -> User:
    # with db:
    user: User = User(name=name)
    print(id(user))
    db.add(user)
    db.commit()
    return user
