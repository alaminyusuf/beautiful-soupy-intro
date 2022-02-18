import requests as req
from bs4 import BeautifulSoup as soap

class TwitterHashTagPosts:
   def __init__(self, hashtag):
      self.hashtag = hashtag
      self.tweets = []
      self.url = "https://mobile.twitter.com/hashtag/" + self.hashtag.strip()

   def scrape_tweets(self):
      content = req.get(self.url)
      soup = soap(content.text, "html.parser")
      tweets = soup.select("#main_content")
      print(tweets)
      for tweet in tweets:
         handle = tweet.find("div", {"class": "username"}).text.replace("\n", "").strip()
         post = tweet.find("div", {"class": "tweet-text"}).text.replace("\n", "").strip()
         self.tweet.append({handle: post})
      return self.tweets


x = TwitterHashTagPosts("tiktokrating")
x.scrape_tweets()