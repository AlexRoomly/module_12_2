import requests as rq
import logging

logger = logging.getLogger('RequestsLogger')
loggerBad = logging.getLogger('RequestsLogger2')
loggerBlock = logging.getLogger('RequestsLogger3')

formatter = logging.Formatter('%(levelname)s: %(message)s')
logger.setLevel(logging.INFO)
fh1 = logging.FileHandler("success_responses.log", 'w', 'utf-8')
fh1.setFormatter(formatter)
logger.addHandler(fh1)
loggerBad.setLevel(logging.WARNING)
fh2 = logging.FileHandler("bad_responses.log", 'w', 'utf-8')
fh2.setFormatter(formatter)
loggerBad.addHandler(fh2)
loggerBlock.setLevel(logging.ERROR)
fh3 = logging.FileHandler("blocked_responses.log", 'w', 'utf-8')
fh3.setFormatter(formatter)
loggerBlock.addHandler(fh3)

sites = ['https://www.youtube.com/', 'https://instagram.com', 'https://wikipedia.org', 'https://yahoo.com',
         'https://yandex.ru', 'https://whatsapp.com', 'https://twitter.com', 'https://amazon.com', 'https://tiktok.com',
         'https://www.ozon.ru']

for site in sites:
    try:
        response = rq.get(site, timeout=3)
        print(response)

        if response.status_code == 200:
            logger.info(f'{site}, response - {response.status_code}')
        else:
            loggerBad.warning(f'{site}, response - {response.status_code}')
    except rq.RequestException:
        loggerBlock.error(f'{site}, NO CONNECTION')
