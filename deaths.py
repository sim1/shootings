import time
import requests
import pendulum
import re
from requests_html import HTMLSession
class Deaths:
    def __init__(self, refresh_time=3600):
        self.last_updated = int(time.time())
        self.refresh_time = refresh_time
        self.shootings = None

    @property
    def should_update(self):
    	return (int(time.time()) - self.last_updated) > self.refresh_time

    def update(self):
        if self.shootings and not self.should_update:
            return
        self._get_wikipedia()


    def last(self, days):
        self.update()

        ret = {'count': 0, 'deaths': 0, 'injuries': 0, 'days': days}
        dayfrom = pendulum.now().subtract(days=days).set(hour=0, minute=0, second=0, microsecond=0)
        for shooting in self.shootings:
            print('st', shooting)
            print('df', type(dayfrom))
            print('pd', type(shooting['pdate']))
            if shooting['pdate'] > dayfrom:
                ret['deaths'] += shooting['dead']
                ret['injuries'] += shooting['injured']
                ret['count'] += 1

        ret['deaths_daily'] = round(ret['deaths'] / ret['days'], 1)
        ret['injuries_daily'] = round(ret['injuries'] / ret['days'], 1)

        return ret

    def _get_wikipedia(self):
        deaths = []
        session = HTMLSession()
        r = session.get('https://en.wikipedia.org/wiki/List_of_mass_shootings_in_the_United_States_in_2019')
        for row in r.html.find('table')[0].find('tr'):
            if len(row.find('td')) < 5:
                continue
            date, _, dead, injured, __, description = row.find('td')
            data = {
                'date': date.text,
                'pdate': pendulum.from_format(date.text, 'MMMM D, YYYY'),
                'injured': int(re.sub(r'\[n \d\]','', injured.text)),
                'dead': int(re.sub(r'\[n \d\]','', dead.text)),
            }
            deaths.append(data)
            print(data)
        self.shootings = deaths

D = Deaths()
print(D.last(7))