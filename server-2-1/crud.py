from sqlalchemy.orm import Session
from models import RecipeTable, RecipeBase
from datetime import datetime

def create_recipe(db: Session, recipe_data: RecipeBase):
    db_recipe = RecipeTable(
        title=recipe_data.title,
        making_time=recipe_data.making_time,
        serves=recipe_data.serves,
        ingredients=recipe_data.ingredients,
        cost=recipe_data.cost,
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe


def get_recipes(db: Session):
    return db.query(RecipeTable).all()


def get_recipe_by_id(db: Session, recipe_id: int):
    return db.query(RecipeTable).filter(RecipeTable.id == recipe_id).first()


def update_recipe(db: Session, recipe_id: int, recipe_data: RecipeBase):
    db_recipe = db.query(RecipeTable).filter(RecipeTable.id == recipe_id).first()
    if db_recipe is None:
        return None

    db_recipe.title = recipe_data.title
    db_recipe.making_time = recipe_data.making_time
    db_recipe.serves = recipe_data.serves
    db_recipe.ingredients = recipe_data.ingredients
    db_recipe.cost = recipe_data.cost
    db_recipe.updated_at = datetime.now()

    db.commit()
    db.refresh(db_recipe)
    return db_recipe


def delete_recipe(db: Session, recipe_id: int):
    db_recipe = db.query(RecipeTable).filter(RecipeTable.id == recipe_id).first()
    if db_recipe is None:
        return False
    db.delete(db_recipe)
    db.commit()
    return True
