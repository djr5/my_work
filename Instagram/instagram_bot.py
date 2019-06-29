from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from credentials import IGUSERNAME, IGPASSWORD, HASHTAGS


class InstgramBot:
	"""docstring for InstgramBot"""
	def __init__(self, username, password):
		self.username = username
		self.password = password
		# self.driver = webdriver.Firefox()
		self.driver = webdriver.Chrome()

	def closeBrowser():
		self.driver.close()

	def login(self):
		driver = self.driver
		driver.get("https://www.instagram.com/accounts/login/")
		time.sleep(3)
		user_name = driver.find_element_by_xpath("//input[@name='username']")
		user_name.clear()
		user_name.send_keys(self.username)
		user_password = driver.find_element_by_xpath("//input[@name='password']")
		user_password.clear()
		user_password.send_keys(self.password)
		user_password.send_keys(Keys.RETURN)
		time.sleep(18)


	def picsLike(self, hashtag):
		driver = self.driver
		driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
		time.sleep(2)

		for page in range(1,3):
			driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
			time.sleep(2)
		href_tags = driver.find_elements_by_tag_name('a')
		pic_links = [tag.get_attribute('href') for tag in href_tags]
		pic_links = [pic_link for pic_link in pic_links if "www.instagram.com/p/" in pic_link]

		for pic in pic_links:
			driver.get(pic)
			driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

			try:
				time.sleep(2)
				# if driver.find_element_by_xpath("//span[@aria-label='Like']"):
				# 	print('LikeFound')
				driver.find_element_by_xpath("//span[@aria-label='Like']").click()
				time.sleep(18)
			except Exception as e:
				time.sleep(2)


rakend = InstgramBot(IGUSERNAME, IGPASSWORD)
rakend.login()
[rakend.picsLike(tag) for tag in HASHTAGS]

