"""Template robot with Python."""
from multiprocessing.connection import wait
from time import sleep
import pandas as pd
from RPA.Browser.Selenium import Selenium
web = Selenium()
excel_file= 'challenge.xlsx'

def opening_broweser():
    df = pd.read_excel(excel_file)
    web.open_available_browser("https://www.rpachallenge.com/")
    sleep(3)
    web.click_element_when_visible('//button[text()="Start"]')
    sleep(4)
    print(df)
    for index,row in df.iterrows():
        web.input_text('//input[@ng-reflect-name="labelFirstName"] ', row['First Name'])
        web.input_text('//input[@ng-reflect-name="lableLastName"]', row['Last Name'])
        web.input_text('//input[@ng-reflect-name="lableCompanyName"]', row['Company Name'])
        web.input_text('//input[@ng-reflect-name="lableRole"]', row['Role in Company'])
        web.input_text('//input[@ng-reflect-name="lableAddress"]', row['Address'])
        web.input_text('//input[@ng-reflect-name="lableEmail"]', row['Email'])
        web.input_text('//input[@ng-reflect-name="lablePhone"]', row['Phone Number'])
        web.click_button('//input[@value-"Submit"]')
        print("Sucessful")




def minimal_task():
    print("Done.")


if __name__ == "__main__":
    minimal_task()
    opening_broweser()
