from translations import get_translations
import mysql.connector
from mysql.connector import MySQLConnection, Error
from dotenv import load_dotenv
import os
#import sys

load_dotenv()

HOST = os.getenv("HOST")
PASSWORD = os.getenv("PASSWORD")
TARGET_LANGUAGE_ID = os.getenv("TARGET_LANGUAGE_ID")


def insert_vocabulary(vocabulary_translations, target_language_id):

    query = "INSERT INTO `learning-with-texts`.words(WoStatus, WoText, WoTextLC, WoTranslation, WoID, WoLgID) " \
            "VALUES (1, %s, %s, %s, %s," + target_language_id + ")"
    query2 = "INSERT INTO `learning-with-texts`.wordtags(WtWoID, WtTgID)" \
        "VALUES (%s, %s)"
    query_to_get_last_autoincrement = "SELECT max(WoID) FROM `learning-with-texts`.words"

    try:
        conn = mysql.connector.connect(
            host=HOST, user="root", password=PASSWORD)
        cursor = conn.cursor()
        cursor.execute(query_to_get_last_autoincrement)
        result = cursor.fetchall()
        if type(result[0][0]) != type(None):
            counter = result[0][0] + 1
        counter = 1

        tuples = []
        for key in vocabulary_translations:
            tupl = (key, key.lower(), vocabulary_translations[key], counter)
            tuples.append(tupl)
            counter += 1

        for tupl in tuples:
            cursor.execute(query, tupl)
            cursor.execute(query2, (tupl[-1], 1))

        conn.commit()

    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()


insert_vocabulary(get_translations(), TARGET_LANGUAGE_ID)
