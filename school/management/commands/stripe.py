import json

import stripe
from django.core.management import BaseCommand

from config.settings import STRIP_API_KEY


class Command(BaseCommand):

    def handle(self, *args, **options):
        stripe.api_key = STRIP_API_KEY

        response = stripe.Product.create(name="Gold Plan")
        product = json.loads(response.last_response.body)
        product_id = product.get('id')

        return product_id



        # stripe.checkout.Session.create(
        #     success_url="https://example.com/success",
        #     line_items=[{"price": "price_1MotwRLkdIwHu7ixYcPLm5uZ", "quantity": 2}],
        #     mode="payment",
        # )









        # response = stripe.PaymentIntent.create(
        #     amount=2000,
        #     currency="usd",
        #     automatic_payment_methods={"enabled": True},
        # )
        # return response.status

