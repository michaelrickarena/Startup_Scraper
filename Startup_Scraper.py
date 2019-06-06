from selenium import webdriver
from bs4 import BeautifulSoup
import time


url='https://angel.co/companies?company_types[]=Startup'
driver = webdriver.Firefox()
driver.get(url)
time.sleep(10)

html=driver.page_source

soup=BeautifulSoup(html,'html.parser')	

results=soup.find_all('div',{'class':'base startup'})



data = []
for result in results:
	datum ={}
	name=result.find('div',{'class':'name'}).get_text()
	pitch=result.find('div',{'class':'pitch'}).get_text()
	website=result.find('div',{'class':'website'}).get_text()
	stage=result.find('div',{'class':'stage'}).get_text()

	for more in result.find_all('div',{'class':'column raised'}):
		raised=more.find('div',{'class':'value'}).get_text()

	for more in result.find_all('div',{'class':'column market'}):
		market=more.find('div',{'class':'value'}).get_text()

	for more in result.find_all('div',{'class':'column company_size'}):
		company_size=more.find('div',{'class':'value'}).get_text()

	for more in result.find_all('div',{'class':'column joined'}):
		joined=more.find('div',{'class':'value'}).get_text()

	for more in result.find_all('div',{'class':'column location'}):
		location=more.find('div',{'class':'value'}).get_text()

def clean_string(var):
	var=str(var)
	var= var.rstrip() #removes white space at both ends
	var= var.replace('\n','') # search and replace
	return var

def clean_dollar(var):
	if '-' in var:
		return None
	var= var.rstrip()
	var= var.replace("\n", '')
	var= var.replace('$', '')
	var= var.replace(',', '')
	var= float(var)
	return var

datum['name'] = clean_string(name)
datum['pitch'] = clean_string(pitch)
datum['website'] = clean_string(website)
datum['stage'] = clean_string(stage)
datum['joined'] = clean_string(joined)
datum['location'] = clean_string(location)
datum['market'] = clean_string(market)
datum['company_size'] = clean_string(company_size)
datum['raised'] = clean_dollar(raised)


data.append(datum)

print(data)