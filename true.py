from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


profile = webdriver.FirefoxProfile(r'C:\Users\<user_name>\AppData\Roaming\Mozilla\Firefox\Profiles\xxxxxx.default-release')
print(1)
profile.set_preference("dom.webdriver.enabled", False)
profile.set_preference('useAutomationExtension', False)
profile.update_preferences()
desired = DesiredCapabilities.FIREFOX
print(2)
driver = webdriver.Firefox(executable_path='./geckodriver.exe',firefox_profile=profile,desired_capabilities=desired)
print(3)

with open("file.txt","r") as f:
	for num in f:
		print(num)
		
		driver.get("https://www.truecaller.com/")
		print(4)
		print("No for which search is going on is : ",num)
		driver.find_element_by_css_selector('input.h-full').send_keys(num)
		driver.find_element_by_css_selector('.bg-brand').click()
		name = driver.find_element(By.CLASS_NAME,'font-montserrat text-lg sm:text-2xl flex-none').text
		address = driver.find_element(By.CLASS_NAME,'field__content')
		
		#writing text
		with open("data.txt","a") as file:
			file.write(f"\nOwner Detail : {num}, {name}, {address}")
			print("Appedned sucessfully.....")
