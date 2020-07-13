import shodan

# SHODAN_API_KEY = "NAPxCiPa0Bir9q4oMiB1uiAWabMexDNB"
SHODAN_API_KEY = "BZwzKf7GQs1MvqWvwGJrf71ycJYX1QXC"

api = shodan.Shodan(SHODAN_API_KEY)

host = api.host('118.69.221.114')

print(host)