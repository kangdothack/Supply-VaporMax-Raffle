import names
import random
import requests
from bs4 import BeautifulSoup
from config import *
from sizes import *
from utils import *

submit_count = input('\nEnter Desired Number of Raffle Entries: ')


def submit():
    headers = {
        'User-Agent': user_agent
    }

    s = requests.Session()
    s.headers.update(headers)

    first_name = names.get_first_name(gender='male')
    last_name = names.get_last_name()
    email = '{}+{}@gmail.com'.format(email_prefix, random.getrandbits(40))
    phone = '04{}'.format(random.randint(10000000, 99999999))

    r = s.get(raffle_url)
    soup = BeautifulSoup(r.text, 'html.parser')
    form = soup.find('form')
    data_id = form['data-id']

    payload = {
        'email': email,
        'data': data_id
    }

    r = s.post(url='https://createsend.com//t/getsecuresubscribelink', data=payload)
    submit_url = r.text

    payload = {
        'cm-f-dyhlkkm': first_name,
        'cm-f-dyhlkkc': last_name,
        'cm-uhutyhi-uhutyhi': email,
        'cm-f-dyhlkkq': phone,
        'cm-fo-dyhlkkjj': sizes.get(size, '11128638'),
        'cm-f-dyhlkka': street,
        'cm-f-dyhlkkf': town,
        'cm-f-dyhlkkz': state,
        'cm-f-dyhlkkv': country,
        'cm-f-dyhlkke': post_code,
        'cm-f-dyhlkks': '',
        'terms': 'Yes'
    }

    r = s.post(url=submit_url, data=payload)
    if 'Thank you for submitting your details' in r.text:
        g_logging('{}/{} Successful Raffle Entries'.format(i, submit_count))
    else:
        r_logging(r.text)


for i in range(int(submit_count)):
    submit()
