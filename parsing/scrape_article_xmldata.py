import time
import urllib
from tqdm import tqdm


def get_page(start, subject, date, apiKey):
    url = 'https://api.elsevier.com/content/search/scopus?start={start}&count=25' \
          '&query=all%28gene%29&date={date}&sort=citedby-count&subj={subject}&apiKey={key}'.format(start=start,
                                                                                                   key=apiKey,
                                                                                                   date=date,
                                                                                                   subject=subject)
    req = urllib.request.Request(url, headers={'User-Agent': "Chrome/35.0.1916.47"})
    html = urllib.request.urlopen(req).read()
    return html


def scrape(subject, startpage, finishpage, dump_name, args):
    for year in range(2018, 2019):
        print(year)
        with open(dump_name, 'wb') as dumps:
            for start in tqdm(range(startpage, finishpage, 25)):
                try:
                    dump = get_page(start, subject, year, args.apikey)
                    dumps.write(dump + b'\r\n')
                    time.sleep(1)
                except:
                    break
