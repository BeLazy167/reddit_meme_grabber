import praw
import urllib.request
def meme_installer():
    meme_list = list()
    title_list = list()
    reddit = praw.Reddit(client_id = "OZsROIAyH5bAbA" ,client_secret = 'PhYFLRgpllL3ZPpdIQe3D5yhRWc' ,username = "DK00167",password = "98766789" ,user_agent ="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36")
    memes = reddit.subreddit("memes")
    hotmemes = memes.top(limit = 20)
    for meme in hotmemes:
        meme_list.append(meme.url)
        title_list.append(meme.title)


    return meme_list, title_list
