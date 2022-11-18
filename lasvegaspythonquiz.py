#Listing containing my question as well as my answers. This saves lots of time and space as we do not need to create lots of if/else code for every single question
QandA = ["1. What US State is Las Vegas located in? a) California b) Nevada c) Wyoming d) Illinois -", "Nevada", 
"2. What is Las Vegas most famous for? a) Music b) Business c) Gambling d) Sightseeing -", "Gambling", 
"3. What is the area that contains Las Vegas's most famous casinos called? a) The Street b) The Las Vegas Concord c) The Las Vegas Strip d) Casino Lane -", "The Las Vegas Strip", 
"4. The Las Vegas Strip is not actually located in the district of Las Vegas. What district is it located in? a) Reno b) New Vegas c) McCarran d) Paradise -", "Paradise", 
"5. Who is widely considered to be the father of Las Vegas? a) Howard Hughes b) Donald Trump c) Bugsy Siegel d) Dean Martin -", "Bugsy Siegel", 
"6. Which airport is widely used to travel to Las Vegas? a) LAX b) McCarran c) Harry Reid d) Salt Lake City -","Harry Reid", 
"7. Concert residencies are a staple of the Las Vegas strip. Which group of artists is considered to have pioneered musical residencies in Vegas? a) The Rolling Stones b) The Beatles c) The Rat Pack d) The Backstreet Boys -", "The Rat Pack", 
"8. Recently, the slogan for Las Vegas changed. What is the old slogan for Las Vegas? a) What happens in Vegas, stays in Vegas b) Viva Las Vegas c) What happens here, only happens here d) The Happiest Place on Earth -", "What happens in Vegas, stays in Vegas", 
"9. Las Vegas is home to some of the world's most famous casinos. Which of the following is NOT one of these casinos? a) The Bellagio b) Skycity c) Caesar's Palace d) The Flamingo -", "Skycity", 
"10. What is the tallest building in Las Vegas? a) The Eiffel Tower b) The Spire c) The Stratosphere d) The Statue of Liberty -","The Stratosphere", 
"11. What does Las Vegas translate to in Spanish? a) The Bells b) The Meadows c) My Dear d) Gold Ring -", "The Meadows", 
"12. Las Vegas is widely considered to be the brightest spot on earth. True or False: Is it visible from space? a) True b) False -", "True"]
#Sets points and current to 0 at the start of the quiz so the following quiz can function properly
points = 0
current = 0
#Introduction to the quiz and gives instructions on how to answer the quiz
print("Welcome to my Las Vegas quiz! Hope you enjoy your play! IMPORTANT: To answer questions type in the answer as it is written in the question. For example, in the question 'Which number comes first? a) 5 b)3 c)89 d) 6?' the answer is 3, so to answer you would type in 3 NOT c)/c")

#Questions
question1 = input(QandA[current])
if question1 == QandA[current+1]:
  print ("Ring a Ding Ding!")
  current = current +2
  points = points +10
else:
     print ("Wrong! Try again next time.")
     current = current +2
     points = points -10

question2 = input(QandA[current])
if question2 == QandA[current+1]:
  print ("Ring a Ding Ding!")
  current = current +2
  points = points +10
else:
     print ("Wrong! Try again next time.")
     current = current +2
     points = points -10

question3 = input(QandA[current])
if question3 == QandA[current+1]:
  print ("Ring a Ding Ding!")
  current = current +2
  points = points +10
else:
     print ("Wrong! Try again next time.")
     current = current +2
     points = points -10

question4 = input(QandA[current])
if question4 == QandA[current+1]:
  print ("Ring a Ding Ding!")
  current = current +2
  points = points +10
else:
     print ("Wrong! Try again next time.")
     current = current +2
     points = points -10

question5 = input(QandA[current])
if question5 == QandA[current+1]:
  print ("Ring a Ding Ding!")
  current = current +2
  points = points +10
else:
     print ("Wrong! Try again next time.")
     current = current +2
     points = points -10
            
question6 = input(QandA[current])
if question6 == QandA[current+1]:
  print ("Ring a Ding Ding!")
  current = current +2
  points = points +10
else:
     print ("Wrong! Try again next time.")
     current = current +2
     points = points -10
        
question7 = input(QandA[current])
if question7 == QandA[current+1]:
  print ("Ring a Ding Ding!")
  current = current +2
  points = points +10
else:
     print ("Wrong! Try again next time.")
     current = current +2
     points = points -10
            
question8 = input(QandA[current])
if question8 == QandA[current+1]:
  print ("Ring a Ding Ding!")
  current = current +2
  points = points +10
else:
     print ("Wrong! Try again next time.")
     current = current +2
     points = points -10
            
question9 = input(QandA[current])
if question9 == QandA[current+1]:
  print ("Ring a Ding Ding!")
  current = current +2
  points = points +10
else:
     print ("Wrong! Try again next time.")
     current = current +2
     points = points -10
            
question10 = input(QandA[current])
if question10 == QandA[current+1]:
  print ("Ring a Ding Ding!")
  current = current +2
  points = points +10
else:
     print ("Wrong! Try again next time.")
     current = current +2
     points = points -10
            
question11 = input(QandA[current])
if question11 == QandA[current+1]:
  print ("Ring a Ding Ding!")
  current = current +2
  points = points +10
else:
     print ("Wrong! Try again next time.")
     current = current +2
     points = points -10
            
question12 = input(QandA[current])
if question12 == QandA[current+1]:
  print ("Ring a Ding Ding!")
  current = current +2
  points = points +10
else:
     print ("Wrong! Try again next time.")
     current = current +2
     points = points -10
#Lists the users final score
print("Well done! You have earned", points, "points! Try your luck at another game perhaps?")