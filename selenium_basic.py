from selenium import webdriver
driver = webdriver.Chrome(executable_path="c:/selenium/chromedriver.exe")
driver.get("https://www.seleniumeasy.com/test/bootstrap-alert-messages-demo.html")
assert "Selenium" in driver.title
elem = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[1]/button[2]')
elem.click()
assert 'normal success message' in driver.page_source
driver.close()
