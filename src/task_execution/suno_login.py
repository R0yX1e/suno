from selenium.webdriver.common.by import By
import undetected_chromedriver as uc

SUNO_URL = "https://app.suno.ai/"

def s_login():
    dirver = uc.Chrome()
    dirver.get(SUNO_URL)

    dirver.implicitly_wait(10)

    sign_up = dirver.find_element(by=By.XPATH, value='/html/body/div[1]/div[1]/nav/div[3]/div[3]/button')
    sign_up.click()

    g_sign_up = dirver.find_element(by=By.XPATH, value='//*[@id=":r2:"]/div/div/div/div/div[3]/div/button[2]')
    g_sign_up.click()
