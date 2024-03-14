import requests

class countries():

	def __init__(self,url):
		self.url = url

	def get_json_data(self):

		try:
			response = requests.get(self.url, verify = False)
			response.raise_for_status()
			return response.json()
		except requests.exceptions.RequestException as e:
			print("Error fetching data:", e)
			return None

	def dollar_currency_country(self):
					data = self.get_json_data()
					if data is None:
						return None
			
					dollar_countries = []
			
					for i in data:
						if 'currencies' in i:
							for currency, details in i['currencies'].items():
								if 'dollar' in details['name']:
									dollar_countries.append(i['name']['common'])
									break
					return dollar_countries
										
			
	def euro_currency_country(self):
		data = self.get_json_data()
		if data is None:
			return None
		euro_countries = []
		for i in data:
			if 'currencies' in i:
				if 'EUR' in i['currencies']:
					euro_countries.append(i['name']['common'])		
		return euro_countries


	def country_name_currency_symbol(self):
		data = self.get_json_data()
		if data is None:
			return None
		countries= []
		currency_details = []
		for i in data:
			if 'name' in i and 'currencies' in i:
				for currency,details in i['currencies'].items():
					countries.append(i['name']['common'])
					currency_details.append(details)
		return countries,currency_details



get_data = countries("https://restcountries.com/v3.1/all")

d = get_data.dollar_currency_country()

print("The countries that has dollar as their currency are as follows: ", d)

e = get_data.euro_currency_country()

print("The countries that has euro as their currency are as follows: ", e)

x,y = get_data.country_name_currency_symbol()

data =[]

for i in range(0, len(x)):
    country_data = {}
    country_data['country_name'] = x[i]
    country_data['currency'] = y[i]
    data.append(country_data)

print(data)




""" The first line "import requests" imports the libraries related to the https pull for python, so my constructor class has only the url 
as a attribute apart from the self, where i m trying to get the url and creating an instance so that i can use it in all other methods.

 get_json_data() method is where i get the data from the given url using the request.json() method and also handling the exception just in case the url 
fails to fetch data. Also in the response.get() , i have added the attribute to verify the SSL certificate just in case the system that runs 
this code may not have the certificate like mine. 

and the next three methods as expected as follows which returns me the values of the country name, currency, countries using dollar and euro as
their currencies by fetching data from the constructor using the self.json_data """

