#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 13:15:08 2019

@author: Walid Boutellis
"""

import schedule
import time
import praw
import pandas as pd



#Fuction to scrape article elements at certain times
def job():
    
   #Authenticating with reddit servers with the access tokens
   #Fields below are left blank for security and privacy purposes
    reddit = praw.Reddit(client_id='',
                             client_secret='',
                             password='',
                             user_agent='',
                             username='')
    

    #Creating an instance of reddit object specifying the subreddit to scrape from
    subreddits=reddit.subreddit('news')
    
    #Extracting top 15 hot posts from the hot section of reddit
    hot_news=subreddits.hot(limit=15)

    #Creating a dictionary to append the values extracted from the api 
    topics_dict={"title":[],\
             "score":[],\
             "id":[],\
             "url":[],\
             "comms_num":[],\
             "author":[],\
             "upvote_ratio":[],\
             }
    
    #Looping through the elements and appeding them to the dictionary    
    for submission in hot_news:
      topics_dict["title"].append(submission.title)
      topics_dict["score"].append(submission.score)
      topics_dict["id"].append(submission.id)
      topics_dict["url"].append(submission.url)
      topics_dict["comms_num"].append(submission.num_comments)
      topics_dict["author"].append(submission.author)
      topics_dict["upvote_ratio"].append(submission.upvote_ratio)
      
     
    df = pd.DataFrame(topics_dict)
    with open('C:/Users/walid/Downloads/reddit_cloud.csv', 'a') as f:
         df.to_csv(f, header=True)
     
    

schedule.every().day.at("15:42").do(job)
schedule.every().day.at("15:43").do(job)

while True:
    schedule.run_pending()
    
    
