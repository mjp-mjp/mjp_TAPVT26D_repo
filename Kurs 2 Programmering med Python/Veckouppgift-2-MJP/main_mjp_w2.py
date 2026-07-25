# This is my Pythonprojekt for week 2 assignment
# 1 Diskutera i grupp
# 1.1 Syftet med koden ser ut att vara att en medlem i nån sorts kundklubb får
# veta vilken rabatt (i procent) de ska få när de når en viss nivå i värde.
# 1.2 Hela koden går inte att köra utan det blir krasch.
# 1.3 Ja, förklaras nedan, bla krasch på final price
# 1.4 Det blir lite "Vilda västern" om/när kunden har nått en viss nivå för rabatt.
# Tex kan man ange 1kr och ändå komma upp till nivå 2. Eller ange 200kr och då bara
# få komma upp till nivå 1. Detta är för att if satserna är fel.

print("Uppgift 1 - Kod utan krasch och utan logiska fel")
level_1 = 100
level_2 = 300
discount = 0

price = input("Välkommen, slå in priset på din vara: ")
price = float(price)
if price >= level_1 and price < level_2:        #större än eller lika med 100 & mindre än 200 så blir det true
    print("Grattis! Du har avancerat till nivå 1 och får 10% rabatt.")
    discount = discount + 10
if price >= level_2:                            #större än eller lika med 200 så blir det true
    print("Grattis! Du har avancerat till nivå 2 och får 25% rabatt.")
    discount = discount + 25

final_price = price * (100 - discount) / 100
print("Efter rabatter blir priset .... " + str(final_price)) #här behövdes en str in för att konvertera float (text med tal)

print()

# 2 Balder
# För att få åka Balder på Liseberg måste man vara 130 cm lång. Skriv ett program som kan säga om man får åka!
# Fråga användaren hur lång man är (i cm)
# Skriv ut antingen "Du får åka!" eller "Du får inte åka"
print("Uppgift 2.1 & 2.2")
length = input("Please state your length in cm: ")
length = float(length)
lenght_requirment = 130
if length < lenght_requirment:
    print("You are not allowed on this ride!")
if length >= lenght_requirment:
    print("You are allowed on this ride!")

# # Diskutera
# # Varför just tre värden: Ett under, ett över samt ett som är prick den längden man måste vara.
# # Varför just denna värden: 121 är under, 130 är prick den längd som är den minsta längden att tillåta åkande, 155 är över
# # 129? Ja, absolut då den är närmast i otillåten gräns (och gärna även 131). Det är en bra test för att se att utvecklaren
# # inte missat i hur koden räknar ut (o)tillåten längd, sk. gränsvärdestestning.

print()

# 3 Sportresultat
# Tottenham spelar mot Liverpool i Champions League. Skriv ett program som frågar användaren hur många mål respektive lag
# gjorde, och som talar om vilket lag som vann.
print("Uppgift 3")
print("Let's figure out which team won!")
team_1 = input("State how many goals Tottenham made, pls: ")
team_2 = input("State how many goals Liverpool made, pls: ")
team_1 = int(team_1)
team_2 = int(team_2)
if team_1 > team_2:
    print("The team who won the game is Tottenham!")
elif team_1 < team_2:
    print("The team who won the game is Liverpool!")

print()

print("Uppgift 3 v2")
# Version 2: programmet ska tala om ifall det blev oavgjort.
print("Let's figure out which team won!")
team_1 = input("State how many goals Tottenham made, pls: ")
team_2 = input("State how many goals Liverpool made, pls: ")
team_1 = int(team_1)
team_2 = int(team_2)
if team_1 > team_2:
    print("The team who won the game is Tottenham!")
elif team_1 < team_2:
    print("The team who won the game is Liverpool!")
else:
    print("No winner - the game ended in a tie!")

print()

print("Uppgift 3 v3")
# Version 3: nu ska programmet tala om hur många mål mer laget vann med.
print("Let's figure out which team won!")
team_1_name = "Tottenham"
team_2_name = "Liverpool"
team_1 = input("State how many goals " + team_1_name + " made, pls: ")
team_2 = input("State how many goals " + team_2_name + " made, pls: ")
team_1 = int(team_1)
team_2 = int(team_2)
if team_1 > team_2:
    result = team_1 - team_2
    print("The team who won the game is " + team_1_name + " and they won by " + str(result) + " goal(s)!")
elif team_1 < team_2:
    result = team_2 - team_1
    print("The team who won the game is " + team_2_name + " and they won by " + str(result) + " goal(s)!")
else:
    print("No winner - the game ended in a tie!")

print()

# # 4 Temperaturomvandling
# # Skriv ett program som kan omvandla en temperatur i grader Celsius till grader Fahrenheit.





