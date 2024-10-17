from pynautobot import api

NAUTOBOT_URL = 'https://demo.nautobot.com'
API_TOKEN = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'

nautobot = api(url=NAUTOBOT_URL, token=API_TOKEN)
print(nautobot)

print(nautobot.dcim)