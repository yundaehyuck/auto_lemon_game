from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# 웹 드라이버 실행 (Chrome 기준)
driver = webdriver.Chrome()
driver.get("https://wwme.kr/lemon/ashley-play")  # 원하는 웹사이트 URL

# XPath를 사용하여 버튼 요소 찾기
button = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/div/main/div[2]/div[2]/div[1]/div/div[2]/button/span[2]")

# 버튼 클릭
button.click()
time.sleep(3)

def detect():

    elements = driver.find_elements(By.CLASS_NAME, "cell")

    maps = [[0]*17 for _ in range(10)]

    i = 0
    j = 0

    for elem in elements:

        x = elem.text

        if x.isdigit():

            maps[i][j] = int(x)
        
        j += 1

        if j == 17:

            i += 1
            j = 0
    
    return maps


def cal(x,y,z,w):

    a,b = min(x,z),max(x,z)
    c,d = min(y,w),max(y,w)

    v = 0

    for i in range(a,b+1):

        for j in range(c,d+1):

            if i >= 0 and i <= 16 and j >= 0 and j <= 9:

                v += maps[j][i]
            
            else:

                return -1
    
    return v

def find():

    for y in range(10):

        for x in range(17):
            
            #시작좌표 (x,y)

            for j in range(10):

                for i in range(17):

                    dx = x + i
                    dy = y + j

                    v = cal(x,y,dx,dy)

                    if v > 10:

                        break

                    elif v == 10:

                        return x,y,dx,dy
                    
                    elif v == -1:
                        
                        break

            
            for j in range(10):

                for i in range(17):

                    dx = x - i
                    dy = y + j

                    v = cal(x,y,dx,dy)

                    if v > 10:

                        break

                    elif v == 10:

                        return x,y,dx,dy
                    
                    elif v == -1:
                        
                        break
            
            
            
            for j in range(10):

                for i in range(17):

                    dx = x + i
                    dy = y - j

                    v = cal(x,y,dx,dy)

                    if v > 10:

                        break

                    elif v == 10:

                        return x,y,dx,dy
                    
                    elif v == -1:
                        
                        break
            
            
            for j in range(10):

                for i in range(17):

                    dx = x - i
                    dy = y - j

                    v = cal(x,y,dx,dy)

                    if v > 10:

                        break

                    elif v == 10:

                        return x,y,dx,dy
                    
                    elif v == -1:
                        
                        break
    
    return -1,-1,-1,-1
            

maps = detect()
now = 0

while 1:

    x,y,z,w = find()

    if x == -1 and y == -1 and z == -1 and w == -1:

        t = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/main/div/main/div[2]/div[1]/div/div[1]/span[2]").text

        if t == now:

            break
    
        maps = detect()
        now = t
        continue

    xpath1 = f'/html/body/div[1]/div[1]/main/div/main/div[2]/div[2]/div/div[{y+1}]/div[{x+1}]'
    start_element = driver.find_element(By.XPATH, xpath1)

    xpath2 = f'/html/body/div[1]/div[1]/main/div/main/div[2]/div[2]/div/div[{w+1}]/div[{z+1}]'
    end_element = driver.find_element(By.XPATH, xpath2)

    action = ActionChains(driver)
    action.click_and_hold(start_element).move_to_element(end_element).release().perform()

    for i in range(x,z+1):

        for j in range(y,w+1):

            maps[j][i] = 0
