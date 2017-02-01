import psycopg2
import main_game

def interact_with_database(command):
    connection = psycopg2.connect("dbname=Battleport user=postgres password=liweiyeh")
    cursor = connection.cursor()

    cursor.execute(command)
    connection.commit()

    # Save results
    results = None
    try:
        results = cursor.fetchall()
    except psycopg2.ProgrammingError:
        # Nothing to fetch
        pass

    # Close connection
    cursor.close()
    connection.close()

    return results


# Uploads a score into the hiscore table
def upload_leaderboards(name, wins, losses):
    interact_with_database("UPDATE score SET score = {} WHERE name = '{}'"
                           .format(name, wins, losses))


# Downloads score data from database
#def download_leaerboards():
#    return interact_with_database("SELECT * FROM score")

print(main_game.saved_name1)
# Downloads the top score from database
def download_top_score():
    result = interact_with_database("SELECT * FROM score ORDER BY score")[0][1]
    return result
