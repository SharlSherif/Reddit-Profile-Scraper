# Introduction
This project scrapes the entire public history of a Reddit user given their username,
specifically:
- Basic user information
- All comments ever made by that user
- All posts ever created by that user
- Subreddits being followed by that user

It has a function that generates a heatmap of the comments according to the date timestamp they were created at. The user information is saved in a JSON format.
# What is the end goal ?
To be able to analyze a person behavior based on their Reddit history using Data Science techniques.\
It's indeed a very ambitious project, but it will be a great way to learn about the basics of Data Science along the way.

# Setup
Have Python 3.x installed and run `pip3 install -r requirements.txt`.

# Usage
```
python3 scrape.py [reddit username]
```

If everything worked properly, you will see something like:

```
[FETCHING] [reddit username] data..
[FETCHING] POSTS..
[FETCHING] 1 -> POST..
[FETCHING] 2 -> POST..
...
[FETCHING] 32 -> POST..
[=FINISHED=] FOUND 32 POSTS
[FETCHING] COMMENTS..
[FETCHING] 1 -> COMMENTS..
[FETCHING] 2 -> COMMENTS..
...
[FETCHING] 38 -> COMMENTS..
[=FINISHED=] FOUND 38 COMMENTS
[SAVING] USER DETAILS..
[SAVED] AT ./output/[reddit username].json
```

Then, you will find the complete data in `./output/[reddit username].json`

# Heatmap

![https://cdn.discordapp.com/attachments/691550010159923220/695212711122042970/x.png](https://cdn.discordapp.com/attachments/691550010159923220/695212711122042970/x.png)
