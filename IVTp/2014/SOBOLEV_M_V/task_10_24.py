sila=0 
lovkost=0 
mudrost=0
zdorovie=0
pool=30
inp=""
chis=0;
print("У вас есть 4 характеристики и 30 очков, распределите их.\nЕсли устанете, нажмите 'Выход'"
+"\nСила \t = "+str(sila)+"\nЗдоровье = "+str(zdorovie)+"\nМудрость = "+str(mudrost)+
"\nЛовкость = "+str(lovkost)+"\nочков: "+str(pool))
while True:
     inp=input("Введите характеристику которую хотите изменить: ")
     if inp.lower()=="выход":
	     break
     chis=input("Введите число на которое хотите изменить: ")
     pool-=int(chis)
     if(pool<=30 and pool >= 0 and inp.lower()=="сила" and (sila+int(chis))>0):     
	      sila+=int(chis)
     elif(pool<=30 and pool >= 0 and inp.lower()=="здоровье" and (zdorovie+int(chis))>0):
	     zdorovie+=int(chis)
     elif(pool<=30 and pool >= 0 and inp.lower()=="мудрость" and (mudrost+int(chis))>0):
	     mudrost+=int(chis)
     elif(pool<=30 and pool >= 0 and inp.lower()=="ловкость" and (lovkost+int(chis))>0):	 
	     lovkost+=int(chis)
     else:
	     pool+=int(chis)
	     print("Неправильный ввод")
     print("Сила \t = "+str(sila)+"\nЗдоровье = "+str(zdorovie)+"\nМудрость = "+str(mudrost)+
	 "\nЛовкость = "+str(lovkost)+"\nочков: "+str(pool))
input("\n\nСпасибо за игру")
