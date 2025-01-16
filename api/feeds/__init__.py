feedbooks = {}

def register_feedbook(feedbook_class):
  feedbook = feedbook_class()
  feedbooks[feedbook.key] = feedbook

from .yufm_com import YufmComFeedBook
register_feedbook(YufmComFeedBook)
