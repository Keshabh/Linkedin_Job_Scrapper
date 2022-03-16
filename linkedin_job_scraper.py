from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # for implicit and explict waits
from selenium.webdriver.chrome.options import Options  # for suppressing the browser
import pandas as pd

option = webdriver.ChromeOptions()
option.add_argument('headless')
#driver = webdriver.Chrome('chromedriver.exe',options=option)


s=Service('chromedriver.exe')
browser = webdriver.Chrome(service=s,options=option)
url='https://www.linkedin.com'
browser.get(url)

username = browser.find_element(By.ID,"session_key")

linkedin_mail_id = input("Enter email: ")
password = input("Enter password: ")

username.send_keys(linkedin_mail_id)
password = browser.find_element(By.ID,"session_password")
password.send_keys(password)
login_button = browser.find_element(By.CLASS_NAME,"sign-in-form__submit-button")
login_button.click()

job_page_url = "https://www.linkedin.com/jobs/"
browser.get(job_page_url)

jobs = browser.find_elements(By.CLASS_NAME,"job-card-list__entity-lockup")
data=[]
for i in jobs:
    data.append(i.text)
print(data)
print("\n")
print(len(data))

jobs_info=[]
for i in (range(len(data))):
    data[i]=data[i].split("\n")
    jobs_info.append(data[i][:4])
print(jobs_info)

Role=[]
Company=[]
Location=[]
Remote=[]
for i in jobs_info:
    job_role,company_name,location,remote=i
    if remote.lower() not in ['remote','onsite','on-site','hybrid']:
        remote="Not specified"
    Role.append(job_role)
    Company.append(company_name)
    Location.append(location)
    Remote.append(remote)

#lets store this data in pandas dataframe.
columns=['JOB ROLE','COMPANY','LOCATION','REMOTE/ON-SITE']
data_frame = pd.DataFrame({"JOB ROLE":Role,"COMPANY":Company,"LOCATION":Location,"REMOTE/ON-SITE":Remote},index=None)

#data_frame.head()

path=r"C:\Users\DCQUASTER JACK\Desktop\linkedin_scrapped_jobs.csv"
#k=os.getcwd()+"\linkedin.csv"
#print(k)
data_frame.to_csv(path,index=False)
