Temps = int(input("Saisir votre temps : "))

Heures = Temps // 3600 
Reste = Temps % 3600 
Minute = Reste // 60 
Seconds = Reste % 60 

print("Heures : " , Heures, " Minutes : " , Minute, " Seconds : " , Seconds)