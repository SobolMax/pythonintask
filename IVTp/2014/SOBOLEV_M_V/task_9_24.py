import random
words=("питон","загадка","простая","сложная","ответ","яблоко")
word=random.choice(words)
live=5
letter=""
wooord=""
(number)=len(word)
print("Я загадал слово, угадай это слово. В этом слове ",str(number),"букв.")
print("У тебя " +str(live)+ " попытки угадать буквы")
while live>0:
	#print (word)
	letter=input("Введите букву\n")
	if letter in list(word):
		print("Да.")
		live=live-1
	else:
		print("Нет.")
		live=live-1
if live==0:
	wooord=input("Попытки закончились. Угадайте слово")
	if wooord==word:
		print("Вы угадали слово")
	else:
		print("Вы не угадали слово")
input("Нажмите Enter для выхода.")
