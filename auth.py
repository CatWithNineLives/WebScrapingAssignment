
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import json
import datetime
import time

url="https://parivahan.gov.in/rcdlstatus/?pur_cd=101"
DRIVER_PATH=r"C:\Users\Josh\Desktop\SurePassAssignment\chromedriver.exe"

driver=webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get(url)
#wait for the browser to fully load
driver.implicitly_wait(30)

# license_input=
# dob_input=driver.find_element_by_xpath('/html/body/form/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[3]/span/input')
# captcha_input=driver.find_element_by_xpath('/html/body/form/div[1]/div[3]/div[1]/div/div[2]/div[3]/div/div[2]/div/div[2]/table/tbody/tr/td[3]/input')
# check_button=driver.find_element_by_xpath('/html/body/form/div[1]/div[3]/div[1]/div/div[2]/div[4]/div/button[1]/span')
# reset_button=driver.find_element_by_xpath('/html/body/form/div[1]/div[3]/div[1]/div/div[2]/div[4]/div/button[2]')

license="DL-0420110149646"
dob="09-02-1976"
captcha_text=""
field_names=["Driver's License No.","Date Of Birth"]
values=[]


# def validate_input(drivers_license,dateofbirth):
#     #validate license
#     if(len(drivers_license)!=16):
#         return False
#     if(not drivers_license[0:2].isalpha()):
#         return False
#     if(drivers_license[2]!='-' and  drivers_license[4]!=' '):    
#         return False
#     if(not drivers_license[3:].isdigit() and not drivers_license[5:].isdigit()):
#         return False
#     global license
#     license=drivers_license
    
#     #validate date 
#     try:     
#         DOB=datetime.datetime(int(dateofbirth[6:10]),int(dateofbirth[3:5]),int(dateofbirth[:2]))    
#     except ValueError:
#         return False
#     global dob    
#     dob=dateofbirth
#     return True     #valid input   

def take_input():
    # drivers_license=input("Enter the Driver's License No. The format is SS-RRYYYYNNNNNNN or SSRR YYYYNNNNNNN. \n Where : SS- Two character state code,\n RR- RTO,\n YYYY- year and NNNNNNN digits. : ")
    # dateofbirth=input("Enter date of birth DD-MM-YYYY : ")
    # if(not validate_input(drivers_license,dateofbirth)):
    #     print("Incorrect format of input")
    #     return False
    return True

# def test_valid():
#     #valid license details
#     license="DL-0420110149646"
#     dob="09-02-1976"

# def test_invalid():
#     #invalid license details
#     license="YY-1020150363697"
#     dob="28-01-1996"

def get_captcha():
    #driver.implicitly_wait(10)
    #input captcha text
    global captcha_text
    captcha_text=input('Input captcha text : ')

def input_captcha():
    #driver.implicitly_wait(30)
    driver.find_element_by_xpath("//*[@id='form_rcdl:j_idt32:CaptchaID']").clear()
    print("cleared captcha")
    time.sleep(10)
    driver.find_element_by_xpath("//*[@id='form_rcdl:j_idt32:CaptchaID']").send_keys(captcha_text)
    print("filled captcha")

# def check_exists_by_id(id):
#     try:
#         driver.find_element_by_id(id)
#     except NoSuchElementException:
#         return False
    
#     return True

def check_exists_by_xpath(xpath):
    print("Inside check exists xpath",xpath)
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        print("No such element exception")
        return False
    return True


def form_input():
    driver.find_element_by_xpath("//*[@id='form_rcdl:tf_dlNO']").send_keys(license)
    print("Filled license")
    driver.find_element_by_xpath("//*[@id='form_rcdl:tf_dob_input']").send_keys(dob)
    print("Filled dob")
    driver.find_element_by_xpath("//*[@id='form_rcdl:j_idt32:CaptchaID']").send_keys(captcha_text)
    print("Filled captcha")
    driver.find_element_by_xpath("//*[@id='form_rcdl:j_idt43']").click()
    print("clicked on check status")
    
def form_output():
    #details of driving license table
    details_driving_license=driver.find_element_by_xpath('/html/body/form/div[1]/div[3]/div[1]/div/div[2]/div[4]/span/div/div/div/div/div/table[1]/tbody')
    data1=[]
    table1_data_rows=details_driving_license.find_elements_by_tag_name("tr")

    #information from table1
    for tr in table1_data_rows:
        for td in tr.find_elements_by_tag_name("td"):
            data1.append(td.text)


    #alternate values of rows are field names and their values, saving in an array
    for i in range(0,len(data1),2):
        field_names.append(data1[i])
    for i in range(1,len(data1),2):
        values.append(data1[i])

    driving_license_validity1=driver.find_element_by_xpath('/html/body/form/div[1]/div[3]/div[1]/div/div[2]/div[4]/span/div/div/div/div/div/table[2]/tbody')
    data2=[]
    table2_data_rows=driving_license_validity1.find_elements_by_tag_name("tr")

    for tr in table2_data_rows:
        for td in tr.find_elements_by_tag_name("td"):
            data2.append(td.text)

    driving_license_validity2=driver.find_element_by_xpath('/html/body/form/div[1]/div[3]/div[1]/div/div[2]/div[4]/span/div/div/div/div/div/table[3]/tbody/tr')
    for td in driving_license_validity2.find_elements_by_tag_name("td"):
            data2.append(td.text)
    
    indices=[0,3,6,8]
    for i in indices:
        field_names.append(data2[i])
    values.append([data2[1],data2[2]]) #two lists as values for field_names 'Non-Transport' and 'Transport'
    values.append([data2[4],data2[5]])
    values.append(data2[7])
    values.append(data2[9])


    vehicle_details_headings=driver.find_element_by_xpath('/html/body/form/div[1]/div[3]/div[1]/div/div[2]/div[4]/span/div/div/div/div/div/div[4]/div/table/thead/tr').find_elements_by_tag_name('th')
    headings2=[]
    #table3_data_rows=details_driving_license.find_elements_by_tag_name("tr")

    #information from table3

    for th in vehicle_details_headings:
        headings2.append(th.text)
        field_names.append(th.text)
    #print(headings2)
    
    vehicle_details=driver.find_element_by_xpath('/html/body/form/div[1]/div[3]/div[1]/div/div[2]/div[4]/span/div/div/div/div/div/div[4]/div/table/tbody/tr').find_elements_by_tag_name('td')
    data3=[]
    for td in vehicle_details:
        data3.append(td.text)
        values.append(td.text)
        


#test_valid()


#validation of captcha text
#check if element with error message is present
#xpath1='/html/body/form/div[1]/div[3]/div[1]/div/div[2]/div[1]/div' #incorrect captcha error message
xpath1='//*[@id="form_rcdl:j_idt13"]/div/ul/li/span[1]'
xpath2='/html/body/div[3]'                                          #no DL details error message
#driver.implicitly_wait(10)

condition=True
while(condition):
    if(take_input()):
        values=[license,dob]
        get_captcha()                                               #get captcha from user
        form_input()                                                #fill the form
        #driver.implicitly_wait(40)
        error_message_exists=check_exists_by_xpath(xpath1)
        print("error1",error_message_exists)        
        
        '''if(not error_message_exists):
            form_output()                                           #scrape the form's output from the webpage
            output=dict(zip(field_names,values))
            print(output)
        '''
        while(error_message_exists):                                #error message exists, incorrect captcha take value again   
            print("ERROR : Incorrect captcha!!")
            get_captcha()
            time.sleep(10)
            input_captcha()
            if(error_message_exists):
                print("Error message before clicking")
            driver.find_element_by_xpath('//*[@id="form_rcdl:j_idt43"]').click()   #clicking on check status button
            print("clicked on check status")
            try:    
                form_output()                                           #scrape the form's output from the webpage
                output=dict(zip(field_names,values))
                print(output)
            except NoSuchElementException:
                print("No such element exception inside loop for table")
            #tic=time.time()
            #driver.implicitly_wait(60)                                             #waiting for page to load
            #toc=time.time()
            #print("time elapsed", (toc-tic))

            #xpath1='/html/body/form/div[1]/div[3]/div[1]/div/div[2]/div[1]/div/ul/li/span[1]' 
            error_message_exists=check_exists_by_xpath(xpath1)
            
            print("Does error message exist? ",error_message_exists)
        
        '''
        form_output()                                           #scrape the form's output from the webpage
        output=dict(zip(field_names,values))
        print(output)

        with open("output_table.json","w") as outfile:
            json.dump(output,outfile)
        '''
        
        
        error_message_exists=check_exists_by_xpath(xpath2)
        print("DL error ",error_message_exists) 
        if(not error_message_exists):              
            form_output()                                           #scrape the form's output from the webpage
            output=dict(zip(field_names,values))
            print(output)

            with open("output_table.json","w") as outfile:
                json.dump(output,outfile)

        else:                                                       #error message exists 'No DL details found'
            print("ERROR : No DL details found!!")
            #if no DL details were found then the reset button is not clickable! First need to exit the no DL details dialog box button.
            xpath3="//*[@id='primefacesmessagedlg']/div[1]/a"
            driver.find_element_by_xpath(xpath3).click()    
        

    choice=input('Press 1 if you want to continue, anything else if not. : ')
    if(choice=='1'):
        condition=True
        #driver.implicitly_wait(10)
        driver.find_element_by_xpath("//*[@id='form_rcdl:rest_bt']").click()    #reset
        
    else:
        print('Exitting')
        condition=False
    
                