#import mysql connector
import mysql.connector
import html_file

#insert data into table coloumns
def data(user_name,games_played,lost,won):


    da=mysql.connector.connect(host='localhost',user='root',password='',database='hangman_game')
    mycoursor=da.cursor()
    coloumns=("INSERT INTO hangman_game.player_table"
         "(player_name,played_games,lost,won)"
         "VALUES(%s,%s,%s,%s)")
    values=(user_name,games_played,lost,won)
    mycoursor.execute(coloumns,values)

    da.commit()
    mycoursor.close()
    

    da.close()
    html_file.html()#call html function
 








