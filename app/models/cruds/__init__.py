from .. import User, Medicine, Recipe
from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound


def get_user_by_name(name: str, db: Session) -> Optional[User]:
    with db:
        try:
            user: Optional[User] = (
                db.query(User)
                .filter(User.name == name)
                .one()
            )
            return user
        except NoResultFound:
            print(f"No user named {name}")
            return None


def get_user_by_id(id: int, db: Session) -> Optional[User]:
    with db:
        try:
            user: Optional[User] = (
                db.query(User)
                .filter(User.id == id)
                .one()
            )
            return user
        except NoResultFound:
            print(f"No user with id {id}")
            return None


def get_medicines_by_user(name: str, db: Session) -> List[Medicine]:
    user: Optional[User] = get_user_by_name(name, db)
    if user is None:
        return []
    with db:
        meds: List[Medicine] = list(
            db.query(Medicine)
            .filter(Medicine.users.contains(user))
            .all()
        )
    return meds


def get_recipes_by_user(name: str, db: Session) -> List[Recipe]:
    user: Optional[User] = get_user_by_name(name, db)
    if user is None:
        return []
    with db:
        recipes: List[Recipe] = list(
            db.query(Recipe)
            .filter(Recipe.user.id == user.id)
            .all()
        )
    return recipes



# NOTE: may be wise to add a dto here (after parsing)
def add_user(name: str, db: Session) -> User:
    with db:
        user: User = User(name=name)
        db.add(user)
        db.commit()
        return user
