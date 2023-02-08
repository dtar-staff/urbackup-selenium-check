from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from time import sleep


class MainPage:

	def __init__(self, driver, url):
		self.driver = driver
		sleep(1)
		self.csv_download_button = driver.find_element(By.XPATH, '//span[text()="CSV"]')

	def download_csv_report(self):
		self.csv_download_button.click()

