# task2_selenium.py
# Automated Login Test with Selenium (AI-assisted)

import sys
import time

# Try to import Selenium and give a helpful message if it's missing
try:
	from selenium import webdriver
	from selenium.webdriver.common.by import By
	from selenium.webdriver.common.keys import Keys
	from selenium.webdriver.chrome.service import Service
	from selenium.webdriver.chrome.options import Options
except ImportError:
	print("Missing Python package 'selenium'.")
	print("Install it with: pip install selenium webdriver-manager")
	print("Or add Selenium to your environment (e.g., requirements.txt).")
	sys.exit(1)

# Optional: use webdriver-manager to automatically install chromedriver
try:
	from webdriver_manager.chrome import ChromeDriverManager
	webdriver_manager_available = True
except Exception:
	webdriver_manager_available = False


def create_driver(headless=True):
	chrome_options = Options()
	if headless:
		# use the modern headless flag if supported
		chrome_options.add_argument('--headless=new')
	chrome_options.add_argument('--no-sandbox')
	chrome_options.add_argument('--disable-dev-shm-usage')

	# Use webdriver-manager if available to avoid requiring chromedriver on PATH
	if webdriver_manager_available:
		service = Service(ChromeDriverManager().install())
	else:
		# assumes chromedriver is on PATH
		service = Service()

	driver = webdriver.Chrome(service=service, options=chrome_options)
	return driver


def main():
	driver = create_driver(headless=True)

	try:
		# Test URL (replace with your app or demo login page)
		driver.get("https://example.com/login")

		# --- Test Case 1: Valid Login ---
		driver.find_element(By.ID, "username").send_keys("valid_user")
		driver.find_element(By.ID, "password").send_keys("correct_password")
		driver.find_element(By.ID, "login-button").click()
		time.sleep(3)
		print("✅ Valid Login Test Passed" if "dashboard" in driver.current_url else "❌ Valid Login Failed")

		# --- Test Case 2: Invalid Login ---
		driver.get("https://example.com/login")
		driver.find_element(By.ID, "username").send_keys("invalid_user")
		driver.find_element(By.ID, "password").send_keys("wrong_password")
		driver.find_element(By.ID, "login-button").click()
		time.sleep(3)
		# protect against missing element
		try:
			error_displayed = driver.find_element(By.ID, "error-message").is_displayed()
		except Exception:
			error_displayed = False
		print("✅ Invalid Login Test Passed" if error_displayed else "❌ Invalid Login Failed")

	finally:
		driver.quit()


if __name__ == "__main__":
	main()
