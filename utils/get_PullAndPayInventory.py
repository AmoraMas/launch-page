import requests
import re
from bs4 import BeautifulSoup
from operator import attrgetter

# -----FUNCTIONS----- #

def main():
	# -----VARIABLES----- #
	vehicleSearch = ['chevrolet', 'S10'], ['GMC', 'Sonoma'], ['Chevrolet', 'Blazer'], ['GMC', 'Jimmy'], ['GMC', 'Jimmy+Or+Envoy'], ['GMC', 'Envoy'], ['GMC', 'Envoy+Xl'], ['GMC', 'Envoy+Xuv']
	locationSearch = [5]
	# LOCATION IDs =
	#   4 Albuquerque, NM
	#   5 Colorado Springs, CO
	#   6 Aurora, CO
	#   7 Denver, CO
	URLs = []
	compiledVehicleData = []
	
	for location in locationSearch:
		for vehicle in vehicleSearch:
			URL = 'https://upullandpay.com/search-inventory?locationId=' + str(location) + '&make=' + vehicle[0] + '&model=' + vehicle[1]
			URLs.append(URL)
	for URL in URLs:
		rawPageData = requests.get(URL)
		if rawPageData.status_code != 200:
			print('Error ' + str(rawPageData.status_code) + ' for page ' + rawPageData.url)
		else:
			#print('Page is good:  ' + rawPageData.url)
			soupPageData = BeautifulSoup(rawPageData.content, 'html.parser')
			#print(souppageData.prettify())
			sectionData = soupPageData.find('div', class_='vehicle-list')
			#print(sectionData.prettify())
			rawVehicleData = sectionData.find_all('div', {'class' : re.compile('vehicle-tile*')})
			#print(rawVehicleData)
			compiledVehicleData += compile_VehicleData(rawVehicleData)
	compiledVehicleData = sorted(compiledVehicleData, key = attrgetter('location', 'onYard', 'year'))

	#index = 0
	#while index < len(compiledVehicleData):
	#	print(compiledVehicleData[index].location)
	#	print(compiledVehicleData[index].year)
	#	print(compiledVehicleData[index].model)
	#	print(compiledVehicleData[index].row)
	#	print(compiledVehicleData[index].trim)
	#	print(compiledVehicleData[index].onYard)
	#	print(compiledVehicleData[index].VIN)
	#	print(compiledVehicleData[index].page)
	#	print(compiledVehicleData[index].imageURL)
	#	print('----------')
	#	index += 1
	return compiledVehicleData


def compile_VehicleData(rawVehicleData):
# extract relevant data and return as an object
	compiledVehicleData = []
	tempVehicleData = []
	
	for rawVehicle in rawVehicleData:
		#imageURL = vehicle.find('img', src=True)
		imageURL = rawVehicle.find('img')['src']
		tempVehicleData = rawVehicle.find_all('span')
		if tempVehicleData[0].text == 'New To Lot':
			index = 1
		else:
			index = 0
		year = tempVehicleData[index].text
		model = rawVehicle.find('h3').text
		location = tempVehicleData[index + 1].text
		row = tempVehicleData[index + 3].text
		trim = (tempVehicleData[index + 4].text).lstrip("Trim: ")
		onYard = (tempVehicleData[index + 5].text).lstrip("On Yard: ")
		if onYard == "Today":
			onYard = "0 Days"
		if onYard[1] == " ":
			onYard = "0" + onYard
		page = 'https://upullandpay.com' + (rawVehicle.find('a', href=True)['href'])
		VIN = page.lstrip("/search-inventory/vehicle?vin=")
		VIN = VIN[:17]
		
		tempVehicleData = create_VehicleObject(location, year, model, row, trim, onYard, VIN, page, imageURL)
		compiledVehicleData.append(tempVehicleData)
	return compiledVehicleData


# -----OBJECTS----- #

class create_VehicleObject:
	def __init__(self, location, year, model, row, trim, onYard, VIN, page, imageURL):
		self.location = location
		self.year = year
		self.model = model
		self.row = row
		self.trim = trim
		self.onYard = onYard
		self.VIN = VIN
		self.page = page
		self.imageURL = imageURL


# -----PROGRAM----- #

if __name__ == "__main__":
	main()
