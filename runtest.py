from selenium import webdriver
from testpage import *

def start_test():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get("https://netpeak.ua")
    driver.get("https://career.netpeak.group")
    driver.get("https://career.netpeak.group/hiring")
    start_test_form = Netpeak(driver)
    start_test_form.input_png_file()
    start_test_form.form()
    start_test_form.check_error_color()
    start_test_form.courses()
    driver.quit()
    
if __name__ == "__main__":
    start_test()