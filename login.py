from selenium import webdriver
import time

def login(username, password):
    driver = webdriver.Chrome()
    driver.get('http://localhost:8080')

    login_button = driver.find_element_by_css_selector('a.button')
    login_button.click()

    username_input = driver.find_element_by_id('username')
    password_input = driver.find_element_by_id('password')

    username_input.send_keys(username)
    password_input.send_keys(password)

    submit_button = driver.find_element_by_css_selector('button[type="submit"]')
    submit_button.click()

    start_button = driver.find_element_by_css_selector('a.button[href="/standby"]')
    start_button.click()

    return driver

# ユーザー1からユーザー4までログインする
users = ['user1', 'user2', 'user3', 'user4']
drivers = []

for i, user in enumerate(users):
    driver = login(user, 'isdev')
    drivers.append(driver)

# ウィンドウサイズを取得
screen_width = driver.execute_script("return window.screen.width;")
screen_height = driver.execute_script("return window.screen.height;")

# ウィンドウを4分割して配置（中央に持ってくる）
for i, driver in enumerate(drivers):
    x = (i % 2) * (screen_width // 2)
    y = (i // 2) * (screen_height // 2)
    width = screen_width // 2
    height = screen_height // 2
    driver.set_window_position(x, y)
    driver.set_window_size(width, height)
    
