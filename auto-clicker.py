import keyboard, pyautogui, time

foods = {
    "baked potato": 440,
    "golden carrot": 816,
    "steak": 587,
    "cooked salmon": 587,
    "pork": 587,
    "rabbit": 587,
    "bread": 440,
    "chicken": 440,
    "carrot": 440,
    "cooked cod": 440
}

afkTime = 10                                # How long you are AFKing for in minutes
firstFoodSlot = 9                           # Slot of your first food slot in your hotbar
lastFoodSlot = 9                            # Slot of your last food slot in your hotbar
foodCounter = 41                            # How much food you have left in your first food slot
timeToEat = 1.62                            # How long it takes to eat your food
typeOfFood = foods["golden carrot"]         # Which food you are eating
firstMendingSlot = 2                        # Slot of the first item you are mending in your hotbar
lastMendingSlot = 6                         # Slot of the last item you are mending in your hotbar

weaponSlot = 1                              # Slot of your weapon hand in your hotbar

attackCooldown = 0.65                       # Length of the cooldown of your weapon
inputRange = afkTime * 60 / attackCooldown  # How many times your avatar will attack during your AFK time

pyautogui.PAUSE = attackCooldown

REPORTER = "switching to %s"

def eat_food():
    keyboard.send("% s" % firstFoodSlot)
    print(REPORTER % firstFoodSlot)
    keyboard.press("shift")
    print("Eating")
    time.sleep(0.5)
    pyautogui.mouseDown(button="right")
    time.sleep(timeToEat)
    pyautogui.mouseUp(button="right")
    print("finished eating")
    time.sleep(0.5)
    keyboard.release("shift")
    keyboard.send("% s" % weaponSlot)
    print(REPORTER % weaponSlot)

def mend_item():
    keyboard.send("% s" % firstMendingSlot)
    print(REPORTER % firstMendingSlot)
    time.sleep(0.5)
    keyboard.send("f")
    time.sleep(0.5)
    keyboard.send("% s" % weaponSlot)
    print(REPORTER % weaponSlot)


print("Attacking: " + str(inputRange) + " times!")
time.sleep(10)

for i in range(int(inputRange)):
    print(str(i))
    pyautogui.click()
    if (i%50 == 0 and firstMendingSlot <= lastMendingSlot):
        mend_item()
        firstMendingSlot += 1
    if (i%typeOfFood == 0):
        if (foodCounter%64 == 0 and firstFoodSlot != lastFoodSlot):
            firstFoodSlot -= 1
        eat_food()
        foodCounter -= 1

print("done")