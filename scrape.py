import requests as req
import os
import json
from datetime import datetime
import sys

username = sys.argv1

print(username)

hugeCommentsList = []
hugePostsList = []
user_details = {}

def fetch_user_comments(lastcommentID=''):
    print(f"Fetching Comments {len(hugeCommentsList)}..")
    url = f"https://gateway.reddit.com/desktopapi/v1/user/{username}/conversations?rtj=only&allow_over18=1&include=identity&after={lastcommentID}&dist=25&sort=new&t=all"
    result = req.get(url, headers={'User-agent': 'your bot 0.2'})
    comments = result.json()['comments']
    for id in comments:
        comment = comments[id]
        if not comment in hugeCommentsList:
            media = comment['media']['richtextContent']['document'][0]['c'][0]
            if 't' in media:
                comment['created'] = datetime.fromtimestamp(comment['created']).strftime('%Y-%m-%d')
        hugeCommentsList.append(comment)
    try:
        next_last_comment = list(comments.keys())[-1]
        fetch_user_comments(next_last_comment)
    except:
        print(f'Reached the end of comments at {len(hugeCommentsList)}')
        user_obj = result.json()
        del user_obj["posts"]
        del user_obj["comments"]
        user_details = user_obj 
        return


def fetch_user_posts(lastPostID=0):
    print(f"Fetching Posts {len(hugePostsList)}..")
    url = f"https://gateway.reddit.com/desktopapi/v1/user/{username}/posts?rtj=only&allow_over18=1&include=identity&after={lastPostID}&dist=25&sort=new&t=all"
    result = req.get(url, headers={'User-agent': 'your bot 0.2'})
    posts = result.json()["posts"]
    for id in posts:
        post = posts[id]
        if not post in hugePostsList:
            timestamp= ''.join(map(str,list(map(int,' '.join(str(post['created'])).split()))[:10]))
            post['created'] = datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d')
            hugePostsList.append(post)
    try:
        next_last_post = list(posts.keys())[-1]
        fetch_user_posts(next_last_post)
    except:
        print(f'Reached the end of posts at {len(hugePostsList)}')
        return


def save_user_details():
    print("Saving details..")
    savedComments = open(f"./{username}.json", "w")
    user_obj = {
        "comments": hugeCommentsList,
        "posts": hugePostsList,
        **user_details  # destruct
    }
    savedComments.write(json.dumps(user_obj))
    print("Done!")


def loop_on_comments():
    savedComments = json.loads(open(f"./{username}.json", "r").read())
    for comment in savedComments:
        if comment['author'] == username:
            media = comment['media']['richtextContent']['document'][0]['c'][0]
            if 't' in media:
                print(comment['author'], media['t'], datetime.fromtimestamp(
                    comment['created']).strftime('%Y-%m-%d'))


fetch_user_comments()
fetch_user_posts()
save_user_details()
# loop_on_comments()

