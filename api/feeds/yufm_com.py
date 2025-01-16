import requests
from bs4 import BeautifulSoup
from datetime import datetime
from zoneinfo import ZoneInfo
from .feedbook import Feedbook

class YufmComFeedBook(Feedbook):
  key = 'yufm.com'
  title = 'You & FM'
  url = 'https://yufm.com/'
  description = 'You & FM, 记录美好生活的个人休闲博客，内容包括生活、兴趣、学习等方面的日志。'

  def fetch_feed(self):
    self._fetch_articles()

    return self.feed

  def _fetch_articles(self):
    response = requests.get(self.url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the relevant content elements
    articles = soup.select('.main-list .post-loop .item')
    print(f"articles size is {len(articles)}")

    # Add the extracted content to the RSS feed
    for article in articles:
        fe = self.feed.add_entry()

        title = article.select_one('.item-title a')
        fe.title(title.text.strip())
        fe.link(href=title.attrs['href'])
        fe.description(article.select_one('.item-excerpt').text.strip())
        pubdate_str = article.select_one('.item-meta-li.date').text
        pubdate = datetime.strptime(pubdate_str, '%Y 年 %m 月 %d 日')
        pubdate = pubdate.astimezone(ZoneInfo('Asia/Shanghai'))
        fe.pubDate(pubdate)
