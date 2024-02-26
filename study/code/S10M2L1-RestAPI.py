import requests

# parameters to limit GET requests to a single instance of a product.  Specific to FakeStoreAPI
parameters = {'limit':1}

response = requests.get('https://fakestoreapi.com/products', params=parameters)
print(response.json())
