import requests
from bs4 import BeautifulSoup
import re


### ---FUNCTIONS--- ###

def main():
	### ---VARIABLES--- ###
	# hourlyURL = "https://weather.com/weather/hourbyhour/l/5d0543c2af6cef0b584364966f20f16d3bf7a4acfa7ee4e539d968360c6abf81"
	# hourlyWeatherData = []
	dailyURL = "https://weather.com/weather/tenday/l/5d0543c2af6cef0b584364966f20f16d3bf7a4acfa7ee4e539d968360c6abf81"
	compiledWeatherData = []

	#rawHourlyData = requests.get(hourlyURL)
	rawDailyData = requests.get(dailyURL)

	if rawDailyData.status_code != 200:
		print('Request for url ' + rawDailyData.url + ' recieved an error code of ' + 	str(rawDailyData.status_code) + '.')
	else:
		soupDailyData = BeautifulSoup(rawDailyData.content, 'html.parser')
		dailyData = soupDailyData.find('div', {'class' : re.compile('DailyForecast--DisclosureList--*')})
		refinedData = dailyData.find_all('details')
		compiledWeatherData = compile_DailyWeatherData(refinedData)
	
	#print(compiledWeatherData[0].sunRise)
	#print(compiledWeatherData[0].moonRise)
	#print(compiledWeatherData[0].moonPhrase)
	
	return compiledWeatherData

def compile_DailyWeatherData(refinedData):
# extract relevant data and return as an object
	allWeatherData = []
	someWeatherData = []
	for data in refinedData:
		date = data.find('h3')
		date = date.text
		tempHigh = data.find('span', {'class' : re.compile('DetailsSummary--highTempValue--*')}).text
		tempLow = data.find('span', {'class' : re.compile('DetailsSummary--lowTempValue--*')}).text
		condition = data.find('span', {'class' : re.compile('DetailsSummary--extendedData--*')}).text
		chanceOfRain = data.find('div', {'class' : re.compile('DetailsSummary--precip--*')})
		chanceOfRain = chanceOfRain.find('span').text
		wind = data.find('div', {'class' : re.compile('DetailsSummary--wind--*')})
		wind = wind.find('span').text
		
		nextSections = data.find_all('ul', {'class' : re.compile('DetailsTable--DetailsTable--*')})
		nextSection = nextSections[0].find_all('li')
		for section in nextSection:
			label = section.find('span', {'class' : re.compile('DetailsTable--label--*')}).text
			value = section.find('span', {'class' : re.compile('DetailsTable--value--*')}).text
			if label == 'Humidity':
				humidity = value
			elif label == 'UV Index':
				uvIndex = value
			elif label == 'Sunrise':
				sunRise = value
			elif label == 'Sunset':
				sunSet = value
			elif label == 'Moonrise':
				moonRise = value
			elif label == 'Moonset':
				moonSet = value
		try:
			sunRise
		except NameError:
			sunRise = 'N/A'
		try:
			sunSet
		except NameError:
			sunSet = 'N/A'
		try:
			moonRise
		except NameError:
			nextSection = nextSections[1].find_all('li')
			for section in nextSection:
				label = section.find('span', {'class' : re.compile('DetailsTable--label--*')}).text
				value = section.find('span', {'class' : re.compile('DetailsTable--value--*')}).text
				if label == 'Moonrise':
					moonRise = value
				elif label == 'Moonset':
					moonSet = value
		moonPhrase = data.find('span', {'class' : re.compile('DetailsTable--moonPhrase--*')}).text
		
		weatherData = DayData(date, tempHigh, tempLow, condition, chanceOfRain, wind, humidity, uvIndex, sunRise, sunSet, moonRise, moonSet, moonPhrase)
		allWeatherData.append(weatherData)
		del(sunRise)
		del(sunSet)
		del(moonRise)
		del(moonSet)
	return allWeatherData


### ---OBJECTS--- ###

class DayData:
	def __init__(self, date, tempHigh, tempLow, condition, chanceOfRain, wind, humidity, uvIndex, sunRise, sunSet, moonRise, moonSet, moonPhrase):
		self.date = date
		self.tempHigh = tempHigh
		self.tempLow = tempLow
		self.condition = condition
		self.chanceOfRain = chanceOfRain
		self.wind = wind
		self.humidity = humidity
		self.uvIndex = uvIndex
		self.sunRise = sunRise
		self.sunSet = sunSet
		self.moonRise = moonRise
		self.moonSet = moonSet
		self.moonPhrase = moonPhrase


### ---PROGRAM--- ###

if __name__ == "__main__":
	main()

