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
    driver.find_element(By.ID, "_x31__px").click() #१
    sleep(3)
    for single_trending in trendingNo_tup:
        x = single_trending
        driver.find_element(By.XPATH, "//span[text()='" + x +"']").click()
        sleep(7)
        original_window_eight = driver.current_window_handle
        #yamaha
        driver.find_element(By.XPATH, "//div[@class='ok18-single-post-content-wrap']//div[@id='okam-ad-82']").click()
        sleep(5)
        driver.switch_to.window(original_window_eight)
        sleep(5)
        driver.close()        


if __name__ == '__main__':
    for _ in range(5):
        ad_click()
