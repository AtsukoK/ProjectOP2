import psycopg2
import pygame

screen_width = 800
screen_height = 600
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)


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
    interact_with_database("INSERT INTO leaderboards VALUES ('{}', {}, {}"
                           .format(name, wins, losses))


# Downloads score data from database
#def download_leaerboards():
#    return interact_with_database("SELECT * FROM score")

# Downloads the top score from database

def download_leaderboads():
    names_leaderboard = interact_with_database("SELECT name, wins FROM leaderboards ")
    return names_leaderboard

