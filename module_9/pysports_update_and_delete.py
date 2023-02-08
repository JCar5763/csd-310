import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

# method created for INNER JOIN - display results easier for insert, update, and delete
def show_players(cursor, title):

    # INNER JOIN and get results from cursor - next two lines
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    players = cursor.fetchall()

    print("\n  -- {} --".format(title))
    
    # for loop to display the results properly 
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))

#try/except block for the connection to the database
try:
    # connect to the database
    db = mysql.connector.connect(**config) 

    cursor = db.cursor()

    # INSERT INTO player, provide info, and commit - next 4 lines
    add_player = ("INSERT INTO player(first_name, last_name, team_id)"
                 "VALUES(%s, %s, %s)")
 
    player_data = ("Smeagol", "Shire Folk", 1)

    cursor.execute(add_player, player_data)
 
    db.commit()

    # call method to display the results after INSERT
    show_players(cursor, "DISPLAYING PLAYERS AFTER INSERT")


    # UPDATE player and execute with cursor - next 2 lines 
    update_player = ("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'")

    cursor.execute(update_player)

    # call method to display the results after UPDATE
    show_players(cursor, "DISPLAYING PLAYERS AFTER UPDATE")


    # DELETE player and execute with cursor - next 2 lines
    delete_player = ("DELETE FROM player WHERE first_name = 'Gollum'")

    cursor.execute(delete_player)

    # call method to display the results after DELETE
    show_players(cursor, "DISPLAYING PLAYERS AFTER DELETE")

    input("\n\n  Press any key to continue... ")

#try/except block for the connection to the database
except mysql.connector.Error as err: 

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:

    db.close()