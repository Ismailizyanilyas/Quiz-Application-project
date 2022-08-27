import time

Red = "\033[0;31m"
Green = "\033[0;32m"
Orange = "\033[0;33m"
Blue = "\033[0;34m"
Purple = "\033[0;35m"
Cyan = "\033[0;36m"
White = "\033[0;37m" 
black = "\033[0;30m"
black = "\033[0;90m"
red = "\033[0;91m"
green = "\033[0;92m"
yellow = "\033[0;93m"
blue = "\033[0;94m"
magenta = "\033[0;95m"
cyan = "\033[0;96m"
white = "\033[0;97m"
cyan_back="\033[0;46m"
pink_back="\033[0;45m"
white_back="\033[0;47m"
blue_back="\033[0;44m"
orange_back="\033[0;43m"
green_back="\033[0;42m"
red_back="\033[0;41m"
grey_back="\033[0;40m"
bold = "\033[1m"
underline = "\033[4m"
italic = "\033[3m"
darken = "\033[2m"
reset = "\033[0m"
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
print(Green + "                      QUIZ APPLICATION V.2                  ")
print(Red + bold + "                        THE SOLAR SYSTEM                    \n")
score = 0

def q(question):
  return input(Blue + question + reset)
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
time.sleep(1.0)
print(Red + bold + "Question 1 of 10")
time.sleep(.50)
q1 = q(" How many kilometres wide is planet Earth? \na. 10,598 km \nb. 12,756 km \nc. 28,450.2 km \n")

if q1 == "b" or q1 == "B" or q1 == "12,756km" or q1 == "12,756 km" or q1 == "12756km" or q1 == "12756 km":
  print("Correct answer!")
  time.sleep(.50)
  print("The Earth measures 12,765 km around its equator, but because the Earth is not a perfect sphere, it measures 12,713.6 km from the North pole to the South.\n")
  score = score+1
  time.sleep(5)
  
elif q1 == "a" or q1 == "A"  or q1 == "10,598km" or q1 == "10,598 km" or q1 == "10598km" or q1 == "10598 km" or q1 == "c" or q1 == "C" or q1 == "28,450.2km" or q1 == "28,450.2 km" or q1 == "28450.2km" or q1 == "28450.2 km":
  print(Red + "Wrong answer!\n")

else:
  print(Red + "Please type a valid answer. This answer will be recorded as incorrect.\n")

time.sleep(5)
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
print(Red + bold + "Question 2 of 10")
time.sleep(.50)
q2 = q(" What is the biggest moon of Saturn? ")

if q2 == "titan" or q2 == "Titan":
  print("Correct answer!")
  time.sleep(.50)
  print("Titan is bigger than Earth's moon, and larger than even the planet Mercury. It's the only world besides Earth that has standing bodies of liquid, including rivers, lakes and seas, on its surface.\n")
  score = score+1
  time.sleep(5)
  
else:
  print(Red + "Wrong answer!\n")

time.sleep(5)
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
print(Red + bold + "Question 3 of 10")
time.sleep(.50)
q3 = q(" Is Uranus one of the following: \na. The seventh planet of the Solar System \nb. The third planet of the Solar System \nc. The fifth planet of the Solar System \nType a, b or c: ")

if q3 == "a" or q3 == "A":
  print("Correct answer!")
  time.sleep(.50)
  print("Uranus is 2.9452 billion km from the Sun, and is located between Neptune and dwarf planet Pluto.\n")
  score = score+1
  time.sleep(5)
  
elif q3 == "b" or q3 == "B" or q3 == "c" or q3 == "C":
  print(Red + "Wrong answer!\n")

else:
  print(Red + "Please type a valid answer. This answer will be recorded as incorrect.\n")

time.sleep(5)
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
print(Red + bold + "Question 4 of 10")
time.sleep(.50)
q4 = q(" How many planets are there in the Solar System? \n")

if q4 == "eight" or q4 == "Eight" or q4 == "8":
  print("Correct answer!")
  time.sleep(.50)
  print("There are eight planets in the Solar System, and they, in order, are Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus and Neptune.\n")
  score = score+1
  time.sleep(5)
  
else:
  print(Red + "Wrong answer!\n")

time.sleep(5)
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
print(Red + bold + "Question 5 of 10")
time.sleep(.50)
q5 = q(" What is the tallest mountain in the Solar System? \na. Mount Everest on Earth \nb. Olympus Mons on Mars \nc. Mons Rümker on the Moon \nType a, b or c: ")

if q5 == "b" or q5 == "B":
  print("Correct answer!")
  time.sleep(.50)
  print("Olympus Mons is tallest mountain and volcano in the Solar System, and is three times taller than Mount Everest on Earth, with a height of 21.9 km and a width of 624 km.\n")
  score = score+1
  time.sleep(5)
  
elif q5 == "A" or q5 == "a" or q5 == "C" or q5 == "c":
  print(Red + "Wrong answer!\n")

else:
  print(Red + "Please type a valid answer. This answer will be recorded as incorrect.\n")

time.sleep(5)
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
print(Red + bold + "Question 6 of 10")
time.sleep(.50)
q6 = q(" What is the name of the famous storm on Jupiter that is larger than Earth? \n")
q6 = q6.lower()
if q6 == "great red spot" or q6 == " the great red spot":
  print("Correct answer!")
  time.sleep(.50)
  print("The Great Red Spot is currently the largest storm in the Solar System, with a width of 16,350 km but originally being 40,000 km wide (which is large enough to swallow three Earths).\n")
  score = score+1
  time.sleep(5)
  
else:
  print(Red + "Wrong answer!\n")

time.sleep(5)
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
print(Red + bold + "Question 7 of 10")
time.sleep(.50)
q7 = q(" What planet was originally a planet, but now isn't? \n")

if q7 == "Pluto" or q7 == "pluto":
  print(reset + "Correct answer!")
  time.sleep(.50)
  print("Pluto is 5,900,000,000 kilometers from the Sun, and because it was too small to be a planet, it was classified as a planet in 2006.\n")
  score = score+1
  time.sleep(5)
  
else:
  print(Red + "Wrong answer!\n")

time.sleep(5)
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
print(Red + bold + "Question 8 of 10")
time.sleep(.50)
q8 = q(" What probes were the first to leave the Solar Sytem? \na. The Cassini-Huygens probes \nb. The Pioneer probes \nc. The Voyager probes \nType a, b or c: ")
q8 = q8.lower()

if q8 == "voyager" or q8 == "voyager probes" or q8 == "the voyager probes" or q8 == "c":
  print("Correct answer!")
  time.sleep(.50)
  print("The Voyager probes were lauched in 1977, and on 25th August 2012, Voyager 1 became the first human-made object to leave the Solar System.\n")
  score = score+1
  time.sleep(5)
  
else:
  print(Red + "Wrong answer!\n")

time.sleep(5)
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
print(Red + bold + "Question 9 of 10")
time.sleep(.50)
q9 = q(" What is the largest object in the Asteroid belt \na. Vesta \nb. Ceres \nc. Capricornus \n")
q9 = q9.lower()

if q9 == "ceres" or q9 == "b":
  print("Correct answer!")
  time.sleep(.50)
  print("Ceres, with a diameter of 946 km was the first ‘asteroid‘ to be discovered, and is now classified as a dwarf planet.\n")
  score = score+1
  time.sleep(5)
  
elif q9 == "vesta" or q9 == "capricornus" or q9 == "c" or q9 == "a":
  print(Red + "Wrong answer!\n")

else:
  print(Red + "Please type a valid answer. This answer will be recorded as incorrect.\n")

time.sleep(5)
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
print(Red + bold + "Question 10 of 10")
time.sleep(.50)
q10 = q("Which object in the Solar System is nicknamed ‘morning star‘ or ‘evening star‘? \na. Venus \nb. Halley's Comet \nc. Sun \n")
q10 = q10.lower()

if q10 == "venus" or q10 == "a":
  print("Correct answer!")
  time.sleep(.50)
  print("Venus was once thought to be a star, and is the brightest object in the night sky after the moon. Venus can even cast shadows. \n")
  score = score+1
  time.sleep(5)
  
elif q10 == "b" or q10 == "c" or q10 == "sun" or q10 == "halleys comet" or q10 == "halley's comet" or q10 == "the sun":
  print(Red + "Wrong answer!\n")

else:
  print(Red + "Please type a valid answer. This answer will be recorded as incorrect.\n")

time.sleep(5)

if score < 10:
  print(Cyan + bold + "┌--------------------------┐")
  print("|Your score is:", score, "out of 10|")
  print("└--------------------------┘")

if score == 10:
  print("\033[3;35;40m┌----------------┐")
  print("|Congratulations!|")
  print("└----------------┘")
  time.sleep(.50)
  print("\033[1;33;47mYOU HAVE GOT 10 OUT OF 10!")