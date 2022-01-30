from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')
chrome_options.add_argument("disable-gpu")
s = Service('chromedriver.exe')
driver = webdriver.Chrome(service=s, options=chrome_options)
url='https://www.powerlanguage.co.uk/wordle/'
driver.get(url)
scriptArray="return Array.apply(0, new Array(localStorage.length)).map(function (o, i) { return localStorage.getItem(localStorage.key(i));})"
result = driver.execute_script(scriptArray)
s = result
ans = s[0][105]+s[0][106]+s[0][107]+s[0][108]+s[0][109]
driver.close();
print(ans)
input("Press any key to exit: ")
