import undetected_chromedriver as uc

driver = uc.Chrome(use_subprocess=True)
driver.get('https://www.pdfdrive.com/')



text_ = driver.find_elements('xpath', '//p')

print(text_.text)