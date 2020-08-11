import base64
import configparser
import json
import os
import time
from difflib import SequenceMatcher
import pyautogui
from PIL import Image
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

class utility:

	def __init__(self, driver):
		self.browserwait = 25
		self.driver= driver

	def quan_driver(self):
		return self.driver

	def quan_navigate_url(self, url):
		self.wait = WebDriverWait(self.driver, self.browserwait)
		self.driver.get(url)
		self.driver.set_page_load_timeout(25)

	def quan_find_element(self, webelement, webvalue):
		if webelement == 'id':
			return self.driver.find_element_by_id(webvalue)
		if webelement == 'xpath':
			return self.driver.find_element_by_xpath(webvalue)
		if webelement == 'linktext':
			return self.driver.find_element_by_link_text(webvalue)
		if webelement == 'partiallinktext':
			return self.driver.find_element_by_partial_link_text(webvalue)
		if webelement == 'name':
			return self.driver.find_element_by_name(webvalue)
		if webelement == 'tagname':
			return self.driver.find_element_by_tag_name(webvalue)
		if webelement == 'classname':
			return self.driver.find_element_by_class_name(webvalue)
		if webelement == 'css':
			return self.driver.find_element_by_css_selector(webvalue)

	def quan_find_elements(self, webelement, webvalue):
		if webelement == 'id':
			return self.driver.find_elements_by_id(webvalue)
		if webelement == 'xpath':
			return self.driver.find_elements_by_xpath(webvalue)
		if webelement == 'linktext':
			return self.driver.find_elements_by_link_text(webvalue)
		if webelement == 'partiallinktext':
			return self.driver.find_elements_by_partial_link_text(webvalue)
		if webelement == 'name':
			return self.driver.find_elements_by_name(webvalue)
		if webelement == 'tagname':
			return self.driver.find_elements_by_tag_name(webvalue)
		if webelement == 'classname':
			return self.driver.find_elements_by_class_name(webvalue)
		if webelement == 'css':
			return self.driver.find_elements_by_css_selector(webvalue)

	def quan_by_element(self, webelement, webvalue):
		if webelement == 'id':
			return By.ID, webvalue
		if webelement == 'xpath':
			return By.XPATH, webvalue
		if webelement == 'classname':
			return By.CLASS_NAME, webvalue
		if webelement == 'cssselector':
			return By.CSS_SELECTOR, webvalue
		if webelement == 'linktext':
			return By.LINK_TEXT, webvalue
		if webelement == 'name':
			return By.NAME, webvalue
		if webelement == 'partiallinktext':
			return By.PARTIAL_LINK_TEXT, webvalue
		if webelement == 'tagname':
			return By.TAG_NAME, webvalue

	def quan_send_key(self, webelement, webvalue, input):
		self.quan_wait_until_visibility_of_element_located(webelement, webvalue)
		self.quan_find_element(webelement, webvalue).send_keys(input)

	def quan_clear(self, webelement, webvalue):
		self.quan_wait_until_visibility_of_element_located(webelement, webvalue)
		self.quan_find_element(webelement, webvalue).clear()

	def quan_click(self, webelement, webvalue):
		self.quan_wait_until_visibility_of_element_located(webelement, webvalue)
		self.quan_find_element(webelement, webvalue).click()

	def quan_delete_all_cookies(self):
		self.driver.delete_all_cookies()

	def quan_browser_quit(self):
		self.driver.quit()

	def quan_current_url(self):
		return self.driver.current_url

	def quan_scroll_to_element(self, webelement, webvalue):
		self.driver.execute_script("arguments[0].scrollIntoView();", self.quan_find_element(webelement, webvalue))

	def quan_select_by_index(self, webelement, webvalue, index):
		select = Select(self.quan_find_element(webelement, webvalue))
		select.select_by_index(index)

	def quan_select_by_visible_text(self, webelement, webvalue, visibletext):
		select = Select(self.quan_find_element(webelement, webvalue))
		select.select_by_visible_text(visibletext)

	def quan_select_by_value(self, webelement, webvalue, value):
		select = Select(self.quan_find_element(webelement, webvalue))
		select.select_by_value(value)

	def quan_deselect_all(self, webelement, webvalue):
		select = Select(self.quan_find_element(webelement, webvalue))
		select.deselect_all()

	def quan_selected_list(self, webelement, webvalue):
		select = Select(self.quan_find_element(webelement, webvalue))
		all_selected_options = select.all_selected_options
		return all_selected_options

	def quan_drag_and_drop(self, element, target):
		action_chains = ActionChains(self.driver)
		action_chains.drag_and_drop(element, target).perform()

	def quan_switch_to_window(self, windowName):
		self.driver.switch_to_window(windowName)

	def quan_switch_to_frame(self, frameName):
		self.driver.switch_to_frame(frameName)

	def quan_forward_browser(self):
		self.driver.forward()

	def quan_backwared_browser(self):
		self.driver.back()

	def quan_zoom_out(self, value):
		self.driver.execute_script("document.body.style.zoom='"+str(value)+"%'")

	def quan_screenshot(self, path):
		self.driver.save_screenshot(path)

	def quan_get_text(self, webelement, webvalue):
		return self.quan_find_element(webelement, webvalue).text

	def quan_download_image(self, webelement, webvalue, path):
		img = self.quan_find_element(webelement, webvalue)
		img.screenshot(path)

	def quan_full_screenshot(self, path):
		screenshot = pyautogui.screenshot()
		screenshot.save(path)

	def quan_cropimage(self, x, y, width, height, sourcepath, destinationpath):
		im = Image.open(sourcepath)
		im = im.crop((int(x), int(y), int(width), int(height)))
		im.save(destinationpath)

	def quan_wait_until_clickable(self, webelement, webvalue):
		self.wait.until(EC.element_to_be_clickable((self.quan_by_element(webelement, webvalue))))

	def quan_wait_until_title_is(self, webelement, webvalue):
		self.wait.until(EC.title_is((self.quan_by_element(webelement, webvalue))))

	def quan_wait_until_title_contains(self, webelement, webvalue):
		self.wait.until(EC.title_contains((self.quan_by_element(webelement, webvalue))))

	def quan_wait_until_presence_of_element_located(self, webelement, webvalue):
		self.wait.until(EC.presence_of_element_located((self.quan_by_element(webelement, webvalue))))

	def quan_wait_until_visibility_of_element_located(self, webelement, webvalue):
		self.wait.until(EC.visibility_of_element_located((self.quan_by_element(webelement, webvalue))))

	def quan_wait_until_visibility_of(self, webelement, webvalue):
		self.wait.until(EC.visibility_of((self.quan_by_element(webelement, webvalue))))

	def quan_wait_until_presence_of_all_element_located(self, webelement, webvalue):
		self.wait.until(EC.presence_of_all_elements_located((self.quan_by_element(webelement, webvalue))))

	def quan_wait_until_text_to_be_present_in_element(self, webelement, webvalue):
		self.wait.until(EC.text_to_be_present_in_element((self.quan_by_element(webelement, webvalue))))

	def quan_wait_until_text_to_be_present_in_element_value(self, webelement, webvalue):
		self.wait.until(EC.text_to_be_present_in_element_value((self.quan_by_element(webelement, webvalue))))

	def quan_wait_until_frame_to_be_available_and_switch_to_it(self, webelement, webvalue):
		self.wait.until(EC.frame_to_be_available_and_switch_to_it((self.quan_by_element(webelement, webvalue))))

	def quan_wait_until_invisiblity_of_element_located(self, webelement, webvalue):
		self.wait.until(EC.invisibility_of_element_located((self.quan_by_element(webelement, webvalue))))

	def quan_wait_until_invisiblity_of_element(self, webelement, webvalue):
		self.wait.until(EC.invisibility_of_element((self.quan_by_element(webelement, webvalue))))

	def quan_wait_until_staleness_of(self, webelement, webvalue):
		self.wait.until(EC.staleness_of((self.quan_by_element(webelement, webvalue))))

	def quan_wait_until_element_to_be_selected(self, webelement, webvalue):
		self.wait.until(EC.element_to_be_selected((self.quan_by_element(webelement, webvalue))))

	def quan_wait_until_element_located_to_be_selected(self, webelement, webvalue):
		self.wait.until(EC.element_located_to_be_selected((self.quan_by_element(webelement, webvalue))))

	def quan_wait_until_element_selection_state_to_be(self, webelement, webvalue):
		self.wait.until(EC.element_selection_state_to_be((self.quan_by_element(webelement, webvalue))))

	def quan_wait_until_element_located_selection_state_to_be(self, webelement, webvalue):
		self.wait.until(EC.element_located_selection_state_to_be((self.quan_by_element(webelement, webvalue))))

	def quan_similar(a, b):
		return SequenceMatcher(None, a, b).ratio()

	def quan_current_working_dir(self):
		return str(os.getcwd())

##################################################### Kailash Code ######################################################

	# To get typed text from a input text field
	def quan_get_user_text(self, webelement, webvalue):
		return (self.quan_find_element(webelement, webvalue).get_attribute('value'))

	# To get href link
	def quan_get_link(self, webelement, webvalue):
		return (self.quan_find_element(webelement, webvalue).get_attribute('href'))

	# Scroll and with URL - Image
	def quan_full_page_screenshot(self, path):
		ScrollHeight = self.driver.execute_script("return document.documentElement.scrollHeight")
		for height in range(0, ScrollHeight, 500):
			self.driver.execute_script("window.scrollTo(0, " + str(height) + ");")
			time.sleep(2)
			self.quan_full_screenshot(path + 'screenshot' + str(height) + '.png')
			time.sleep(2)

	# With URL - JSON
	def quan_full_screenshot_json(self, keyname):
		data = {}
		screenshot = pyautogui.screenshot()
		screenshot_bytes = screenshot.tobytes()
		data[keyname] = base64.encodebytes(screenshot_bytes).decode("utf-8")
		screenshot_json_obj = json.dumps(data)
		return screenshot_json_obj

	# Scroll and with URL - JSON
	def quan_full_page_screenshot_json(self, keyname):
		ScrollHeight = self.driver.execute_script("return document.documentElement.scrollHeight")
		data = {}
		for height in range(0, ScrollHeight, 500):
			self.driver.execute_script("window.scrollTo(0, " + str(height) + ");")
			time.sleep(2)
			screenshot = pyautogui.screenshot()
			screenshot_bytes = screenshot.tobytes()
			data[keyname + ' ' + str(height)] = base64.encodebytes(screenshot_bytes).decode("utf-8")
			time.sleep(2)
		screenshot_json_obj = json.dumps(data)
		return screenshot_json_obj

	# To check whether a Radio button is clicked
	def quan_radio_checked(self, webelement, webvalue):
		return (self.quan_find_element(webelement, webvalue)).is_selected()


	# To check whether a Checkbox is clicked
	def quan_box_checked(self, webelement, webvalue):
		return (self.quan_find_element(webelement, webvalue)).is_selected()

	# Wait until Alert pops up
	# def quan_wait_until_alert_pops_up(self, webelement, webvalue):
	# 	self.wait.until(EC.alert_is_present((self.quan_by_element(webelement, webvalue))))

	# Switch to Alert
	# def quan_switch_to_alert(self, webelement, webvalue):
	# 	self.wait.until(EC.switch_to_alert((self.quan_by_element(webelement, webvalue))))