from bs4 import BeautifulSoup
import requests
httpLink = "http://www.amazon.in/War-Lanka-Ram-Chandra-Book/dp/9356291527/ref=zg_bs_books_sccl_1/258-9846763-6918247?pd_rd_i=9356291527&psc=1"
httpsLink = "https://www.amazon.in/War-Lanka-Ram-Chandra-Book/dp/9356291527/ref=zg_bs_books_sccl_1/258-9846763-6918247?pd_rd_i=9356291527&psc=1"

def getSoup(link):
    f = requests.get(link)
    soup = BeautifulSoup(f.content, 'html.parser')
    return soup

def writeFile(soup, filename):
    with open (filename, "w", encoding='utf-8') as f:
        f.write(soup.prettify())



if __name__ == '__main__':
    soup = getSoup(httpsLink)
    writeFile(soup, "https.html")
    uls = soup.find_all("ul", class_="a-unordered-list a-nostyle a-vertical a-spacing-none detail-bullet-list")
    for ul in uls:
        lis = ul.find_all("li")
        for li in lis:
            #print(li.text)
            
            if 'Publisher' in li.text:
                with open ('bs4.txt','a', encoding='utf-8') as f:
                    f.write(li.text)
                    f.write('\n')
            if 'Language' in li.text:
                with open ('bs4.txt','a',encoding='utf-8') as f:
                    f.write(li.text)
                    f.write('\n')
            if 'Paperback' in li.text:
                with open('bs4.txt','a',encoding='utf-8') as f:
                    f.write(li.text)
                    f.write('\n')
            if 'ISBN-10' in li.text:
                with open ('bs4.txt','a',encoding='utf-8') as f:
                    f.write(li.text)
                    f.write('\n')
            if 'ISBN-13' in li.text:
                with open ('bs4.txt','a', encoding='utf-8') as f:
                    f.write(li.text)
                    f.write('\n')
            if 'Item Weight' in li.text:
                with open ('bs4.txt','a',encoding='utf-8') as f:
                    f.write(li.text)
                    f.write('\n')
            if 'Dimensions' in li.text:
                with open ('bs4.txt','a',encoding='utf-8') as f:
                    f.write(li.text)
                    f.write('\n')
