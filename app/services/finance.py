import requests

def calculate_rentability(n_price, actual_price, n_quantity, actual_quantity):
   
    """
    Calculate the rentability based on the provided parameters.

    :param n_price: The initial price of the asset.
    :param actual_price: The current price of the asset.
    :param n_quantity: The initial quantity of the asset.
    :param actual_quantity: The current quantity of the asset.
    :return: The calculated rentability as a float.
    """

    if n_price <= 0 or actual_price <= 0 or n_quantity <= 0 or actual_quantity <= 0:
        raise ValueError("Prices and quantities must be greater than zero.")

    rentability = ((actual_price * actual_quantity) - (n_price * n_quantity)) / (n_price * n_quantity)
    return rentability

def testing_get():
    """
    Just a simple test function to return a message.
    This function is used to verify that the service is running correctly.
    """

    return {
        "message": "This is a test response from the finance service."
    }

def crypto_price():
    """
    Fetch the current price of Ethereum in Bitcoin using the API from api-ninjas.
    This function retrieves the price of ETH in BTC and returns it as a JSON object.
    """

    symbol = 'ETHBTC'
    data = requests.get("https://api.api-ninjas.com/v1/cryptoprice?symbol={}".format(symbol), headers={
        "X-Api-Key": 'Td7mye3mN4eRMeQ1ulUB7g==le75Cpr4dH06E9IX'})

    if data.status_code == requests.codes.ok:
        print(data.text)
        return data.json()

    

    else:
        return {"error": "Failed to fetch crypto prices", "status_code": data.status_code, "reason": data.text}