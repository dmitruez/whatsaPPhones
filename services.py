from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import eel

options = Options()
options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(options=options)
driver.set_window_size(600, 600)
wait = WebDriverWait(driver, 20)


def get_qrcode():
	driver.get('https://web.whatsapp.com/')
	wait.until(ec.visibility_of_element_located((By.XPATH, "//canvas[@aria-label='Scan me!']")))
	driver.find_element(By.XPATH, "//div[@class='_19vUU']").screenshot('web/qr_code.png')


@eel.expose
def get_names():
	wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='g0rxnol2 _3fGK2']")))
	div_group = driver.find_element(By.XPATH, "//div[@class='g0rxnol2 _3fGK2']")
	scroll_high = driver.execute_script("return arguments[0].scrollHeight", div_group)
	current_high = 0
	names = []
	text = []
	while scroll_high > current_high:
		wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='_199zF _3j691']")))
		group_names = driver.find_elements(By.XPATH, "//div[@class='_199zF _3j691']")
		
		for name in group_names:
			if name.text not in text:
				names.append("data:image/png;base64," + name.screenshot_as_base64)
				text.append(name.text)
		current_high += 450
		driver.execute_script("arguments[0].scrollTop = arguments[0].scrollTop + 550", div_group)
		
	return names
