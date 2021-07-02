import pickle
from bs4 import BeautifulSoup


ff = open("mainpage.obj",'rb')
mainpage = pickle.load(ff)
ff.close()


main_page = BeautifulSoup(mainpage,'html.parser')
#print(main_page.prettify())
#print(main_page.html.body)

#tag = main_page.find_all("section")#, class_="sister")W

total_jobs = main_page.findAll('section')

#print(total_jobs[5].prettify())
print(total_jobs[1].findAll('h4', {'class':'job-title m-0 p-sm-right ng-isolate-scope'})[0].text.strip(" \n\t\r").encode('utf-8'))

job_type = total_jobs[5].findAll('strong', {'class':'js-type'})[0].text.strip(" \n\t\r")
print(job_type)

job_level = total_jobs[5].findAll('span', {'class':'js-contractor-tier'})[0].text.strip(" - \n\t\r")
print(job_level)

job_budget = total_jobs[5].findAll('span', {'class':'js-budget'})[0].text.strip(" -  \n\t\r")

print(job_budget)

#job_estimated_time = total_jobs[5].findAll('span', {'class':'js-duration'})[0].text.strip("Est. Time -  : \n\t\r ")

#print(job_estimated_time)

job_country = total_jobs[5].findAll('strong', {'class':'text-muted client-location ng-binding'})[0].text
print(job_country)



ff2 = open("job.obj",'rb')
job = pickle.load(ff2)
ff2.close()

jj_page = BeautifulSoup(job,'html.parser')
#print(jj_page.prettify())

job_detail = jj_page.findAll('div', {'class':'job-description break mb-0'})[0].text
print(job_detail)

try:
    job_skill = jj_page.findAll('a', {'class':'cfe-ui-job-skill up-skill-badge m-0-left m-0-top m-xs-bottom'})
    skills = [skill.text for skill in job_skill]
    print(skills)
except:
    job_skill = "No Data"