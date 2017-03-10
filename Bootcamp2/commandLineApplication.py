import json
def Africa_capital_cities():
	API_url="https://www.africanvault.com/list-countries-africa/"
	request=urlopen(API_url)
	country=request.read().decode("utf")
	json_object=json.loads(country)
	print(json.dumps(json_object))
	Africa_capital_cities() 