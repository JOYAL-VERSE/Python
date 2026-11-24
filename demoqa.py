
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch browser
driver = webdriver.Chrome()

# Open DemoQA website
driver.get("https://demoqa.com/text-box")
driver.maximize_window()

# Enter user details
driver.find_element(By.ID, "userName").send_keys("Krishna Priya")
driver.find_element(By.ID, "userEmail").send_keys("krishna@gmail.com")
driver.find_element(By.ID, "currentAddress").send_keys("Thrissur, Kerala")
driver.find_element(By.ID, "permanentAddress").send_keys("Irinjalakuda, Kerala")

# Submit the form
driver.find_element(By.ID, "submit").click()

time.sleep(2)

# Verify entered details
output = driver.find_element(By.ID, "output").text

if ("Krishna Priya" in output and
    "krishna@gmail.com" in output and
    "Thrissur, Kerala" in output and
    "Irinjalakuda, Kerala" in output):

    print("All details verified successfully!")
else:
    print("Verification failed!")

# Close browser
driver.quit()
