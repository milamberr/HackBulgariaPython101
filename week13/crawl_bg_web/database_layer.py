import requests
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pprint import pprint


site = 'http://register.start.bg/'
Base = declarative_base()


class BgServers(Base):
    __tablename__ = 'bgservers'
    id = Column(Integer, primary_key=True)
    url = Column(String)
    server = Column(String)
    # count_visitors = Column(Integer)


engine = create_engine('sqlite:///bg_servers.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def crawl_servers():
    import re

    response = requests.get(site)
    content = response.text
    content = re.findall("link\.php\?id=\d+", content)
    crawl_info(content)


def crawl_info(content):
    import re

    for i in range(len(content)):
        id_ref = int(re.findall('\d+', content[i])[0])
        print(i)
        search_site = '{0}{1}'.format(site, content[i])
        new_response = requests.get(search_site, timeout=5)
        if new_response.status_code == 200 and 'Server' in new_response.headers.keys():
            url = new_response.url
            server = new_response.headers['Server'].split("/")[0]
            print(server, url, id_ref)
            #post(url, server, id_ref)
            crawl_info_in_database(server, url)

    session.commit()


def post(url, server, id_ref):
    requests.post('http://192.168.0.14:5000/',
        data={
            'server': server,
            'url': url,
            'id': id_ref
        }
    )


def crawl_info_in_database(server, url):
    session.add(BgServers(url=url, server=server))


crawl_servers()
