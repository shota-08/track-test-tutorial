from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, DateTime
from database import Base


class RecipeTable(Base):
    __tablename__ = "recipes"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, nullable=False)
    making_time = Column(String, nullable=False)
    serves = Column(String, nullable=False)
    ingredients = Column(String, nullable=False)
    cost = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class RecipeBase(BaseModel):
    title: str
    making_time: str
    serves: str
    ingredients: str
    cost: str


class Recipe(RecipeBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class RecipeCreateSuccessResponse(BaseModel):
    message: str = "Recipe successfully created!"
    recipe: List[Recipe]


class RecipeCreateFailureResponse(BaseModel):
    message: str = "Recipe creation failed!"
    required: str = "title, making_time, serves, ingredients, cost"


class RecipeListResponse(BaseModel):
    recipes: List[Recipe]


class RecipeDetailResponse(BaseModel):
    message: str = "Recipe details by id"
    recipe: List[Recipe]


class RecipeUpdateResponse(BaseModel):
    message: str = "Recipe successfully updated!"
    recipe: List[Recipe]

