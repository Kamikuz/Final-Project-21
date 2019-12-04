import requests
import json

countrylist = requests.get('https://restcountries.eu/rest/v2/all')
countrylist = countrylist.json()

file = open('file.txt','w')

for item in countrylist:
	x = '<option id="sel' + item['alpha3Code'] + '" value="sel' + item['alpha3Code'] + '">'+ item['name'] +'</option>'
	print(x)