# mongo configurations
MONGODB = dict(
    hostname = "localhost",
    port = 27017,
    db = 'tweets',
    collection = 'test'
)

# Create twitter app to access Twitter Streaming API (https://apps.twitter.com)
TWITTER = dict(
    consumer_key = '',
    consumer_secret = '',
    access_token = '',
    access_secret = ''
)

# Elasticsearch configurations
ELASTICSEARCH = dict(
    hostname = "localhost:9200",
    new_hostname = "localhost:9200",
    index = "tweets_en",
    type = "doc_en"
)

# Emotion hashtags keywords (change these to your own keywords, as many as you can)
KEYWORDS = dict( joy = [
"#accomplished",
"#alive",
"#amazing",
"#awesome"],
trust = [
"#acceptance",
"#admiration",
"#amused",
"#appreciated"],
fear = [
"#afraid",
"#anxious",
"#apprehension"],
surprise = [
"#amazed",
"#amazement",
"#crazy",
"#different"],
sadness = [
"#alone",
"#ashamed",
"#awful"],
disgust = [
"#bitter",
"#blah",
"#bored"
"#boredom"],
anger = [
"#aggravated",
"#aggressiveness",
"#anger",
"#anger2",
"#angry"],
anticipation = [
"#adventurous",
"#anticipation",
"#curious"],
other = [
"#asleep",
"#awake",
"#brave",
"#busy"])
