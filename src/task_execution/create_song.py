from selenium.webdriver.common.by import By
import undetected_chromedriver as uc

SUNO_URL = "https://app.suno.ai/create/"

def create_song(custom_mode, key, style=None, title=None):

    driver = uc.Chrome()
    driver.get(SUNO_URL)
    driver.implicitly_wait(10)

    if custom_mode:
        lyrics = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[1]/div/div/div/div[1]/div[2]/div/div[1]/div[2]/textarea')
        lyrics.send_keys(key)

        if style != None:
            driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[1]/div/div/div/div[1]/div[2]/div/div[2]/textarea').send_keys(style)
        if title != None:
            driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[1]/div/div/div/div[1]/div[2]/div/div[3]/input').send_keys(title)
    else:
        driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[1]/div/div/div/div[1]/div[2]/div[2]/textarea').send_keys(key)
