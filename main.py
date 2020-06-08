import random
import urllib.request
import reddit as m
def download_image(url,title):
    try:
        fullname = str(title[0:9])+".jpg"
        urllib.request.urlretrieve(url,fullname)
    except: print("error")
meme_url,title_list  = m.meme_installer()
for i in range(0, len(title_list) ):
    #download_image(meme_url[i], title_list[i])
    print( meme_url[ i ], title_list[ i ] )
