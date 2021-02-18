import requests
import time
from bs4 import BeautifulSoup
from urllib.parse import quote
from new_words_identifier import get_words_not_in_db
from get_words_from_db import get_words_from_db
from random import randrange
from new_words_identifier import get_steem_from_verb


def get_translation(wd):
    word = get_steem_from_verb(wd)
    encodedWord = quote(word, safe='')

    headers = {
        "Connection": "keep-alive",
        "Cache-Control": "max-age=0",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"  # ,
        # "Cookie": "_ga=GA1.2.1881955161.1582831612; experiment_context_frz5KvKmF=8; __gads=ID=f4f9d6b7b527a2c1:T=1582831617:S=ALNI_MZr_ect1ZrW8mgXuF_Q3G6HrGJNfg; __qca=P0-1709188403-1582831616045; JSESSIONID=jnDp-tOSFfm0-LvOsKSmg5-E.unknown-host; CTXTNODEID=bstweb16; _gid=GA1.2.172236075.1595256918; didomi_token=eyJ1c2VyX2lkIjoiMTcwODgxZGEtYTVkMy02MDBmLTgxMmMtNWY5NTg5MTQ2ZmQyIiwiY3JlYXRlZCI6IjIwMjAtMDItMjdUMTk6MjY6NTEuNDgwWiIsInVwZGF0ZWQiOiIyMDIwLTA3LTIwVDE0OjU1OjIwLjA2NFoiLCJ2ZW5kb3JzIjp7ImVuYWJsZWQiOlsiZ29vZ2xlIiwiZmFjZWJvb2siXX0sInB1cnBvc2VzIjp7ImVuYWJsZWQiOlsiY29va2llcyIsImFkdmVydGlzaW5nX3BlcnNvbmFsaXphdGlvbiIsImFkX2RlbGl2ZXJ5IiwiY29udGVudF9wZXJzb25hbGl6YXRpb24iLCJhbmFseXRpY3MiXX0sInZlcnNpb24iOjF9; euconsent=BOvcO_SO22ONwAHABBENDS-AAAAxJr_7__7-_9_-_f__9uj3Or_v_f__32ccL59v_h_7v-_7fi_-0nV4u_1vft9yfk1-5ctDztp5w7iakivXmqdeb1v_nz3_9pxP78k89r7335EQ_v8_v-b7BCPN_Y3v-8K96lPK; context.lastpair=de-en; history_pair=de-en; experiment_context_H5bY9vKoU=0; _gat=1"
    }

    response = requests.get(
        "https://en.langenscheidt.com/german-english/" + encodedWord, headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser')
    el = span = soup.find(id="did-you-mean")
    span = soup.select_one(".summary-inner > a")
    if span and not el:
        translation = span.text
        return translation.strip()
    return ""


def get_translations():
    translations = {}
    for word in get_words_not_in_db(get_words_from_db()):
        time.sleep(randrange(0, 1))
        translation = get_translation(word)
        if translation != "":
            translations[word] = translation

    return translations
