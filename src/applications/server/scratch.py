import requests
def main():
    response = requests.get('https://justiz.de/onlinedienste/insolvenzbekanntmachungen/index.php')
    print(response.text)

main()