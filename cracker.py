import random
import pyautogui #creates a graphical user interface to input password

#chars below can be edited to extend the range of characters

chars = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
#convert string of characters into list
char = list(chars)

pwd = pyautogui.password("Enter Password:")
sample_pwd = ""

while sample_pwd != pwd:
    sample_pwd = random.choices(char, k=len(pwd))
    print("<====" + str(sample_pwd) + "<====")
    if sample_pwd == list(pwd):
        print("The password is " + "".join(sample_pwd))
        break
