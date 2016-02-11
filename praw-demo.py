import praw #import the Python Reddit API to use in our script
import urllib #used to download our images

client = praw.Reddit(user_agent='sample_thing')
submissions = client.get_subreddit('wallpapers').get_hot(limit=10)
#iterate over submission objects
for index, sub in enumerate(submissions):
    # print dir(sub) to see all attributes of the 'submission' object
    url = sub.url
    print url
    #if url ends with image file extension, it is a single image, we can download it!
    if url.endswith('.jpg' or '.png'):
        #my desired local file name is the index
        #plus a '.' plus the image's extension
        local_file_name = str(index) + '.' + url.split('.')[-1]
        #urllib.urlretrieve(<url>, <desired-local-filename>)
        urllib.urlretrieve(url, local_file_name)
