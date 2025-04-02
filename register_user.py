from playwright.sync_api import sync_playwright
import logging
import re

lg = logging.basicConfig(filename="Register_user.log", level=logging.INFO, format="%(asctime)s : %(levelname)s : %(message)s")
lg = logging.getLogger(__name__)


lg.info("Starting Playwright with python script for Automation ter user action")

try:

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto('http://automationexercise.com')
        lg.info("Navigationg to URL https://automationexercise.com/")

        page.wait_for_timeout(3000)
        print(page.title())
        assert "Automation Exercise" in page.title(), "Sorry!Could not load the home page successfully"

        page.locator("a[href='/login']").click()
        lg.info("Clicking on Signup/Login button")

        assert page.locator('//h2[contains(text(),"New User Signup!")]').is_visible(), "New User SignUp is not visible"
        lg.info("Verifying New User Signup label is visible")

        Name = page.locator('input[name="name"]').fill('Abcd Efgh')
        lg.info("Entering the Name field in Home Page {Name}")

        Email = page.locator('input[data-qa="signup-email"]').fill("exmaple@gmail.com")
        lg.info("Entering email address field Home page {Email}")

        page.locator('button[data-qa="signup-button"]').click()
        lg.info("clicking on Signup Button")

        assert page.locator('//b[contains(text(),"Enter Account Information")]').is_visible(), "Label Enter Account Information in not visible"
        lg.info("Ensuring Enter Account Information Label is visible after entering Name and Email while user registration")

        Title = page.locator('input[value="Mr"]').click()
        lg.info("Entering the title field: {Title}")
        page.locator('input[data-qa="name"]').fill(Name)
        lg.info("Entering the Name filed in Account Creation page: {Name}")
        page.locator('input[data-qa="password"]').fill('123456')
        day = page.locator('//select[@name="days"]').select_option(index=28)
        lg.info("Entering the day value in DOB field: {day}")
        month = page.locator('//select[@data-qa="months"]').select_option(index=7)
        lg.info("Entering the month value in DOB field: {month} ")
        year = page.locator('//select[@data-qa="years"]').select_option(value=1992)
        lg.info("Entering the year value in DOB field: {year} ")
        page.locator('//label[contains(text(),"Sign up for")]').is_checked()
        lg.info("Checked In-- Sign up for our newsletter!")
        page.locator('//label[contains(text(),"Receive special")]').is_checked()
        lg.info("Checked In-- Receive special offers from our partners!")

        #Entering more details of user account related information 
        First_Name = page.locator('input[data-qa="first_name"]').fill("Abcd")
        lg.info("Entering first name field: {First_Name}")
        Last_Name = page.locator('input[data-qa="last_name"]').fill("Efgh")
        lg.info("Entering Last name field: {Last_Name}")
        company = page.locator('input[data-qa="company"]').fill("xyz Inc")
        lg.info("Entering the comapny  field: {company}")
        address = page.locator('input[data-qa="address"]').fill("6430 N Kedzie Ave")
        lg.info("Entering the address  field: {address}")
        address_Two = page.locator('input[data-qa="address2"]').fill("Near ...")
        lg.info("Entering the address Two field: {address_Two}")
        country = page.locator('//select[@name="country"]').select_option(value="United States")
        lg.info('Entering Country filed: {country}')
        state = page.locator('input[data-qa="state"]').fill("IL")
        lg.info("Entering State Field {state}")
        city = page.locator('input[data-qa="city"]').fill('Chicago')
        lg.info("Entering the city field: {city}")
        zipcode = page.locator('input[data-qa="zipcode"]').fill('60645')
        lg.info('Entering the zipcode filed {zipcode}')
        ph_number = page.locator('input[data-qa="mobile_number"]').fill('2644625542')
        lg.info('Entering Phone number field: {ph_number}')

        page.locator('button[data-qa="create-account"]').click()
        lg.info("Clicking on Create Account Button!!")

        assert page.locator('//h2[contains(text(),"Account Created")]').is_visible(), "Account Creation failed"

        page.wait_for_timeout(3000)

        browser.close()

    
except TimeoutError as e:
        lg.error(f"Timeout error occurred: {e}")
except AssertionError as e:
        lg.error(f"Assertion failed: {e}")
except Exception as e:
        lg.error(f"An unexpected error occurred: {e}")




    



    






    


    
    

    



    
