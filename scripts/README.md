## Twitter Crawler
The following crawler helps you to stream and store tweets from the [Twitter API](https://developer.twitter.com/en/docs.html) based on hashtag keywords. The keyword basically play the role of a filter, where the tweets collected are only those that contain any of the keywords in the list provided. 

---
## How To Make it Work!
- First, you need a database to store your tweets. The crawler already supports the ability to store tweets in both Elasticsearch and MongoDB. On that note, the crawler assumes that you have installed all the necessary libraries and software to stream and store. The crawler stores tweets in tthe following `json` format: 

    `{'hashtags': [], 'tweet_id': '1052497792675926022', 'created_at': 'Wed Oct 17 09:53:22 +0000 2018', 'text': 'I wanawanawanawanawanawanawanawanawanawana be a super star be a be a super star'}`

- Then you can configure the `config.py` file and provide the necessary configurations to store you data. You can also provide the keywords you will search for on the Twitter Streaming API.

- The following are the configurations you need to add yourself:
    - MongoDB settings:
    ```python
        MONGODB = dict(
            hostname = '<hostname>',
            port = 27017,
            db = '<db_name>',
            collection = '<collection_name>'
        )
    ```
    - Twitter API keys (you can get your own [here](https://apps.twitter.com/))
    ```python
        TWITTER = dict(
            consumer_key = '<consumer_key>',
            consumer_secret = '<consumer_secret>',
            access_token = '<access_token>',
            access_secret = '<access_secret>'
        )
    ```
    - Elasticsearch settings:
    ```python
        ELASTICSEARCH = dict(
            hostname = "localhost:9200",
            new_hostname = "localhost:9200",
            index = "tweets_en",
            type = "doc_en"
        )
    ```
    - Keyword filters:
    ```python
    KEYWORDS = dict( 
        joy = ["#hashtag1", "#hashtag2",...],
        trust = ["#hashtag1", "#hashtag2",...],
        fear = ["#hashtag1", "#hashtag2",...],
        surprise = ["#hashtag1", "#hashtag2",...],
        sadness = ["#hashtag1", "#hashtag2"...],
        disgust = ["#hashtag1", "#hashtag2",...],
        anger = ["#hashtag1", "#hashtag2",...],
        anticipation = ["#hashtag1", "#hashtag2",...],
        other = ["#hashtag1", "#hashtag2",...]
    )
    ```

- After you have configured the file above, you should be ready to run the script, using the following command: 

    `python twitter_crawler.py`
    
- Pay attention to the `twitter_crawler.py` script as currently it is only set to store tweets on a MongoDB. You can change these settings in the script by yourself. 

---
## Citation

If you are using this crawler for research purposes please include the following paper citation:

Elvis Saravia, Hsien-Chi Toby Liu, Yi-Shin Chen, DeepEmo: Learning and Enriching Pattern-Based Emotion Representations [arXiv:1804.08847](https://arxiv.org/abs/1804.08847), 2018.

---
## Author
[Elvis Saravia](https://twitter.com/omarsar0)
