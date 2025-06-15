from enum import Enum

from fastapi import FastAPI, HTTPException

from app.data_loader import load_products


class ProductField(str, Enum):
    name = "name"
    description = "description"
    calories = "calories"
    fats = "fats"
    carbs = "carbs"
    proteins = "proteins"
    unsaturated_fats = "unsaturated fats"
    sugar = "sugar"
    salt = "salt"
    portion = "portion"


app = FastAPI()

products_data = load_products()


@app.get("/all_products/")
def get_all_products():
    return products_data


@app.get("/products/{product_name}")
def get_product_by_name(product_name: str):
    for product in products_data:
        if product["name"].lower() == product_name.lower():
            return product
    raise HTTPException(status_code=404, detail="Product not found")


@app.get("/products/{product_name}/{product_field}")
def get_product_field(product_name: str, product_field: ProductField):
    for product in products_data:
        if product["name"].lower() == product_name.lower():
            if product_field.value in product:
                return {product_field.value: product[product_field.value]}
            raise HTTPException(
                status_code=404, detail="Field not found in product"
            )
    raise HTTPException(status_code=404, detail="Product not found")
