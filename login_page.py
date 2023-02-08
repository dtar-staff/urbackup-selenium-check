from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from time import sleep


class LoginPage:

	def __init__(self, driver, url):
		driver.get(url)
		sleep(2)
		self.password_input = driver.find_element(By.XPATH, '//input[@id="password"]')
		self.submit_button = driver.find_element(By.XPATH, '//button[@type="submit"]')

	def input_password(self, password):
		self.password_input.send_keys(password)

	def submit_login(self):
		self.submit_button.click()
