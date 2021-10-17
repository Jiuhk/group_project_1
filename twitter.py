import tweepy
import sqlite3

# keys to authenticate
consumer_key = 'N6gSTYL6SNTNqcu0uhcW2qEue'
consumer_secret = 'vfxvNvk8mvdH1GcFSAmOar5E2RXaiHnB0HGQ8CSg0eIu2mtQBG'
access_token = '2769979454-VzVkbDRQRjCxjNCuipQ2yaAcSIt6XzdSSaVH2B7'
access_token_secret = 'JtezsQUiV9EDf1ehPQm4G2i03mQbXi5637pi1QsBJCEWP'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


# initialize API via Tweepy
api = tweepy.API(auth)
user_name = 'JoeBiden'


# get Joe Biden's user object
user = api.get_user(screen_name=user_name)


# get Joe Biden's tweets 
tweets = api.user_timeline(screen_name=user_name, 
                           count=20,
                           include_rts = True,
                           tweet_mode = 'extended')


# get Joe Biden's friends
friends = api.get_friends(screen_name=user_name, count=100)


# initialize db
db_file = r'twitter.db'
db = sqlite3.connect(db_file)
c = db.cursor()
# for traceback: db.set_trace_callback(print)


# create table 'profile' to store profile if not exists
# c.execute("DROP TABLE profile")
c.execute('''CREATE TABLE IF NOT EXISTS profile (
            screen_name VARCHAR(40),
            id INTEGER,
            name VARCHAR(40),
            location VARCHAR(20),
            url VARCHAR(50),
            description TEXT,
            followers_count INTEGER,
            friends_count INTEGER,
            statuses_count INTEGER,
            created_at VARCHAR(30)
            );''')

c.execute('''
insert into profile (name) values ('Karen')
''')

# store Joe Biden's information into profile:

joe_biden = c.execute("SELECT * FROM profile WHERE id = ?;", tuple([user.id]))
if len(c.fetchall()) == 0:     # if joe biden record not exists

    c.execute('''INSERT INTO profile
                (screen_name, id, name, location,
                url, description, followers_count,
                friends_count, statuses_count,
                created_at)
                VALUES (?, ?, ?, ?, ?, ?,
                ?, ?, ?, ?);''', (user.screen_name,
                user.id, user.name, user.location, user.url,
                user.description, user.followers_count,
                user.friends_count, user.statuses_count, user.created_at))


# create table 'following' to store friends of Joe Biden

# store Joe Biden's friends into following
for friend in friends:
    friend_test = c.execute("SELECT * FROM following WHERE id = ?;", tuple([friend.id]))
    if len(c.fetchall()) == 0:     # if friend record not exists
        c.execute('''INSERT INTO following
                    (screen_name, id)
                    VALUES (?, ?)''', (friend.screen_name, friend.id))


# create table 'jbTweets' to store all tweets from Joe Biden
c.execute('''CREATE TABLE IF NOT EXISTS jbTweets(
             TweetsID INT,
             CreatedAT DATE,
             FullText TEXT,
             Likes INT,
             Retweets INT,
             Comments INT
             );''')



# export tweets to json
from collections import defaultdict
l = defaultdict(list)
print(len(tweets))
elms = ['id', 'full_text', 'created_at', 'favorite_count', 'retweet_count']
for post in tweets:
    for elm in elms:
        l[elm].append(post._json[elm])
    

import pandas as pd
df = pd.DataFrame(l)
pd.set_option('max_columns', None)
print(df)
db.commit()

db.close()
