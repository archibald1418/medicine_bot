from typing import Optional, List
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from app.models import Recipe, User


def get_recipes_by_user(name: str, db: Session) -> List[Recipe]:
    user: Optional[User] = get_user_by_name(name, db)
    if user is None:
        return []
    try:
        recipes: List[Recipe] = list(
            db.query(Recipe)
            .filter(Recipe.fk_user_id == user.id)
            .all()
        )
    except NoResultFound:
        print(f"No recipes with user {user.id}")
        return []
    return recipes


