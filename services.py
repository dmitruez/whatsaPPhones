from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class Service:
	options = Options()
	options.add_argument('--disable-blink-features=AutomationControlled')
	driver = webdriver.Chrome(options=options)
	driver.set_window_position(100, 100)
	driver.set_window_size(450, 450)
	wait = WebDriverWait(driver, 20)
	
	
	def get_qrcode(self):
		self.driver.get('https://web.whatsapp.com/')
		self.wait.until(ec.visibility_of_element_located((By.XPATH, "//canvas[@aria-label='Scan me!']")))
		self.driver.find_element(By.XPATH, "//div[@class='_19vUU']").screenshot('web/qr_code.png')
	
	
		
# service = Service()
# service.get_qrcode()
# service.get_names()