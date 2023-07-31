import mysql.connector
import webbrowser

filename = "play_history.html"

def main(body, filename):
    #create a body of html page
    output = open(filename,"w")
    output.write(body)
    output.close()


def html():
    global filename
    # connecting to the MYsql and create a data base
    htm = mysql.connector.connect(user='root', password='',host='localhost',database='hangman_game')
    
    #select table in the data base
    select_table = """SELECT * FROM player_table"""
    cursor = htm.cursor()
    cursor.execute(select_table)
    result = cursor.fetchall()

    lis = []

    tbl = "<tr><td>player_name</td><td><td>played_games</td><td><td>won</td><td><td>lost</td><td></tr>"
    lis.append(tbl)

    for rows in result:
        a = "<tr><td>%s</td>"%rows[0]
        lis.append(a)
        b = "<td><td>%s</td>"%rows[1]
        lis.append(b)
        c = "<td><td>%s</td>"%rows[2]
        lis.append(c)
        d = "<td><td>%s</td></tr>"%rows[3]
        lis.append(d)


    
    body = '''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
    <html>
    <head>
    <meta content="text/html; charset=ISO-8859-1"
    http-equiv="content-type">
    <title>Game History</title>
    </head>
    <body>
    <table>
    %s
    </table>
    </body>
    </html>
    '''%(lis)
    main(body, filename)#call main function
    webbrowser.open(filename)#open web browser and show Game Results
    #close Mysql 
    if(htm.is_connected()):
        cursor.close()
        htm.close()
        print("MySQL connection is closed.")   


    

 
