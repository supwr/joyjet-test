import json
from .settings import TEST2_PATH
from .models import calculate_total
from .json_parser import (
    get_json,
    save_output,
    parse_articles,
    parse_carts,
    parse_delivery_fees,
)


def generate_output():
    carts = []
    articles = []
    delivery_fees = []
    result = []

    data_file = r"%s\%s" % (TEST2_PATH, "data.json")
    data = get_json(data_file)

    if "delivery_fees" in data:
        delivery_fees = parse_delivery_fees(data["delivery_fees"])

    if "articles" in data:
        articles = parse_articles(data["articles"])

    if "carts" in data:
        carts = parse_carts(data["carts"])

    for cart in carts:
        result.append(calculate_total(cart, articles, delivery_fees))

    output_file = r"%s\%s" % (TEST2_PATH, "output.json")
    save_output(output_file, json.dumps({"carts": result}))


def get_json_data(file):
    output_file = r"%s\%s" % (TEST2_PATH, file)
    return get_json(output_file)


def get_readme():
    readme_file = r"%s\%s" % (TEST2_PATH, "README.md")
    content = ""
    with open(readme_file) as f:
        return f.read()

    return content
