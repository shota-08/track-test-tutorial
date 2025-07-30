from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from models import RecipeBase, RecipeCreateSuccessResponse, RecipeCreateFailureResponse, RecipeListResponse, RecipeDetailResponse, RecipeUpdateResponse
from database import SessionLocal, engine, Base
import crud

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/recipes/")
async def create_new_recipe(recipe: RecipeBase, db: Session = Depends(get_db)):
    try:
        db_recipe = crud.create_recipe(db, recipe)
        return RecipeCreateSuccessResponse(
            message="Recipe successfully created!",
            recipe=[db_recipe]
        )
    except Exception as e:
        return RecipeCreateFailureResponse(
            message="Recipe creation failed!",
            required="title, making_time, serves, ingredients, cost"
        )


@app.get("/recipes/")
async def get_all_recipe(db: Session = Depends(get_db)):
    recipes = crud.get_recipes(db)
    return RecipeListResponse(recipes=recipes)


@app.get("/recipes/{id}")
async def get_recipe_by_id(id: int, db: Session = Depends(get_db)):
    recipe = crud.get_recipe_by_id(db, id)
    if recipe is None:
        return {"message": "Recipe not found"}
    return RecipeDetailResponse(recipe=[recipe])


@app.patch("/recipes/{id}")
async def update_recipe_by_id(id: int, recipe: RecipeBase, db: Session = Depends(get_db)):
    updated_recipe = crud.update_recipe(db, id, recipe)
    if updated_recipe is None:
        return {"message": "Recipe not found"}
    return RecipeUpdateResponse(recipe=[updated_recipe])


@app.delete("/recipes/{id}")
async def delete_recipe_by_id(id: int, db: Session = Depends(get_db)):
    result = crud.delete_recipe(db, id)
    if result:
        return {"message": "Recipe successfully removed!"}
    else:
        return {"message": "No Recipe found"}
