import collections

Article = collections.namedtuple("Article", "id name price")
Cart = collections.namedtuple("Cart", "id items")
CartItem = collections.namedtuple("CartItem", "article_id quantity")
DeliveryFee = collections.namedtuple("DeliveryFee", "min_price max_price price")
Discount = collections.namedtuple("Discount", "article_id type value")


def get_article(articles, id):
    """
    Queries article by article id
    """
    article = [a for a in articles if a.id == id]

    if len(article) > 0:
        return article[0]

    return None


def get_delivery_fee(delivery_fees, price):
    """
    Queries delivery fee by price range
    """
    fee = None
    for d in delivery_fees:
        min_price = d.min_price if d.min_price is not None else price
        max_price = d.max_price if d.max_price is not None else price
        if min_price <= price < max_price:
            fee = d

    if fee:
        return fee.price

    return 0


def get_discount(discounts, article_id):
    """
    Queries discount by article id
    """
    discount = [d for d in discounts if d.article_id == article_id]

    if len(discount) > 0:
        return discount[0]

    return None


def calculate_total(cart, articles=[], delivery_fees=[], discounts=[]):
    """
    Calculates cart's total price, applying delivery fees and discounts
    """
    total = 0
    for item in cart.items:
        article = get_article(articles, item.article_id)
        discount = get_discount(discounts, article.id)
        price = article.price

        if discount:
            if discount.type == "amount":
                price = int(price - discount.value)
            else:
                percentage = float(discount.value) / float(100)
                price = int(price - (price * percentage))

        total += int(item.quantity) * int(price)

    if delivery_fees:
        total += int(get_delivery_fee(delivery_fees, total))

    return {"id": cart.id, "total": total}
