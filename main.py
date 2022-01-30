from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')
chrome_options.add_argument("disable-gpu")
driver = webdriver.Chrome(executable_path= r'chromedriver.exe', options=chrome_options)
url='https://www.powerlanguage.co.uk/wordle/'
driver.get(url)
scriptArray="return Array.apply(0, new Array(localStorage.length)).map(function (o, i) { return localStorage.getItem(localStorage.key(i));})"
result = driver.execute_script(scriptArray)
s = result
ans = s[0][105]+s[0][106]+s[0][107]+s[0][108]+s[0][109]
print(ans)