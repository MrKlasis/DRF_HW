import stripe

from config.settings import STRIP_API_KEY

stripe.api_key = STRIP_API_KEY


def product_create_stripe(prod_name):
    response = stripe.Product.create(name=prod_name)
    return response.get("id")


def price_create_stripe(prod_id, prod_price):
    response = stripe.Price.create(
        currency="usd",
        unit_amount=prod_price,
        product=prod_id,
    )
    return response.get("id")


def session_create_stripe(prod_price, count=1):
    response = stripe.checkout.Session.create(
      success_url="https://example.com/success",
      line_items=[{"price": prod_price, "quantity": count}],
      mode="payment",
    )
    return response.get("url")


# product_name = "Course"
# product_price = 100
#
# product_id = product_create_stripe(product_name)
# price_id = price_create_stripe(product_id, product_price)
# print(session_create_stripe(price_id))
