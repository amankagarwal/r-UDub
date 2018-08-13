import requests
from pprint import pprint
import json

# This code currently creates a dictionary out of all the posts (not comments, yet)
# which were posted in between the given timestamps (used the winter quarter timestamps for testing)
# Code takes 12 seconds to run currently, so efficiency is certainly in question here.

START_TIMESTAMP = 1514937600 #3rd january timestamp 00:00:00
END_TIMESTAMP = 1521244800 #17th march timestamp 00:00:00
BASE_URL = "https://www.reddit.com/r/udub/new"

def get_dict_from_json(url):
    send_request = requests.get(url,  headers = {'User-agent': 'your bot 0.1'})
    python_dict = json.loads(send_request.text)
    return (python_dict)

def get_all_data(start_date, end_date): # Can make this function such so that I can get data between two particular days
    count = 0
    after_tag = ""
    main_dict = {}
    for i in range(40): #Reddit stores only 1000 posts 1000/25 = 40 lol
        request_parameters = "/.json?count="  + str(count) + "&after=" + after_tag
        request_url = BASE_URL + request_parameters
        python_dict = get_dict_from_json(request_url)
        after_tag = python_dict["data"]["after"]
        all_posts_array = python_dict["data"]["children"]
        for i in range(len(all_posts_array)):
            post_dictionary = all_posts_array[i]
            post_data = post_dictionary["data"] # This is also a dictionary
            post_timestamp = post_data["created_utc"]
            if (post_timestamp >= start_date and post_timestamp <= end_date): #need a more efficient way to check this
                                                                              #deal with this
                post_author = post_data["author"]
                post_title = post_data["title"]
                post_description = post_data["selftext"]
                post_comments_link = post_data["permalink"]
                main_dict[post_timestamp] = [post_author, post_title, post_description, {"comments_link" : post_comments_link}]
        count = count + 25
    return (main_dict)

main_dict = get_all_data(START_TIMESTAMP, END_TIMESTAMP)
pprint(main_dict)

def parse_comments(comments_link):
    comments_url = "http://www.reddit.com" + comments_link + ".json"
    python_dict = get_dict_from_json(comments_url)

# Working on the comments section extraction
array_of_dicts = get_dict_from_json(url)
pprint(array_of_dicts)
total_comments = len(array_of_dicts)
for i in range(len(array_of_dicts)):
    if  (i != 0): # Why? This means there exists a comment other that the description
        comments_outer_dict = array_of_dicts[i]
        comments_array = comments_outer_dict["data"]["children"]
        for j in range(len(comment_array):
            comment_data_outer_dict = comments_array[j]
            comments_data_inner_dict = comment_data_outer_dict["data"]
            comment_timestamp = comment_data_inner_dict["created_utc"]
            comment_author = comment_data_inner_dict["author"]
            comment_body = comment_data_inner_dict["body"]
            comment_title = comment_data_inner_dict["title"]
            comment_next_after_tag = comment_next_after_tag["after"]
