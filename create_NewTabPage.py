from os import remove
import utils.get_WeatherReport as weathers
import utils.get_PullAndPayInventory as vehicles
import utils.get_LinkData as linkies

# -----FUNCTIONS----- #

def main():
    # -----VARIABLES----- #
    outputFile = "./index.html"
    linkFile = "./data/links.txt"
    imageFolder = 'images/'

    try:
        remove(outputFile)
    except FileNotFoundError:
        print("This is your first time running this script.")

    newTabPage = open(outputFile, "a")

    print("Collecting weather data.")
    compiledWeatherData = weathers.main()
    print("Collecting vehicle data.")
    compiledVehicleData = vehicles.main()
    print("Collecting link data.")
    links = linkies.main(linkFile)
    print("Writing collected data to file.")

    start_indexPage(newTabPage)
    start_weatherSection(newTabPage)
    i = 0
    for weather in compiledWeatherData:
        write_weatherSection(newTabPage, weather)
        i += 1
        if i >= 4:
            break
    end_weatherSection(newTabPage)
    start_vehicleSection(newTabPage)
    for vehicle in compiledVehicleData:
        if int(vehicle.year) > 1997:
            if vehicle.onYard == "1 day" or len(vehicle.onYard) == 6:
                write_vehicleSection(newTabPage, vehicle)
            elif len(vehicle.onYard) == 7 and vehicle.onYard < "15 days":
                write_vehicleSection(newTabPage, vehicle)
    end_vehicleSection(newTabPage)
    start_linkSection(newTabPage)
    for link in links:
        if link[0][0] == '<' and link[0][-1] == '>':
            newTabPage.write(link[0] + "\n")
        else:
            linkLogo = imageFolder + link[1]
            write_linkSection(newTabPage, link[0], linkLogo, link[2])
    end_linkSection(newTabPage)
    end_indexPage(newTabPage)

    newTabPage.close()


def start_indexPage(page):
    page.write("<!DOCTYPE html> \n")
    page.write("<html lang=\"en\">\n")
    page.write("<HEAD>\n")
    page.write("	<TITLE>My New Tab</TITLE>\n")
    page.write("	<link rel=\"stylesheet\" href=\"index.css\">\n")
    page.write("</HEAD>\n")
    page.write("<BODY>\n")
    page.write("<CENTER>\n\n")


def start_weatherSection(page):
    page.write("<DIV class=\"section-group\">\n")


def write_weatherSection(page, weatherData):
    page.write("	<DIV ID=\"weather\" class=\"section-block\">\n")
    page.write("		<DIV class=\"weather-day\">\n")
    page.write("			<H3>" + weatherData.date + "</H3>\n")
    page.write("			<SPAN class=\"temperature\">" + weatherData.tempLow + "</SPAN>\n")
    page.write("			<SPAN class=\"temperature\">" + weatherData.tempHigh + "</SPAN>\n")
    page.write("			<SPAN class=\"Condition\">" + weatherData.condition + "</SPAN>\n")
    page.write("		</DIV>\n")
    page.write("		<DIV class=\"weather-status\">\n")
    page.write("			<SPAN class=\"status\">" + weatherData.humidity + " Hmdty</SPAN>\n")
    page.write("			<SPAN class=\"status\">" + weatherData.chanceOfRain + " Rain</SPAN>\n")
    page.write("			<SPAN class=\"status\">" + weatherData.wind + " Wind</SPAN>\n")
    page.write("		</DIV>\n")
    page.write("		<DIV class=\"weather-sun-moon\">\n")
    page.write("			<SPAN class=\"sun-left\">SunRise = " + weatherData.sunRise + "</SPAN>\n")
    page.write("			<SPAN class=\"moon-right\">MoonRise = " + weatherData.moonRise + "</SPAN>\n")
    page.write("		</DIV>\n")
    page.write("		<DIV class=\"weather-sun-moon\">\n")
    page.write("			<SPAN class=\"sun-left\">SunSet = " + weatherData.sunSet + "</SPAN>\n")
    page.write("			<SPAN class=\"moon-right\">MoonSet = " + weatherData.moonSet + "</SPAN>\n")
    page.write("		</DIV>\n")
    page.write("	</DIV>\n\n")


def end_weatherSection(page):
    page.write("</DIV>\n\n\n")


def start_vehicleSection(page):
    page.write("<DIV class=\"section-group\">\n")


def write_vehicleSection(page, vehicleData):
    page.write("	<DIV ID=\"upullandpay\" class=\"section-block\">\n")
    page.write("		<A href=\"" + vehicleData.page + "\" target=\"_blank\"> \n")
    page.write("		<DIV class=\"vehicle-data\">\n")
    page.write("			<SPAN class=\"vehicle-year\">" + vehicleData.year + "</SPAN>\n")
    page.write("			<SPAN class=\"vehicle-trim\">" + vehicleData.trim + "</SPAN>\n")
    page.write("			<H3>" + vehicleData.model + "</H3>\n")
    page.write("		</DIV>\n")
    page.write("		<DIV class=\"vehicle-age\">\n")
    page.write("			Avail\n")
    page.write("			<SPAN class=\"vehicle-age-number\">" + vehicleData.onYard + "</SPAN>\n")
    page.write("		</DIV>\n")
    page.write("		<SPAN class=\"vehicle-location\">" + vehicleData.location + "</SPAN>\n")
    page.write("		<SPAN class=\"vehicle-row\">Row: " + vehicleData.row + "</SPAN>\n")
    page.write("		</A>\n")
    page.write("	</DIV>\n\n")


def end_vehicleSection(page):
    page.write("</DIV>\n\n\n")


def start_linkSection(page):
    page.write("<DIV ID=\"link-group\" class=\"section-group\">\n")


def write_linkSection(page, linkName, linkLogo, linkURL):
    page.write("	<DIV ID=\"link-block\" class=\"section-block\">\n")
    page.write("		<A HREF=\"" + linkURL + "\" target=\"_blank\">\n")
    page.write("			<DIV class=\"favorite-link-logo\">\n")
    page.write("				<IMG SRC=\"" + linkLogo + "\">\n")
    page.write("			</DIV>\n")
    page.write("			<DIV class=\"favorite-link-name\">\n")
    page.write("				" + linkName + "\n")
    page.write("			</DIV>\n")
    page.write("		</A>\n")
    page.write("	</DIV>\n\n")


def end_linkSection(page):
    page.write("</DIV>\n\n\n")


def end_indexPage(page):
    page.write("</CENTER>\n")
    page.write("</BODY>\n")
    page.write("</HTML>\n\n")


# -----PROGRAM----- #

if __name__ == "__main__":
    main()
