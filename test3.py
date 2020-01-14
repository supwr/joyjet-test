import json
from .settings import TEST3_PATH
from .models import calculate_total
from .json_parser import (
    get_json,
    save_output,
    parse_articles,
    parse_carts,
    parse_discounts,
    parse_delivery_fees,
)


def generate_output():
    carts = []
    articles = []
    delivery_fees = []
    discounts = []
    result = []

    data_file = r"%s\%s" % (TEST3_PATH, "data.json")
    data = get_json(data_file)

    if "delivery_fees" in data:
        delivery_fees = parse_delivery_fees(data["delivery_fees"])

    if "discounts" in data:
        discounts = parse_discounts(data["discounts"])

    if "articles" in data:
        articles = parse_articles(data["articles"])

    if "carts" in data:
        carts = parse_carts(data["carts"])

    for cart in carts:
        result.append(calculate_total(cart, articles, delivery_fees, discounts))

    output_file = r"%s\%s" % (TEST3_PATH, "output.json")
    save_output(output_file, json.dumps({"carts": result}))


def get_json_data(file):
    output_file = r"%s\%s" % (TEST3_PATH, file)
    return get_json(output_file)


def get_readme():
    readme_file = r"%s\%s" % (TEST3_PATH, "README.md")
    content = ""
    with open(readme_file) as f:
        return f.read()

    return content
