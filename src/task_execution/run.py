from selenium.webdriver.common.by import By

class login:
    def __init__(self,driver) -> None:
        self.driver = driver

    def s_login(self):
        self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[1]/nav/div[3]/div[3]/button').click()
        
        self.driver.find_element(by=By.XPATH, value='//*[@id=":r2:"]/div/div/div/div/div[3]/div/button[2]').click()

    def g_login(self,email, password):
        self.driver.find_element(by=By.XPATH, value='//*[@id="identifierId"]').send_keys(email)
        
        self.driver.find_element(by=By.XPATH, value='//*[@id="identifierNext"]/div/button/span').click()
        
        self.driver.find_element(by=By.XPATH, value='//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
        
        self.driver.find_element(by=By.XPATH, value='//*[@id="passwordNext"]/div/button/span').click()


class create:
    def __init__(self,driver) -> None:
        self.driver = driver

    def create_song(self,custom_mode, key, style=None, title=None):
        if custom_mode:
            self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[1]/div/div/div/div[1]/div[2]/div/div[1]/div[2]/textarea').send_keys(key)

            if style != None:
                self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[1]/div/div/div/div[1]/div[2]/div/div[2]/textarea').send_keys(style)
            if title != None:
                self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[1]/div/div/div/div[1]/div[2]/div/div[3]/input').send_keys(title)
        else:
            self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[1]/div/div/div/div[1]/div[2]/div[2]/textarea').send_keys(key)