import undetected_chromedriver as uc
from time import sleep
from selenium.webdriver.common.by import By

trendingNo_tup = ("१","२","३","४","५","६","७","८","९")

def ad_click():
    driver = uc.Chrome()
    driver.get('https://www.onlinekhabar.com/')
    sleep(6)
    driver.maximize_window()
    sleep(3)
    original_window_one = driver.current_window_handle
    #ambe steels
    driver.find_element(By.XPATH, "//body/div[@id='page']/div[@id='content']/section[1]/div[1]/div[1]").click()
    sleep(5)
    driver.switch_to.window(original_window_one)
    sleep(5)
    original_window_two = driver.current_window_handle
    print("Ambe done")
    #panchakanya
    driver.find_element(By.XPATH, "//a[@href='https://www.panchakanya.com/']").click()
    sleep(5)
    driver.switch_to.window(original_window_two)
    sleep(5)
    driver.find_element(By.ID, "_x31__px").click() #१
    sleep(3)
    print("panchakanya done")
    for single_trending in trendingNo_tup:
        x = single_trending
        driver.find_element(By.XPATH, "//span[text()='" + x +"']").click()
        sleep(7)
        original_window_three = driver.current_window_handle
        #shaurya_cements / riddhi_siddhi_cement
        driver.find_element(By.XPATH, "//a[@href='https://shauryacements.com/']//img").click()
        sleep(5)
        driver.switch_to.window(original_window_three)
        sleep(5)
        original_window_four = driver.current_window_handle
        print("riddhi siddhi done")
        #bajaj
        driver.find_element(By.XPATH, "//a[@href='https://bit.ly/Online-Khabar']//img").click()
        sleep(5)
        driver.switch_to.window(original_window_four)
        sleep(5)
        original_window_five = driver.current_window_handle
        sleep(5)
        driver.switch_to.window(original_window_five)
        sleep(5)
        original_window_six = driver.current_window_handle
        sleep(5)
        print("bajaj done")
        #ncell
        driver.find_element(By.XPATH, "//div[@class='okam-ad-position-wrap singlepage-abovemainphoto okam-device-desktop']").click()
        sleep(5)
        driver.switch_to.window(original_window_six)
        sleep(5)
        original_window_seven = driver.current_window_handle
        print("ncell done")
        #jagadamba
        driver.find_element(By.XPATH, "//a[@href='http://jagdambacement.com/']//img").click()
        sleep(5)
        driver.switch_to.window(original_window_seven)
        sleep(5)
        original_window_eight = driver.current_window_handle
        print("jagadamba done")
        #yamaha
        driver.find_element(By.XPATH, "//div[@class='ok18-single-post-content-wrap']//div[@id='okam-ad-82']").click()
        sleep(5)
        driver.switch_to.window(original_window_eight)
        sleep(5)
        print("yamaha done")
    driver.close
    sleep(5)        


if __name__ == '__main__':
    for _ in range(5):
        ad_click()

