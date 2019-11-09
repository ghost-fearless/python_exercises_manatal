import requests
from bs4 import BeautifulSoup
import argparse


parser = argparse.ArgumentParser(description="Get the number of twitter followers")
parser.add_argument("--user", default="https://twitter.com/KMbappe", help="argument should be like this https://twitter.com/KMbappe")
user = parser.parse_args().user


try:
    twitter_user_html = requests.get(user)
    twitter_user = BeautifulSoup(twitter_user_html.text, "html.parser")
    number_of_followers = twitter_user.find("li", {"class":"ProfileNav-item ProfileNav-item--followers"}).find("span", {"class":"ProfileNav-value"})
    print "The number of followers for: {}, is: {}, or {}".format(user, number_of_followers["data-count"], number_of_followers.text)
except Exception as e:
    print "--user argument should be like this https://twitter.com/KMbappe"
    print "or maybe the user doesn't exist"
