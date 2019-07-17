import graphene
import stripe
from .extras import transact
from cetacea.settings.base import env

stripe.api_key = env('STRIPE_SECRET_KEY')

# def create_checkout(request):
#     result = transact({
#         'amount': '11.00',
#         'payment_method_nonce': request,
#         'options': {
#             "submit_for_settlement": True
#         }
#     })

#     if result.is_success or result.transaction:
#         # return redirect(url_for('show_checkout',transaction_id=result.transaction.id))
#         return 'worked'
#     else:
#         for x in result.errors.deep_errors: print('Error: %s: %s' % (x.code, x.message))
#         # return redirect(url_for('new_checkout'))
#         return 'no worked'

class Purchase(graphene.Mutation):
    nonce = graphene.String(required=True)
    amount = graphene.Float(required=True)

    class Arguments:
        nonce = graphene.String(required=True)
        amount = graphene.Float(required=True)
    
    def mutate(self, info, nonce, amount):
        charge = stripe.Charge.create(
            amount=100,
            currency='usd',
            description='example',
            source='tok_1Eoo53LfRZjVPd22EbqMlnZE'
        )
        # result = transact({
        #     'amount': str(amount),
        #     'payment_method_nonce': nonce,
        #     'options': {
        #         "submit_for_settlement": True
        #     }
        # })

        # if result.is_success or result.transaction:
        #     # return redirect(url_for('show_checkout',transaction_id=result.transaction.id))
        #     return 'worked'
        # else:
        #     for x in result.errors.deep_errors: print('Error: %s: %s' % (x.code, x.message))
        #     # return redirect(url_for('new_checkout'))
        #     return 'no worked'

        return Purchase(nonce=nonce)

class Mutation(graphene.ObjectType):
    purchase = Purchase.Field()