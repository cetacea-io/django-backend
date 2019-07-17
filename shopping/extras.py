from cetacea.settings.base import env
import braintree

gateway = braintree.BraintreeGateway(
    braintree.Configuration(
        environment=env('BRAINTREE_ENVIRONMENT'),
        merchant_id=env('BRAINTREE_MERCHANT_ID'),
        public_key=env('BRAINTREE_PUBLIC_KEY'),
        private_key=env('BRAINTREE_PRIVATE_KEY')
    )
)

def generate_client_token():
    return gateway.client_token.generate()

def transact(options):
    return gateway.transaction.sale(options)

def find_transaction(id):
    return gateway.transaction.find(id)