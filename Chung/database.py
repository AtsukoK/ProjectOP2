import psycopg2


def interaction(DataTesting):
    # interactie opzetten dmv .cursor
    conn = psycopg2.connect(" dbname=highscore user=postgres password = 1")
    cursor = conn.cursor()

    cursor.execute(DataTesting)
    conn.commit()

    result = None
    try:
        result = cursor.fetchall()
    except psycopg2.ProgrammingError:

        pass #als er geen data is om in te zetten

    cursor.close()
    conn.close()

    return result


# Uploads a score into the highscores table
def upload_score(name, score):
    interaction("UPDATE highscores SET score = {} WHERE name = '{}'"
                           .format(score, name))


# retrieves scores from database
def display_scores():
    return interaction("SELECT * FROM score")


# show highest highscore from database
def display_top_score():
    result = interact_with_database("SELECT * FROM score ORDER BY score")[0][1]
    return result




def insert_score(name, score):
    interaction("Insert Into highscores(score, name) Values ('{}' , '{}')"
                           .format(score, name))

insert_score( 'test', 0)

#om de correcte database te maken voer de volgende sql syntax in
#create database project_2_highscore
# en dan
#create table highscores(
#    score integer,
#    name TEXT
#);
