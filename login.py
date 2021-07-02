from playwright.sync_api import sync_playwright
import playwright
import pickle
from bs4 import BeautifulSoup
import time


portal_link = 'https://www.upwork.com/ab/account-security/login'
username = ''
password = ''
secret = ''

with sync_playwright() as p:
    browser = p.firefox.launch(headless=False, slow_mo=200)
    page = browser.new_page()
    page.goto('https://www.upwork.com/ab/account-security/login')
    #page.screenshot(path=f'upwork.png')
    #<button data-v-0c7bde74="" data-v-733406b2="" id="login_password_continue"/button>

    page.fill('#login_username', username)
    page.click('#login_password_continue')

    page.fill('#login_password', password)
    page.click('#login_control_continue')

    try:
        #page.wait_for_selector("text=Let's make sure it's you", timeout=5)
        #print("2")
        page.fill('#login_answer', secret)
        #print("3")
        page.click('#login_control_continue')
        #print("4")
        #page.wait_for_timeout(1000)
        #print(page.content())
    except playwright._impl._api_types.TimeoutError:
        #page.screenshot(path=f'upwork.png')
        print("Errror")
    except:
        print("Something else went wrong")

    #print("5")
    start_page = page.content()

    filehandler = open(b"mainpage.obj","wb")
    pickle.dump(start_page,filehandler)
    filehandler.close()

    print("Sleeping")
    time.sleep(5)

    main_page = BeautifulSoup(start_page,'html.parser')

    job_link = main_page.findAll('a', {'class':'job-title-link break visited ng-binding'})
    print(job_link[0].prettify())

    if job_link[0].has_attr('href'):
        half_link = job_link[0]['href']
        print(half_link)
        print("*****")
        job_page_link = "https://upwork.com" + half_link
        print(job_page_link)
        page.goto(job_page_link, wait_until="networkidle")
        
        job_page = page.content()
        #filehandler2 = open(b"job.obj","wb")
        #pickle.dump(job_page,filehandler2)
        #filehandler2.close()
        page.go_back(wait_until="networkidle")
    

    #main_page = BeautifulSoup(current_page,'html.parser')
    page.screenshot(path=f'main.png')
    #print(main_page.prettify())
    browser.close()
