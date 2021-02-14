import tweepy
import os
import mysql.connector
import datetime
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

consumer_key = os.environ.get('CONSUMER_KEY')
consumer_secret = os.environ.get('CONSUMER_SECRET')
access_key = os.environ.get('ACCESS_KEY')
access_secret = os.environ.get('ACCESS_SECRET')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

print("stat_get_twitter_status")

try:

    # DBcon
    conn = mysql.connector.connect(
        host='0.0.0.0',
        port='3306',
        user='user',
        password='password',
        database='schema',
        charset='utf8mb4'
    )

    cur = conn.cursor(buffered=True)

    user = api.get_user("FIN4LE_P")

    toDayDate = datetime.datetime.today()
    twitCount = user.statuses_count
    followCount = user.friends_count
    followerCount = user.followers_count
    favoCount = user.favourites_count

    cur.execute("INSERT INTO TWITTER_STATUS VALUES (%s, %s, %s, %s, %s)",(toDayDate, twitCount, followCount, followerCount, favoCount))
    conn.commit()

except tweepy.error.TweepError as e:
    print("err")
    print(e.reason)
except mysql.connector.Error as e:
    print("SQLSTATE value:", e.sqlstate)  # SQLSTATE value
    print("Error message:", e.msg)       # error message
    print("Error code:", e.errno)        # error number
    print("Error:", e)                   # errno, sqlstate, msg values
    s = str(e)
    print("Error:", s)                   # errno, sqlstate, msg values
finally:
    cur.close()
    conn.close()

print("success")