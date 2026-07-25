import math
# # Veckouppgift 1
# # 1 Starta upp PyCharm - check
# # 2 Skapa projekt och synka med GitHub - delvis check
#
# # message = "Hello world"
# # name = "Marie"
# # print(message)
# # print("This program was made by " + (name) + ".")
#
# # print()
#
# 3 Diskutera i grupp - check, förändringar och resultat enligt nedan
print("3 Diskutera i grupp")
print()
cost = 100              #Biljettpris               100 utan "" vilket då betyder tal (INT) och inte text
amount_to_spend = 200   #Pengar på fickan          samma logik som ovan
print("   Det blir " + str(amount_to_spend - cost ) + " kronor över.") #Str saknades, behövs för att översätta tal till text
what_is_left = int((amount_to_spend - cost) / 2)   #delat går före minus, så paranteser måste sättas. Tänk matte-logik
print("   Varje person får " + str(what_is_left) + " kronor var.")     #Str saknades, behövs för att översätta tal till text

print()

# 4 Använda variabler och datatyper
# 4 1a
print("4 Använda variabler och datatyper")
print("  4 1a")
person_1_age = input("   Hur ung är du? ")
person_1_age = int(person_1_age)
print("   " + str(person_1_age)) #Printar för räknekontroll
print()

# 4 1b
print("4 1b")
person_1_lenght = input("   Vad är din längd i cm (avrunda till närmaste heltal)? ")
person_1_lenght = int(person_1_lenght)
print("   " + str(person_1_lenght))    #Printar för räknekontroll
person_2_lenght = input("   Ange valfri kompis/syskon/kollegas längd (avrunda till närmaste heltal). ")
person_2_lenght = int(person_2_lenght)
print("   " + str(person_2_lenght))    #Printar för räknekontroll
together = input("   Hur långa är ni tillsammans? ")
together = int(together)
print("   " + str(together))        #Printar för räknekontroll
combined_lenght = int(person_1_lenght + person_2_lenght)    #Uträkning av ålder kombinerad
print("   Ni är då tillsammans " + str(combined_lenght) + " cm långa.")

print()

# 4 2a
print("4 2a")
cost = 2000
discount_percent = 75.0
discount_amount = cost * discount_percent / 100 #Uträkning av av vad rabatten blir i värde
left_to_pay = int(cost - discount_amount)       #Uträkning av vad värdet blir att betala efter rabatt
print("  Jackan kommer efter rabatten kosta " + str(left_to_pay) + " kronor.")

print()

# 4 2b
print("4 2b")
cost = input("  Hur mycket kostar jackan du vill köpa? ")
cost = int(cost)
print("  " + str(cost))              #Printar för räknekontroll
discount_percent = input("  Vad är rabatten i procent? ")
discount_percent = int(discount_percent)
print("  " + str(discount_percent))
discount_amount = cost * discount_percent / 100
amount_left_to_pay = int(cost - discount_amount)
print("  Jackan kommer att kosta " + str(amount_left_to_pay) + " kronor.")

print()

# 5 Fler övningar
# 5 1a
print("5 Fler övningar")
print("  5 1a")
speed = input("    Vad tror du din genomsnittliga hastighet kommer vara. Ange km/h. ")
speed = int(speed)
distance = 470
time_to_drive = int(distance / speed)
print("    Det kommer ta ungefär " + str(time_to_drive) + " timmar att köra mellan Sthlm och Gbg.")

print()

print("  5 1b")
speed = input("    Vad tror du din genomsnittliga hastighet kommer vara. Ange km/h. ")
speed = int(speed)
distance = 470
time_to_drive = int(distance / speed * 60)       #Valde INT här för jag ville inte ha resultatet med decimaler
print("    Det kommer ta ungefär " + str(time_to_drive) + " minuter att köra mellan Sthlm och Gbg.")

print()

print("  5 1c")
speed = input("    Vad tror du din genomsnittliga hastighet kommer vara. Ange km/h. ")
speed = int(speed)
distance = 470
total_minutes = (distance * 60) // speed         #Vi måste gör * först för att det ska bli rätt med matten (inifrån och ut)
#Tänk pengar. 5/3 personer blir 1 kr var. Om man först gör om det till ören, så blir det 5*100=500/3 vilket ger 166öre som ju då ger 1,66kr var.
hours = total_minutes // 60                      #Räknar ut minuter till hela (heltal) timmar
minutes = total_minutes % 60                     #Räknar fram vad som blir kvar (resten/modulo) när heltal är uppfyllt
#time_to_drive = (distance / speed * 60)         #Behöver inte denna men lät den vara kvar
print("    Det kommer ta ungefär " + str(hours) + " timmar och " + str(minutes) + " minuter att köra mellan Sthlm och Gbg.")

print()

print("  5 2")
import math                                        #Noterar att rekommendation är att lägga in detta högst upp, men låter det ligga här för stunden.
sida_1 = input("  Hur lång är den stående sidan (y-axel) i triangeln? ")
sida_1 = int(sida_1)
sida_2 = input("  Hur lång är den liggande sidan (x-axel) i triangeln? ")
sida_2 = int(sida_2)
hypotenusan = math.sqrt(sida_1 * sida_1 + sida_2 * sida_2)
print("  Hypotenusan är " + str(hypotenusan))

print()

print("  5 3a")
import datetime                                    #Noterar att rekommendation är att lägga in detta högst upp, men låter det ligga här för stunden.

