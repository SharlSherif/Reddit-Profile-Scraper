import requests as req
import os
import json
from datetime import datetime
import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

username = sys.argv[1]

class Scrape:
    hugeCommentsList = []
    hugePostsList = []
    user_details = {}

    def main (self):
        print(f'[FETCHING] {username} data..')
        print(f"[FETCHING] POSTS..")
        self.fetch_user_posts()
        print(f"[FETCHING] COMMENTS..")
        self.fetch_user_comments()
        self.save_user_details()
        return self.user_details
    
    def fetch_user_comments(self, lastcommentID=''):
        url = f"https://gateway.reddit.com/desktopapi/v1/user/{username}/conversations?rtj=only&allow_over18=1&include=identity&after={lastcommentID}&dist=25&sort=new&t=all"
        result = req.get(url, headers={'User-agent': 'your bot 0.2'})
        comments = result.json()['comments']
        for id in comments:
            comment = comments[id]
            if not comment in self.hugeCommentsList:
                media = comment['media']['richtextContent']['document'][0]['c'][0]
                if 't' in media:
                    comment['created'] = datetime.fromtimestamp(comment['created']).strftime('%Y-%m-%d')
            self.hugeCommentsList.append(comment)
            print(f"[FETCHING] {len(self.hugeCommentsList)} -> COMMENTS..")
        try:
            next_last_comment = list(comments.keys())[-1]
            fetch_user_comments(next_last_comment)
        except:
            print(f'[=FINISHED=] FOUND {len(self.hugeCommentsList)} COMMENTS')
            user_obj = result.json()
            del user_obj["posts"]
            del user_obj["comments"]
            self.user_details = user_obj
            return self.hugeCommentsList


    def fetch_user_posts(self, lastPostID=0):
        url = f"https://gateway.reddit.com/desktopapi/v1/user/{username}/posts?rtj=only&allow_over18=1&include=identity&after={lastPostID}&dist=25&sort=new&t=all"
        result = req.get(url, headers={'User-agent': 'your bot 0.2'})
        posts = result.json()["posts"]
        for id in posts:
            post = posts[id]
            if not post in self.hugePostsList:
                timestamp= ''.join(map(str,list(map(int,' '.join(str(post['created'])).split()))[:10]))
                post['created'] = datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d')
                self.hugePostsList.append(post)
                print(f"[FETCHING] {len(self.hugePostsList)} -> POST..")
        try:
            next_last_post = list(posts.keys())[-1]
            return self.fetch_user_posts(next_last_post)
        except:
            print(f'[=FINISHED=] FOUND {len(self.hugePostsList)} POSTS')
            return self.hugePostsList


    def save_user_details(self):
        print(f"[SAVING] USER DETAILS..")
        savedComments = open(f"./output/{username}.json", "w")
        self.user_details = {
            "comments": self.hugeCommentsList,
            "posts": self.hugePostsList,
            **self.user_details  # destruct
        }
        savedComments.write(json.dumps(self.user_details))
        print(f"[SAVED] AT ./output/{username}.json")
        return self.user_details


    def loop_on_comments(self):
        savedComments = json.loads(open(f"./output/{username}.json", "r").read())
        for comment in savedComments:
            if comment['author'] == username:
                media = comment['media']['richtextContent']['document'][0]['c'][0]
                if 't' in media:
                    print(comment['author'], media['t'], datetime.fromtimestamp(
                        comment['created']).strftime('%Y-%m-%d'))

    def structure_commentslist (self):
        comments = self.hugeCommentsList
        commentsList = {}
        max_length = 0
        for comment in comments:
            created=comment['created']
            if created not in commentsList:
                commentsList[created] = [1] # thats count 1
            else:
                if type(commentsList[created]) == int:
                    new_value = [commentsList[created]]
                else:
                    new_value = commentsList[created]
                    
                last_elem = new_value[len(new_value)-1]
                new_value.append(last_elem+1)
                if len(new_value) > max_length:
                    max_length=len(new_value)
                commentsList[created] = new_value

        for id in commentsList:
            list = commentsList[id]
            if len(list) < max_length:
                additional = [0] * (max_length - len(list))
                commentsList[id] += additional
        return {'commentsList':commentsList, 'max_length':max_length}
    
    def generate_heatmap(self, type) :
        array = []
        max_length = 1
        if type == 'posts':
            List = self.structure_commentslist()
            array = List['commentsList']
            max_length = List['max_length']
        # else if type == 'comments':
            
        structured = pd.DataFrame(array, index=[i for i in range(0, max_length)])
        plt.figure(figsize=(100,300))
        plt.title("Average Arrival Delay for Each Airline, by Month")
        ax = sns.heatmap(structured,annot=True,square=True)
        sns.set(font_scale=1)

scraper = Scrape()
scraper.main()
scraper.generate_heatmap('posts')