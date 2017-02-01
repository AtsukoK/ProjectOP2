import psycopg2
import pygame

screen_width = 1920
screen_height = 1080
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)


def interact_with_database(command):
    connection = psycopg2.connect("dbname=Battleport user=postgres password=Scholtz1")
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


# Updates an existing row in the leaderboards
def update_leaderboards(name, wins, losses):
    interact_with_database("UPDATE leaderboards SET wins = {}, losses = {} WHERE name = '{}'"
                           .format(wins, losses, name))

# Inserts a row into the leaderboards
def insert_leaderboards(name, wins, losses):
    interact_with_database("INSERT INTO leaderboards VALUES ('{}', {}, {})"
                           .format(name, wins, losses))

# Counts the amount of rows
def count_rows():
    counter = interact_with_database("SELECT count(name) FROM leaderboards")
    return counter

# Downloads the leaderboards
def download_leaderboards():
    get_names_leaderboard = interact_with_database("SELECT name, wins, losses FROM leaderboards ORDER BY wins DESC")
    return get_names_leaderboard