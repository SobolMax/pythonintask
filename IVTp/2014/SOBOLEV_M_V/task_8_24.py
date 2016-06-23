import random

inp=""
words="Сессия","Питон","Автомат","РГСУ","Расписание"
podskaz="Студенты не любят этого","Язык программирования",\
"Все студенты хотят это","Альма матер","Странный предмет, вроде бы есть, а вроде и нет"
rand=random.randint(0,4)
massiv=list(words[rand].lower())
random.shuffle(massiv)
anagram=''.join(massiv)
score=0
print("Компьютер загадал одно из 5 слов относящиеся к учубе: "+anagram)
while inp.lower()!=words[rand].lower():
     inp=input("Введите слово: ")
     if words[rand].lower()==inp.lower():
	     score=score+10
	     print('Вы угадали')
     elif inp.lower()=="подсказка":
	     score=score-5
	     print(podskaz[rand]) 		 
     else:
	     print("Вы не угадали =(\nВведите 'Подсказка'")
input("Вы набрали: "+str(score)+" очков\n\nOk")
