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
                           count=1,
                           include_rts = False,
                           tweet_mode = 'extended')


# initialize db
db_file = r'twitter.db'
db = sqlite3.connect(db_file)
c = db.cursor()
db.set_trace_callback(print)

# create table to store profile if not exists
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

c.execute('drop table profile')

db.commit()

db.close()
