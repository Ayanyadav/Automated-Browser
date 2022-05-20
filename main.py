import speech_recognition as sr
from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(r"C:\\Users\\asus\\PycharmProjects\\voice_automation\\venv\\sources\\chromedriver.exe")


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said= r.recognize_google(audio)

            print(said)
        except Exception as e:
            print("Exception:" + str(e))
    return said.capitalize()


text = get_audio()
while 'Exit' not in text:
    try:
        if "Search" in text:
            driver.get("https://www.google.com/")

            print("Search what")
            text = get_audio()
            search_bar = driver.find_element_by_name("q")
            search_bar.clear()
            search_bar.send_keys(text)
            search_bar.send_keys(Keys.RETURN)

            text = get_audio()
        if "Back" in text:
            driver.back()
            text = get_audio()
        if "Forward" in text:
            driver.forward()
            text = get_audio()
        if "Maximize" in text:
            driver.maximize_window()
        if "Minimize" in text:
            driver.minimize_window()
        if "Refresh" in text:
            driver.refresh()
            text = get_audio()
        if "Click" in text:
            print("click what")
            text = get_audio()
            driver.find_element_by_partial_link_text(text).click()
            text = get_audio()
        if "Input" in text:
            text = get_audio()
            search_bar = driver.find_element_by_tag_name("input").click()
            search_bar.clear()
            search_bar.send_keys(text)
            search_bar.send_keys(Keys.RETURN)

            text = get_audio()
        if "Down" in text:
            driver.execute_script('scroll(0,700)')
        if "Up" in text:
            driver.execute_script('scroll(0,-700)')

        else:
            print("its not working")
            text = get_audio()
    except Exception as e:
        print("Exception:" + str(e))

print('exiting')
