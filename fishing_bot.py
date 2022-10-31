import time
import pyautogui
import cv2 as cv


def main():
    countdown()
    # stronghold_routine()
    start_fishing()


def countdown():
    cd = range(0, 5)
    for i in cd:
        print(len(cd) - i)
        time.sleep(1)
    print("Start")


def start_fishing():
    # set life energy, may be implemented through input
    energy = 7400
    # set durabiloty
    d = 100
    # calculate how many trys to do from energy
    trys = round(energy / 60)
    # change to fishing tool, if its not on screen
    if not pyautogui.locateOnScreen("images/AngelSymbol.png", confidence=0.6):
        pyautogui.keyDown('B')
        pyautogui.keyUp('B')
        time.sleep(10)
    # move to location and start fishing by pressing "E"
    pyautogui.moveTo(955, 819)
    time.sleep(10)
    pyautogui.keyDown('E')
    pyautogui.keyUp('E')
    i = 0
    j = 0
    # search screen until image was found
    while i in range(trys):
        if pyautogui.locateOnScreen("images/Ausrufezeichen.png", confidence=0.6):
            # x1, y1 = pyautogui.center(pyautogui.locateOnScreen("images/Ausrufezeichen.png", confidence=0.6))
            i = i + 1
            j = 0
            pyautogui.keyDown('E')
            pyautogui.keyUp('E')
            pyautogui.sleep(10)
            #print(str(i +1) + ". try")
            if i % d == 0:
                print(str(i) + '. try, durability limit reached, go to stronghold')
                go_repair()
                pyautogui.moveTo(955, 819)
                pyautogui.sleep(10)
                pyautogui.keyDown('B')
                pyautogui.keyUp('B')
                time.sleep(10)
            pyautogui.keyDown('E')
            pyautogui.keyUp('E')
            time.sleep(10)
        print("j :", j)
        print("i: ", i)
        j = j + 1
        if j > 60:
            pyautogui.keyDown('E')
            pyautogui.keyUp('E')
            time.sleep(10)
            j = 0


def go_repair():
    # go to stronghold
    pyautogui.keyDown('9')
    pyautogui.keyUp('9')
    time.sleep(60)
    # open menu and repair
    pyautogui.hotkey('ctrl', '1')
    time.sleep(20)
    pyautogui.click(231, 271)
    time.sleep(20)
    pyautogui.click(196, 353)
    time.sleep(20)
    pyautogui.click(1285, 927)
    time.sleep(20)
    pyautogui.click(725, 820)
    time.sleep(20)
    pyautogui.doubleClick(905, 645, interval=4)
    time.sleep(10)
    # quit menus
    for j in range(3):
        pyautogui.keyDown('esc')
        pyautogui.keyUp('esc')
        time.sleep(10)
    # go back to world
    pyautogui.keyDown('8')
    pyautogui.keyUp('8')
    time.sleep(120)


def stronghold_routine():
    # go to stronghold
    pyautogui.keyDown('9')
    pyautogui.keyUp('9')
    time.sleep(45)
    # open menu
    pyautogui.hotkey('ctrl', '1')
    time.sleep(10)
    do_port_stuff()
    do_farm_stuff()
    # close menu
    pyautogui.keyDown('esc')
    pyautogui.keyUp('esc')
    time.sleep(10)
    # go back to world
    pyautogui.keyDown('8')
    pyautogui.keyUp('8')
    time.sleep(45)


def do_port_stuff():
    # go to port
    pyautogui.click(169, 274)
    time.sleep(10)
    # collect normal missions
    pyautogui.click(195, 356)
    time.sleep(20)
    for i in range(2):
        pyautogui.click(650, 356)
        time.sleep(10)
        pyautogui.click(1677, 804)
        time.sleep(10)
        pyautogui.click(953, 729)
        time.sleep(10)
        pyautogui.click(953, 729)
    # send firt ship
    pyautogui.click(650, 356)
    time.sleep(10)
    pyautogui.click(1677, 804)
    time.sleep(10)
    pyautogui.click(910, 629)
    time.sleep(10)
    # send snd ship
    pyautogui.click(673, 429)
    time.sleep(10)
    pyautogui.click(1677, 804)
    time.sleep(10)
    pyautogui.click(910, 629)
    time.sleep(10)
    # collect special missions...
    # ...
    pyautogui.keyDown('esc')
    pyautogui.keyUp('esc')
    time.sleep(10)


def do_farm_stuff():
    # collect ressources
    pyautogui.click(220, 272)
    time.sleep(10)
    pyautogui.click(200, 356)
    time.sleep(10)
    pyautogui.click(949, 921)
    time.sleep(10)
    pyautogui.click(906, 645)
    time.sleep(10)
    pyautogui.click(957, 714)
    time.sleep(10)
    # repair equip
    pyautogui.click(1279, 923)
    time.sleep(10)
    pyautogui.click(723, 817)
    time.sleep(10)
    pyautogui.click(908, 627)
    time.sleep(10)
    for i in range(2):
        pyautogui.keyDown('esc')
        pyautogui.keyUp('esc')
        time.sleep(10)


if __name__ == '__main__':
    main()
