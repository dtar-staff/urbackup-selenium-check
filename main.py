from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from login_page import LoginPage
from main_page import MainPage

from time import sleep
from config import *

import csv
import os

driver_options = webdriver.FirefoxOptions()
driver_options.add_argument("-headless")
driver = webdriver.Firefox(options=driver_option)

login_page = LoginPage(driver, LOGIN_URL)
login_page.input_password(PASSWORD)
login_page.submit_login()

main_page = MainPage(driver, MAIN_PAGE_URL)
main_page.download_csv_report()
sleep(2)
driver.close()

with open(PATH + "/" + FNAME) as report_file:
	report_reader = csv.DictReader(report_file, delimiter=',', quoting=csv.QUOTE_ALL)
	for row in report_reader:
		print(row['\ufeff"Computer name"'], row["Last file backup"], row["File backup status"], sep="\t\t\t")

os.remove(PATH + "/" + FNAME)
