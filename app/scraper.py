import requests
from bs4 import BeautifulSoup

from app.data_loader import save_products

HOME_URL = "https://www.mcdonalds.com/ua/uk-ua/eat/fullmenu.html"
PRODUCT_URL = ("https://www.mcdonalds.com/dnaapp/itemDetails?"
               "country=UA&language=uk&showLiveData=true&item=")


def get_nutrient_value(product_data: dict, nutrient_name: str):
    nutrient_list = product_data.get("nutrient_facts", {}).get("nutrient", [])
    for item in nutrient_list:
        if item.get("name") == nutrient_name:
            return item.get("value")
    return None


def parse_single_product(product_id: str):
    response = requests.get(PRODUCT_URL + product_id)
    response.raise_for_status()
    product_data = response.json().get("item", {})

    info = {
        "name": product_data.get("item_name"),
        "description": product_data.get("description"),
        "calories": get_nutrient_value(product_data, "Калорійність"),
        "fats": get_nutrient_value(product_data, "Жири"),
        "carbs": get_nutrient_value(product_data, "Вуглеводи"),
        "proteins": get_nutrient_value(product_data, "Білки"),
        "unsaturated_fats": get_nutrient_value(product_data, "НЖК"),
        "sugar": get_nutrient_value(product_data, "Цукор"),
        "salt": get_nutrient_value(product_data, "Сіль"),
        "portion": get_nutrient_value(product_data, "Вага порції"),
    }

    return info


def get_menu_products():
    response = requests.get(HOME_URL).content
    soup = BeautifulSoup(response, "html.parser")

    products_id = [
        item.get("data-product-id")
        for item in soup.select(".cmp-category__item")
    ]

    return [parse_single_product(product_id) for product_id in products_id]


def main():
    menu = get_menu_products()
    save_products(menu)
