#import internal and external packages
import create_table
import mysql.connector
from mysql.connector import Error

#cretae a database for the game
def base(user_name,games_played,lost,won):
    try:
        mydb=mysql.connector.connect(host='localhost',user='root',password='')
        mycoursor=mydb.cursor()

        #check connected or not
        if mydb:
            print("Connected")
        else:
            print("Not Connected")

        mycoursor .execute("CREATE DATABASE hangman_game")
        create_table.table(user_name,games_played,lost,won)
        
        
    except Error as e:
         create_table.table(user_name,games_played,lost,won)

         
    
