

import gettext
import pycountry
import requests
from bs4 import BeautifulSoup
import re
from cleanco import cleanco
from hashlib import sha256


def hash(email_address):
    """Generates an unique identifier for a given item."""
    # hash based on email_address
    return sha256(str(email_address).encode('utf-8')).hexdigest()


def english_to_katakana(word):
    """ converts english into katakana - works with more than one words;
    english_to_katakana("good morning") -> 'グッド・モーニング' """
    url = 'https://www.sljfaq.org/cgi/e2k_ja.cgi'
    url_q = url + '?word=' + word
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15'}
    request = requests.get(url_q, headers=headers)
    soup = BeautifulSoup(request.text, 'html.parser')
    katakana_string = soup.find_all(class_='katakana-string')[0].string.replace('\n', '')
    return katakana_string

def to_jap_com_name(comnam):
    ''' extract suffix, convert name to katakana, translate suffix - return string
    to_jap_com_name('Padilla PLC') => 'パディラー株式会社' '''
    # 1. extract company suffix
    # 2. Katakana name
    # 3. Append Translation of suffix
    analyzed_name = cleanco(comnam)
    basename, suffix = analyzed_name.clean_name(), analyzed_name.type()
    jap_basename = english_to_katakana(basename)
    jap_suffix = '株式会社' if suffix else ''
    return jap_basename + jap_suffix
    

def to_jap_country(eng_country):
    translator = gettext.translation('iso3166', pycountry.LOCALES_DIR, languages=["ja"])
    translator.install()
    _ = translator.gettext
    jap_country=_(eng_country)
    return jap_country if jap_country!=eng_country else None

def extract_street_num(street1):
    '''picks up any numbers before the text
    Japanese address put these are end of line'''
    match = re.match("(?P<num>\s*\d+-?\d*)?\s*(?P<rem>.*)",street1,flags=re.DOTALL)
    return match.group("num"), match.group("rem")