from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
import requests
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import re
import string
import pandas as pd

consumer_key = "vda0bvGAXzcctfC03dQ5NioUD"  # twitter app’s API Key
consumer_secret = "xUffA1Jwa8Qj7Y9zoMGx6gq0ZDxJl3O8rBnUmu3H1L2B4X9Wyr"  # twitter app’s API secret Key
access_token = "705612433101037569-go3bNSZCyEg84Q1DhPsUgYw4ZHNPUMY"  # twitter app’s Access token
access_token_secret = "9UabKEkrGqPkzZh6iURtxQuTGlzjh5CxnyOfH0VxGLziu"  # twitter app’s access token secret
subscription_key = "c29c2530d7b14c1398498b8842d1c920"
endpoint = "https://eastus.api.cognitive.microsoft.com/"
sentiment_url = endpoint + "/text/analytics/v2.1/sentiment"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth_api = API(auth)


def get_tweets():
    accbl_twts = []
    my_set = {'disability', 'blindpeopleproblems', 'blindsnaps',
              'disabilityonyoutube', 'disabilityofYT', 'blindgirlbeauty',
              'worldsightday', 'Beyond2020Vision', 'blindgirlpower',
              'thingsblindgirlssay', 'disabilitiesonYT',
              'disabilitiesonyoutube', 'blindgirlstorytime',
              'accessibilitymatters', 'blindgirl', 'disabilityonYT',
              'GuideDogs', 'blindgirlproblems', 'blindgirlmoments', 'Blind',
              'accessibility', 'GuideDog', 'blindgirlwin', 'blind',
              'servicedog', 'blindgirlWIN', 'blindgirlinsta', 'deaf', 'Braille',
              'inclusion'}
    ids = set()

    count = 0
    for status in Cursor(auth_api.user_timeline, id='jennylayfluffy').items():
        count += 1
        if status.entities is not None and "hashtags" in status.entities:
            for entity in status.entities["hashtags"]:
                if entity is not None and entity["text"] is not None and \
                        entity["text"] in my_set:
                    if status.id not in ids:
                        txt = re.sub(r'http\S+', '',
                                     status.text)
                        accbl_twts.append(txt)
                        ids.add(status.id)

    count = 0
    for status in Cursor(auth_api.user_timeline, id='MollyBOfficial').items():
        count += 1
        if hasattr(status, "entities"):
            entities = status.entities
            if "hashtags" in entities:
                for ent in entities["hashtags"]:
                    if ent is not None:
                        if "text" in ent:
                            hashtag = ent["text"]
                            if hashtag is not None:
                                if hashtag in my_set:
                                    if status.id not in ids:
                                        txt = re.sub(r'http\S+', '', status.text)
                                        accbl_twts.append(txt)
                                        ids.add(status.id)

        with open("molly_tweets.txt", "w") as f:
            for item in accbl_twts:
                f.write("%s\n" % item)


def read_tweets():
    read_tweets_list = []
    count = 0
    f = open("molly_tweets.txt", "r")
    fl = f.readlines()
    for x in fl:
        t = x.strip('\n')
        t.translate(string.punctuation)
        if len(t) == 0 or len(t) == 1:
            continue
        d = {"id": count, "language": "en", "text": t}
        read_tweets_list.append(d)
        count = count + 1

    return read_tweets_list


def get_sentiment(read_tweets_list):
    scores = []
    tweets = []
    documents = {"documents": read_tweets_list}

    headers = {"Ocp-Apim-Subscription-Key": subscription_key}
    response = requests.post(sentiment_url, headers=headers, json=documents)
    sentiments = response.json()

    print("Top 10 with negative sentiment:")
    list_dict = sentiments["documents"]
    newlist = sorted(list_dict, key=lambda k: k['score'])
    for i in range(0, 10):
        val = newlist[i]['id']
        print(newlist[i]['score'], read_tweets_list[int(val)]['text'])
        scores.append(newlist[i]['score'])
        tweets.append(read_tweets_list[int(val)]['text'])

    dict = {'score': scores,
            'tweet': tweets,
            }

    df = pd.DataFrame(dict)
    df.to_csv(r'molly_negative.csv', index = None, header=True)

    scores = []
    tweets = []
    print()
    print("Top 10 with positive sentiment:")
    list_dict = sentiments["documents"]
    revlist = sorted(list_dict, key=lambda k: k['score'], reverse=True)
    for i in range(0, 10):
        val = revlist[i]['id']
        print(revlist[i]['score'], read_tweets_list[int(val)]['text'])
        scores.append(newlist[i]['score'])
        tweets.append(read_tweets_list[int(val)]['text'])

    dict = {'score': scores,
            'tweet': tweets,
            }

    df = pd.DataFrame(dict)
    df.to_csv(r'molly_positive.csv', index=None, header=True)


def generate_wordcloud():
    f = open("molly_tweets.txt", "r")
    comment_words = ' '
    stopwords = set(STOPWORDS)

    twt_read = f.readlines()
    for line in twt_read:
        txt = line.strip('\n')
        if len(txt) == 0:
            continue
        txt = re.sub(r'http\S+', '', txt)
        txt.translate(string.punctuation)
        word_tokens = txt.split()
        for i in range(len(word_tokens)):
            word_tokens[i] = word_tokens[i].lower()
        for words in word_tokens:
            comment_words = comment_words + words + ' '

    wordcloud = WordCloud(width=1600, height=800,
                          background_color='white',
                          stopwords=stopwords,
                          min_font_size=10).generate(comment_words)

    plt.figure(figsize=(20,10), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)

    plt.show()


def main():
    # get_tweets()
    # read_tweets_list = read_tweets()
    # get_sentiment(read_tweets_list)
    generate_wordcloud()


if __name__ == '__main__':
    main()
