from datetime import datetime
import sys
import re
import os
from time import sleep
from selenium import webdriver
#from selenium.webdriver.support.ui import WebDriverWait

"""
Returns a simplified version of current date in the format day - month - YEAR.
"""
def getTimeFormat():
	return str(datetime.today().strftime('%d-%m-%Y'))

"""
DEPRECATED: Search the content of the document for the title tag, used a regular expresion to include every posible title tag.

def getTitle(content):
	match = re.search('<title.*?>(.*?)</title>', content)
	return match.group(1) if match else 'No title'
"""

"""
Check if the given title is inactive or not, depending on the usual inactive titles for airbnb, vrbo and homeaway.
"""
def isInactive(title):
	
	airbnbTitle  	   = 'Vacation Rentals, Homes, Experiences &amp; Places - Airbnb'
	vrboTitle    	   = 'Top 50 Vacation Rentals | Vrbo.com'
	homeawayTitle      = 'Top 50 Vacation Rentals | HomeAway'
	genericTitle 	   = 'Vacation Rentals '
	alternativeTitleEs = "En cualquier lugar · Estadías · Airbnb"
	alternativeTitleEn = "Anywhere · Stays · Airbnb"
	
	if( title == airbnbTitle	    or
		title == vrboTitle          or
		title == homeawayTitle      or
		title == genericTitle 		or
		title == alternativeTitleEn or
		title == alternativeTitleEs ):
		return True
	
	return False

"""
Returns the input given by the user
"""
def readUserInput():
	fileName  = input("File  Name: ")
	titleRow  = input("Title  Row: ")
	sheetName = input("Sheet Name: ")
	return fileName, titleRow, sheetName

""" Returns a new Selenium driver. """
def openBrowser():
	#return webdriver.PhantomJS(executable_path='phantomjs')
	#return webdriver.Firefox()
	return webdriver.Chrome()

""" Closes the given driver instance. """
def closeBrowser(driver):
	driver.close()

""" Returns the title from a url given a driver.
    First  note: extensionTime will increase the execution time by O(tn) for a given extensionTime t.
    Second note: This execution time must be there as it's an explicit wait for javascript to load.
    Third  note: For slow internet conection, use bigger extensionTimes like 4 or 5.
"""
def getTitle(driver, url):
	extensionTime = 3
	try:
		driver.get(url)
		sleep(extensionTime)
		return driver.title
	except:
		print(sys.exc_info()[0])