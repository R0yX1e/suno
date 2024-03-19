import csv
from execution.selenium_suno import Login
import undetected_chromedriver as uc

async def start_chrome():
    with open('account.csv', 'r') as csvfile:
        account_list = list(csv.reader(csvfile))

    for account in account_list:
        driver = uc.Chrome()
        driver.implicitly_wait(10)
        await driver.get('https://accounts.google.com/signin')
        await Login(driver).g_login(account[0],account[1])

async def loop_task():
    pass