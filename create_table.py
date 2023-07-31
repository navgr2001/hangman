#import internal and external packages
import insert_data
import mysql.connector
from mysql.connector import Error



#create a batabase table for the game
def table(user_name,games_played,lost,won):
    try:
        tb=mysql.connector.connect(host='localhost',user='root',password='',database='hangman_game')
        mycoursor=tb.cursor()

        mycoursor.execute("CREATE TABLE player_table (player_name VARCHAR(40),played_games int(100),won int(100),lost int(100))")
        insert_data.data(user_name,games_played,lost,won)
    except Error as e:
        
        insert_data.data(user_name,games_played,lost,won)
    
    
    
    
