#Imports
import pandas as pd
import requests
import os
import sys
from time import sleep
import src.util as ut

"""	
	fileName  = Name of the file, no .xlsx termination
	titleRow  = The row that contains the titles
	sheetName = Sheet we are going to use as template

	returns a datraframe with the data from the spreadsheet.
"""
def readExcel(fileName, titleRow, sheetName):
	try:
		excelFileName = "./io/input/" + fileName + ".xlsx"

		data = pd.read_excel(excelFileName, header=(int(titleRow) - 1), sheet_name=sheetName)#, usecols=['provider_url', 'active'])
		
		return data
	except Exception as ex:
		print(ex)
		input()



"""
	urls 	 = dataframe
	fileName = Output fileName

	returns an array with response and count.
"""
def transform(urls, fileName):

	count = 0
	f = open("./io/output/report.txt", "w")				# Open report file in write mode

	try:
		browser = ut.openBrowser()						# Open browser instance

		for index, row in urls.iterrows():				# For each row with given index
			url = row['provider_url']
			if url != float('nan'):						# Check if url is empty
				title = ut.getTitle(browser, url)
				#print(index + 3, ut.isInactive(title), title)
				if(ut.isInactive(title)):				# Check if the title is active or not
					urls.loc[index, 'active'] = 'no'	# First, set the value of active to no if title IS inactive
					msg = 'Found inactive at ' + str(index + 3) + ' with the link ' + row['provider_url'] # Generic message to print
					print(msg) 							# Print message
					f.write(str(msg) + ' ' + ut.getTimeFormat() + "\n") # Write message plus current time.
					count = count + 1					# Increase count of inactive listings

				else:
					urls.loc[index, 'active'] = 'yes'	# Set value to yes (active)
				#input()

		ut.closeBrowser(driver) 						# Close browser
	except Exception as ex:
		print(sys.exc_info()[0])
		print(ex)

	countMsg = 'Found a total of: ' + str(count) + ' inactive listings.' # Message with the count of how many inactives we have.
	
	print(countMsg) 								# Print message
	f.write(str(countMsg)) 							# Write message in report.txt
	f.close() 										# Close report.txt
	
	urls.to_excel( './io/output/' + str(fileName) + '.xlsx' ) # Write dataframe to excel file. 

def main():
	#fileName, titleRow, sheetName = 'cathedral_v3', 2, 'Juan'
	fileName, titleRow, sheetName = ut.readUserInput()
	df = readExcel(fileName, titleRow, sheetName)
	transform(df, fileName)




if __name__ == "__main__":
	main()