from django.http import HttpResponse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def fill_google_form(request):
    name = request.GET.get('name', 'Vivek')
    contact = request.GET.get('contact', '8360210146')
    address = request.GET.get('address', 'H-1687 Keshavpuram Kalyanpur')
    pin_code = request.GET.get('pin_code', '208017')
    dob = request.GET.get('dob', '04/03/2003')
    gender = request.GET.get('gender', 'Male')
    captcha_code = request.GET.get('captcha_code', 'GNFPYC')

    if not all([name, contact, address, pin_code, dob, gender, captcha_code]):
        return HttpResponse("Missing required parameters.", status=400)

    
    service = Service(executable_path=r"C:/chromedriver/chromedriver.exe") 
    driver = webdriver.Chrome(service=service)

    try:
        form_url = "https://docs.google.com/forms/d/e/1FAIpQLSdUCd3UWQ3VOgeg0ZzNeT-xzNawU8AJ7Xidml-w1vhfBcvBWQ/viewform"
        driver.get(form_url)

        
        WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '//input[@aria-label="Full Name"]')))

        
        driver.find_element("whsOnd.zHQkBf", '//input[@aria-label="Full Name"]').send_keys(name)
        driver.find_element("rFrNMe k3kHxc RdH0ib yqQS1 zKHdkd", '//input[@aria-label="Contact Number Write the 10 Digits only"]').send_keys(contact)
        driver.find_element("edhGSc zKHdkd kRy7qc RdH0ib yqQS1", '//input[@aria-label="Full Address"]').send_keys(address)
        driver.find_element("rFrNMe k3kHxc RdH0ib yqQS1 zKHdkd", '//input[@aria-label="Pin Code"]').send_keys(pin_code)
        driver.find_element("OabDMe cXrdqd Y2Zypf", '//input[@aria-label="Date Of Birth"]').send_keys(dob)
        driver.find_element("rFrNMe k3kHxc RdH0ib yqQS1 zKHdkd", '//input[@aria-label="Gender"]').send_keys(gender)
        driver.find_element("rFrNMe k3kHxc RdH0ib yqQS1 zKHdkd", '//input[@aria-label="Type this code: GNFPYC This code is to verify you are a human. Protected by xfanatical."]').send_keys(captcha_code)

    
        driver.find_element("uArJ5e UQuaGc Y5sE8d VkkpIf QvWxOd", '//span[text()="Submit"]').click()

        time.sleep(3)
        driver.save_screenshot('form_submission_confirmation.png')  

        message = "Form submitted successfully and screenshot saved."

    except Exception as e:
        message = f"An error occurred: {e}"
        print(f"Error: {e}")  

    finally:
        driver.quit()  

    return HttpResponse(message)

