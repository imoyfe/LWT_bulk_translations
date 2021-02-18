
## IDENTIFY UNKNOWN VOCABULARY AND INSERT TRANSLATIONS INTO DATABASE

1. There are 3 main scripts:
* mysql_python.py
* new_words_identifier.py
* translations.py

2. *translations.py* calls *new_words_identifier.py*, that selects from our database the vocabulary currently stored.
It also calls the *new_words_identifier.py* to get the words from a text and then compare them with current words in database so that we obtain the words that are not in our database yet.
Finally, *translations.py* calls an API to translate the words not in db, returning a dictionary with original word as the key and the translation as the value.

3. *mysql_pyhton.py* contains the queries to insert our vocabulary (dictionary) into our database.


### IMPORTANT:

* Add the text to be translated in "input.txt" file.
* Environment variables such as HOST and PASSWORD are located in an .env file. Please, create your own .env file in order to connect with your own database.
* Remember to change the environment variable called TARGET_LANGUAGE_ID (also located in the .env file) in case you want to work with different languages. It has been set "1" for German by default.