from selenium.webdriver.common.by import By
import undetected_chromedriver as uc

GOOGLE_LOGIN_URL = "https://accounts.google.com/signin"

def g_login(email, password):
    driver = uc.Chrome()
    driver.get(GOOGLE_LOGIN_URL)

    driver.implicitly_wait(10)

    email_input = driver.find_element(by=By.XPATH, value='//*[@id="identifierId"]')
    email_input.send_keys(email)

    e_next_button = driver.find_element(by=By.XPATH, value='//*[@id="identifierNext"]/div/button/span')
    e_next_button.click()

    password_input = driver.find_element(by=By.XPATH, value='//*[@id="password"]/div[1]/div/div[1]/input')
    password_input.send_keys(password)

    p_next_button = driver.find_element(by=By.XPATH, value='//*[@id="passwordNext"]/div/button/span')
    p_next_button.click()