from selenium import webdriver
from selenium.webdriver.common.by import By
testlink = "https://www.amazon.in/War-Lanka-Ram-Chandra-Book/dp/9356291527/ref=zg_bs_books_sccl_1/258-9846763-6918247?pd_rd_i=9356291527&psc=1"
driver = webdriver.Chrome()
driver.get(testlink)
uls = driver.find_element(By.XPATH,'//*[@id="detailBullets_feature_div"]')
lis = uls.find_elements(By.TAG_NAME,'li')
for li in lis:
    #print(li.text)
    if 'Publisher' in li.text:
        with open ('sel.txt','a') as f:
            f.write(li.text)
            f.write('\n')
    if 'Language' in li.text:
        with open ('sel.txt','a') as f:
            f.write(li.text)
            f.write('\n')
    if 'Paperback' in li.text:
        with open ('sel.txt','a') as f:
            f.write(li.text)
            f.write('\n')
    if 'ISBN-10' in li.text:
        with open ('sel.txt','a') as f:
            f.write(li.text)
            f.write('\n')
    if 'ISBN-13' in li.text:
        with open ('sel.txt','a') as f:
            f.write(li.text)
            f.write('\n')
    if 'Item Weight' in li.text:
        with open ('sel.txt','a') as f:
            f.write(li.text)
            f.write('\n')
    if 'Dimensions' in li.text:
        with open ('sel.txt','a') as f:
            f.write(li.text)
            f.write('\n')
    

driver.close()
