from feedgen.feed import FeedGenerator

class Feedbook:
  key = None
  title = None
  url = None
  description = None
  feed = None

  def __init__(self):
    feed = FeedGenerator()
    feed.id(self.feed_url())
    feed.link(href=self.url, rel='alternate')
    feed.link(href=self.feed_url(), rel='self')
    feed.title(self.title)
    feed.description(self.description)
    self.feed = feed

  def feed_url(self):
    return f"https://myfeedbook.vercel.app/feed/{self.key}"
