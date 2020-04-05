# Introudction
This project scrapes the entire public history of a Reddit user given their username,
specifically:
- Basic user information
- All comments ever made by that user
- All posts ever created by that user
- Subreddits being followed by that user

It has a function that generates a heatmap of the comments according to the date timestamp they were created at.\
The user information is saved in a JSON format.
# What is the end goal ?
To be able to analyze a person behavior based on their Reddit history using Data Science techniques.\
It's indeed a very ambitious project, but it will be a great way to learn about the basics of Data Science along the way.

# Setup
Run `pip install -r requirements.txt`.

# Usage
*Assuming you installed all the required libraries*\
Run the scraper by `py scrape.py USERNAME`\
replace `USERNAME` to a valid reddit username

After passing a valid reddit username\
`py scrape.py SilentButDeadlySquid`

If everything worked properly, you will see this :

![https://i.imgur.com/7YeZ2GX.png](https://i.imgur.com/7YeZ2GX.png)\
![https://i.imgur.com/uCRUDG0.png](https://i.imgur.com/uCRUDG0.png)

You'll find the complete data in `./output/SilentButDeadlySquid.json`

# Heatmap

![https://cdn.discordapp.com/attachments/691550010159923220/695212711122042970/x.png](https://cdn.discordapp.com/attachments/691550010159923220/695212711122042970/x.png)
