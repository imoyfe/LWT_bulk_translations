import mysql.connector
from mysql.connector import MySQLConnection, Error
from dotenv import load_dotenv
import os

load_dotenv()

HOST = os.getenv("HOST")
PASSWORD = os.getenv("PASSWORD")

def get_words_from_db():
    db_words = []
    query = "SELECT WoText FROM `learning-with-texts`.words"
    conn = mysql.connector.connect(host=HOST, user="root", password=PASSWORD)
    cursor = conn.cursor()
    
    try:
        cursor.execute(query)
        myresult = cursor.fetchall()
        
        for wo in myresult:
            db_words.append(wo[0])

        conn.commit()

    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()
    
    return db_words

