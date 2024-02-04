from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup as bs
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By





class Parser:
	driver = webdriver.Chrome()
	wait = WebDriverWait(driver, 20)
	