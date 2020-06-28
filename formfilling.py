import requests
from bs4 import BeautifulSoup

url="https://parivahan.gov.in/rcdlstatus/?pur_cd=101"

html_content=requests.get(url).text
soup=BeautifulSoup(html_content,"lxml")
#print(soup.prettify())

#name of headings
headings=[]
headings.append(soup.find("label",attrs={"id":"form_rcdl:j_idt17"}).text)
headings.append(soup.find("label",attrs={"id":"form_rcdl:j_idt22"}).text)
headings.append(soup.find("label",attrs={"id":"form_rcdl:j_idt32:j_idt35"}).text)
print(headings)

#scrape captcha image by id
image=soup.find("img",attrs={"id":"form_rcdl:j_idt32:j_idt38"})


#input1=soup.find("input", attrs={"id":"form_rcdl:tf_dlNO"})
