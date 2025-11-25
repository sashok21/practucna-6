from typing import Optional
from decimal import Decimal

from pydantic import BaseModel, Field


class ProductCreateSchema(BaseModel):
    """Схема для створення нового товару."""
    name: str = Field(max_length=100)
    description: Optional[str] = Field(default=None, max_length=255)
    price: Decimal = Field(gt=0, decimal_places=2)  

    category_id: int = Field(gt=0)
    brand_id: int = Field(gt=0)

    in_stock: bool = Field(default=True)

    class Config:
        from_attributes = True



class CategorySchema(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class BrandSchema(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

    class Config:
        from_attributes = True


class ProductResponseSchema(ProductCreateSchema):
    """Схема для повернення одного товару (повний набір полів)."""
    id: int = Field(gt=0)
    category: CategorySchema
    brand: BrandSchema

    category_id: int = Field(exclude=True)
    brand_id: int = Field(exclude=True)

    class Config:
        from_attributes = True



class ProductPartialUpdateSchema(BaseModel):
    """Схема для часткового оновлення товару (використовується PATCH)."""
    name: Optional[str] = Field(default=None, max_length=100)
    description: Optional[str] = Field(default=None, max_length=255)
    price: Optional[Decimal] = Field(default=None, gt=0, decimal_places=2)
    in_stock: Optional[bool] = Field(default=None)

    category_id: Optional[int] = Field(default=None, gt=0)
    brand_id: Optional[int] = Field(default=None, gt=0)

    class Config:
        from_attributes = True
