import random
from datetime import datetime
import create_database

#create variables
user_name=""
element="_"
#create dictionary
word=["cat","rat","dog","elephant","tiger","cow","lion","rabbit","shark","dolphin","parrot","crow","frog","cheeta","monkey"]
word_num=0
name=[]
won=0
lost=0
games_played=0
date_time=0
h1="HANGMAN GAME"
print(h1.center(75,'*'))
print()

now=datetime.now()#current date and time
date_time=now.strftime("%d/%m/%Y , %H:%M:%S")
print("date and time: ",date_time)
print()                       
         
def main():
    global user_name,element
    if __name__=='__main__': 
      if element in user_name:
        pass
      else:
       user_name=input("Enter Player Name:- ")
       element=user_name
      start()
      choice=input("Do you want to run again(if yes select y if no select n):-  ")
      if choice in 'y':
        main()
      
      else:
          choice=='n'
          create_database.base(user_name,games_played,lost,won)
       
  
def start():
  letter=" "
  global word,word_num,won,games_played,lost
  random_word=random.choice(word)
  word_num=len(random_word)
  games_played+=1
  count = word_num+1
  while count > 0:

      win=word_num
     
      print()
      
      print("\nword:-",end=" ")
      for element in random_word:
  
         

        if element in letter:
            win=win-1
            print(element,end="")
             
        else:
            print("_",end=" ")     
            
             
 
      if win == 0:
       
         print("\nYou Won!")
         print("Word is ",random_word)
         won+=1
         break
         
         
      elif count == 1:
              print("\nYou Lost!")    
              print("Word is ",random_word)
              lost+=1
              break
      print()        
      print(count-1, "turns remaining")
      user  = input("\nletter:")
      letter += user
      
      if user  not in random_word:     
             count -= 1
             print("Invaid")


main()#call main function



