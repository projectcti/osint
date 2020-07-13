import shodan

SHODAN_API_KEY = "NAPxCiPa0Bir9q4oMiB1uiAWabMexDNB"

api = shodan.Shodan(SHODAN_API_KEY)

host = api.host('118.69.221.114')

print(host)