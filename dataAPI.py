import tweepy
import numpy as np
import streamlit as st

consumer_key = st.secrets["2eclLd2w8PVXXBDsVWem0Pcle"]
consumer_secret = st.secrets["hYYYsHklf4lcymQIVI46GZAZLqc9L6lICiVfX9dIPPcT5AQ3k6"]
access_token = st.secrets["1174002413902036993-rNgENEVhakXw0w4hMSzARpTECxJcTD"]
access_token_secret = st.secrets["FgpbKH5HSq9Dnc0syWLlrOHEB1QNJLQL6lJqps6CKBugr"]

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def data_fetch(twitter_username):
    user = api.get_user(screen_name=twitter_username)

    statuses_count = user.statuses_count
    followers_count = user.followers_count
    friends_count = user.friends_count
    favourites_count = user.favourites_count
    listed_count = user.listed_count
    default_profile = user.default_profile
    profile_sidebar_border_color = user.profile_sidebar_border_color
    profile_background_tile = user.profile_background_tile
    profile_sidebar_fill_color = user.profile_sidebar_fill_color
    description = user.description

    if profile_sidebar_border_color != "C0DEED":
        profile_sidebar_border_color = 0
    else:
        profile_sidebar_border_color = 1

    if description == "":
        description = 0
    else:
        description = 1

    if profile_sidebar_fill_color == "DDEEF6":
        profile_sidebar_fill_color = 1
    else:
        profile_sidebar_fill_color = 0

    if default_profile:
        default_profile = 1
    else:
        default_profile = 0

    if profile_background_tile:
        profile_background_tile = 1
    else:
        profile_background_tile = 0

    final = [statuses_count, followers_count, friends_count, favourites_count, listed_count, default_profile,
             profile_sidebar_border_color, profile_background_tile, profile_sidebar_fill_color, description]
    return final
