from selenium import webdriver as wd

browser = wd.Chrome()
browser.get('https://google.com')

print(browser.page_source)
