from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import csv 
import time
import pyautogui

username = ""
passwrod = ""
Phone_Number = ''
file_path = r""

all_table_data = []
outputfile = "attendance..csv"
# Create a new Options object
chrome_options = Options()

# Add an argument to set the logging level
# Level 3 will suppress most informational messages and warnings
chrome_options.add_argument("--log-level=3")

# Initialize the Chrome driver with the specified options
driver = webdriver.Chrome(options=chrome_options)

#website


driver.get("https://mujslcm.jaipur.manipal.edu/Home/Index")
assert "Manipal University" in driver.title
#username and password


username_field = driver.find_element(By.ID, "txtUserName")
password_field = driver.find_element(By.NAME, "Password")
username_field.send_keys(username)
password_field.send_keys(passwrod)
#sign in
time.sleep(1)

signin_field = driver.find_element(By.ID, "login_submitStudent")
signin_field.click()
time.sleep(1)

#attandance 
reports_fiels = driver.find_element(By.LINK_TEXT,"Reports").click()

time.sleep(2)
attdance = driver.find_element(By.LINK_TEXT,"Attendance Summary").click()


time.sleep(10)
#data to be collected 
try:
    table = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "kt_ViewTable")))

    rows = table.find_elements(By.TAG_NAME, "tr")

    for i, row in enumerate(rows):
            # 4. Find all cells (both headers <th> and data <td>) in the current row
            # Using XPath is robust for finding either tag.
            cells = row.find_elements(By.XPATH, ".//th | .//td")
            
            # 5. Get the text from each cell. Selenium's .text will get the content 
            # from the nested <span> tag automatically.
            row_data = [cell.text.strip() for cell in cells]
            
            # Only add non-empty rows to our final list
            if any(row_data):
                filtered_row = [row_data[0], row_data[1], row_data[-1]]
                all_table_data.append(filtered_row)
                print(f"{row_data[0]}: {row_data[1]} : attdance in  % : {row_data[-1]}")
except Exception as e:
     print(f"An error occurred: {e}")

try:
        with open(outputfile,mode='w',newline='',encoding='utf-8') as file:
             writer = csv.writer(file)
             writer.writerows(all_table_data)
except Exception as e:
        print(f"Error saving file: {e}")

time.sleep(2)
driver.close()
time.sleep(3)

#whatsapp

pyautogui.hotkey('winleft')

pyautogui.typewrite('Google Crome\n',0.2)
time.sleep(1)
pyautogui.hotkey('winleft', 'up')
time.sleep(2)

pyautogui.typewrite('https://web.whatsapp.com/\n',0.1)
time.sleep(30)

try:
      pyautogui.click(x=250,y=222,button='left')
except:
       pyautogui.click(pyautogui.locateCenterOnScreen('slcm.PNG'))

time.sleep(2)
pyautogui.typewrite(Phone_Number)

time.sleep(2)
pyautogui.click(x=305,y=449,button='left')

#attach icon
time.sleep(3)
pyautogui.click(x=695,y=983,button='left')
time.sleep(2)

#doucument
pyautogui.click(x=703,y=555,button='left')
time.sleep(2)

#file selection
pyautogui.write(file_path)
time.sleep(2)

#to send the file 
try:
     pyautogui.click(x=765,y=563,button='left')
except:
      print('hello') 
time.sleep(2)


pyautogui.typewrite(str(datetime.datetime.now().date()))

pyautogui.press("enter") 

time.sleep(3)
# closing the browser 

pyautogui.hotkey('ctrl', 'shift', 'w')

