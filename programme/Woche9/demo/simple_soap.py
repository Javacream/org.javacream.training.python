from suds.client import Client
def main():
    wsdl_location = 'https://www.w3schools.com/xml/tempconvert.asmx?WSDL'
    client = Client(wsdl_location)
    print(client)
    print(client.service.CelsiusToFahrenheit('11'))
    print(client.service.FahrenheitToCelsius('11'))

main()