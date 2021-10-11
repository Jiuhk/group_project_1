import tweepy

consumer_key = 'N6gSTYL6SNTNqcu0uhcW2qEue'
consumer_secret = 'vfxvNvk8mvdH1GcFSAmOar5E2RXaiHnB0HGQ8CSg0eIu2mtQBG'
access_token = '2769979454-VzVkbDRQRjCxjNCuipQ2yaAcSIt6XzdSSaVH2B7'
access_token_secret = 'JtezsQUiV9EDf1ehPQm4G2i03mQbXi5637pi1QsBJCEWP'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


api = tweepy.API(auth)
user_name = 'JoeBiden'


user = api.get_user(screen_name=user_name)
print(user.followers_count)