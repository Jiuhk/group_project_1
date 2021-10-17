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


# store Joe Biden's information into profile:

joe_biden = c.execute("SELECT * FROM profile WHERE id = :id;", {'id': user.id})
if len(c.fetchall()) == 0:     # if joe biden record not exists

    c.execute('''INSERT INTO profile
                (screen_name, id, name, location,
                url, description, followers_count,
                friends_count, statuses_count,
                created_at)
                Values (?, ?, ?, ?, ?, ?,
                ?, ?, ?, ?);''', (user.screen_name,
                user.id, user.name, user.location, user.url,
                user.description, user.followers_count,
                user.friends_count, user.statuses_count, user.created_at))



# create table jbTweets to store all tweets from Joe Biden
c.execute('''CREATE TABLE IF NOT EXISTS jbTweets(
             TweetsID INT,
             CreatedAT DATE,
             FullText TEXT,
             Likes INT,
             Retweets INT,
             Comments INT
             );''')


# store 


# save all the above changes to db
db.commit()

# close db
db.close()
