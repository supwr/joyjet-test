from os import path
import json
from .models import Article, Cart, CartItem, DeliveryFee, Discount


def get_json(file):
    """
    Loads json from file
    """
    data = {}
    if path.exists(file):
        with open(file) as json_data:
            data = json.load(json_data)

    return data


def save_output(file_name, content):
    """
    Saves json output to file
    """
    with open(file_name, "w") as file:
        file.write(content)


def parse_articles(articles_json):
    """
    Parse articles from json to namedtuples.
    Returns a list of namedtuples.
    """
    articles = []

    for article in articles_json:
        articles.append(
            Article(id=article["id"], name=article["name"], price=article["price"])
        )

    return articles


def parse_carts(carts_json):
    """
    Parse carts from json to namedtuples.
    Returns a list of namedtuples.
    """
    carts = []

    for c in carts_json:
        items = []

        for i in c["items"]:
            items.append(CartItem(article_id=i["article_id"], quantity=i["quantity"]))

        carts.append(Cart(id=c["id"], items=items))

    return carts


def parse_delivery_fees(json_delivery_fees):
    """
    Parse delivery fees from json to namedtuple.
    Returns a list of namedtuples.
    """
    delivery_fees = []

    for delivery_fee in json_delivery_fees:
        eligible_transaction_volume = delivery_fee["eligible_transaction_volume"]
        delivery_fees.append(
            DeliveryFee(
                min_price=eligible_transaction_volume["min_price"],
                max_price=eligible_transaction_volume["max_price"],
                price=delivery_fee["price"],
            )
        )

    return delivery_fees


def parse_discounts(discounts_json):
    """
    Parse discounts from json to namedtuple.
    Returns a list of namedtuples.
    """
    discounts = []
    for discount in discounts_json:
        discounts.append(
            Discount(
                article_id=discount["article_id"],
                type=discount["type"],
                value=discount["value"],
            )
        )

    return discounts
