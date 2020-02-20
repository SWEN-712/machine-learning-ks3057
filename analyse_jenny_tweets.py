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


def get_tweets_simple():
    jenny_tweets = auth_api.user_timeline(screen_name='jennylayfluffy',
                                          count=600, include_rts=False,
                                          tweet_mode='extended')

    final_tweets = [each_tweet.full_text for each_tweet in jenny_tweets]
    with open("jenny_tweets.txt", "w") as f:
        for item in final_tweets:
            f.write("%s\n" % item)


def get_tweets():
    accbl_twts = []
    ids = set()
    hashtags = set()
    j_hashtags = {'hearingadvocacy', 'USBLN16', 'WorldBrailleDay',
              'RepresentationMatters', 'Oscars2017', 'design', 'MSEnvision',
              'endals', 'MSInspire', 'WEDay',
              'AbilitySummit', 'microsofttranslator', 'NOWHITEFLAGS', 'NFB15',
              'Disabilityconfident',
              'KNFBReader', 'IDSL2018', 'MSFTGarage', 'CodeJumper', 'A11Y',
              'INForInclusion', 'DiversityandTech',
              'DriveforInclusion', 'OneNote', 'GDPR',
              'OfficeInsiders', 'DeafLeaders', 'FCC',
              'dyslexia', 'marmitethrone', 'BeFearless', 'CelebratingChampions',
              'usabilityTest', 'mEnabling19', 'DeafOutLoud',
              'AccessibilityAct', 'Rio2016', 'InsideXbox', 'Azure', 'WinML',
              'AIForAccessibility', 'career', 'inclusive_design', 'blind',
              'Deaf',
              'ChangetheWorld', 'inclusivetech', 'DiversityandInclusion',
              'Pride', 'AI', 'technology', 'MSBuild',
              'SmartCity', 'inclucity', 'disabilityemployment',
              'signlanguage', 'usbln15', 'MSEnvisionForum', 'Office365', 'asl',
              'XboxGC', 'EyeControl', 'StarbucksSigns', 'disabilities',
              'windowsCE','BEdeaffriendly',
              'Accessibility',
              'aapd', 'deaf', 'philanthropy', 'oscarsnerd', 'NAD',
              'LearningTogether', 'sketchnotes', 'XboxAdaptiveController',
              'g3ict',
              'GameChanger', 'call4brain', 'IDPD2016', 'DisabilityRights',
              'SeeingAI', 'Gears5', 'microsoftlife', 'cosp11',
              'AutismDay2016', 'UniteForParkinsons', 'inclusion', 'BREAKING',
              'MakeWhatsNext', 'SignLanguagesDay', 'Wired25', 'HackMars',
              'usbln17', 'chi2017', 'inclusivedesign', 'deaftalent',
              'AXSChat', 'STEM', 'AT_APPG',
              'Specialized', 'Inclusion', 'eyetrackingforwindows',
              'MicrosoftAbilitySummit', 'lalege',
              'Microsofts', 'autumncolors', 'colorblind', 'WEareOne', 'CAO',
              'britsabroad', 'LondonStrong', 'ChooseToInclude', 'Accessiblity',
              'assistivetech', 'designforall', 'Autism',
              'beforeandafter', 'WorldsMostEthicalCompanies', 'hurricaneharvey',
              'guidedogsawards', 'CRPD', 'AbilityHacks', 'Chester', 'vacation',
              'lovemyteam', 'CitiesUnlocked', 'ability2016', 'ZeroCon19',
              'ada25',
              'Accessible', 'IDPD2019', 'neverwashingmycheek', 'g4ebootcamp',
              'FutureDecoded', 'A11y', 'Hamiltunes', 'axschat',
              'deafgain', 'SBLIV', 'HLAA2016',
              'AutismAdvantage',
              'IT', 'RisingLeaders', 'SeeAmazing', 'Pride2017',
              'SCOTUS',
              'wheelchairinmotion', 'inspiration', 'GnomeLastedFiveMinutes',
              'MicrosoftAI', 'Obama', 'ADA', 'InclusiveDesign',
              'Blind',
              'ATIA19', 'PartiallySighted',
              'EdRobertsDay','JustDoIt', 'USBLN', 'Skype', 'accessibilty',
              'inclusivehiring', 'SignLanguageWeek', 'ADA27',
              'abilityhack',
              'CSUNATC18', 'BritAbroadDrama', 'WAAD', 'LA2015',
              'ndcautism16', 'SCNYC17',
              'WorldAutismAwarenessDay', 'accessible', 'disabilityisastrength',
              'hackathon', 'DeafProblems', 'GAAD',
              'disability', 'cfasummit', 'MSIgnite', 'socialgood', 'EyeMine',
              'AwesomeAintEasy', 'access', 'USBLN17', 'Dreamers',
              'Build2017', 'autismatwork',
              'noexcuse', 'X019', 'IWDeaf2018',
              'NonVisibleDisabilities', 'Disability', 'MicrosoftEDU',
              'Disabilities', 'InsiderFast', 'USBLN18',
              'inclusionworks', 'individuality', 'CSUNATC17',
               'ImagineCup', 'tech',
              'AccessibilityTips', 'wheelchair', 'MinecraftEDU', 'Gamescom2019',
              'business', 'HitRefresh', 'empowering', 'cfa16', 'cpchat',
              'TEDTalk',
              'xboxa11y', 'SpecialOlympics', 'E2',
              'deaffriendly',
              'IronMan', 'October1st', 'WHChamps', 'bobbi4GU', 'innovation',
              'SBLIII', 'worldbrailleday', 'lead', 'Invention', 'PSBJCorpCit',
              'WAAD2015', 'autism',
              'MicrosoftEvent',
              'WindowsTip', 'AbilityAward', 'ALSicebucketchallenge', 'WinHEC',
              'Outlook', 'DesignForAll', 'MostAdmired', 'HoloLens',
              'pALS', 'Gameon', 'a11ycampseattle', 'PR',
              'Neurodiversity', 'code', 'Paralympics', 'Bett2018',
              'GleasonMovie',
              'DigitalInclusion', 'microsoft', 'LearningTools', 'GLEASON',
              'AssistiveTechnology', 'jobs', 'DisabilityConfident',
              'TeamGleason',
              'USBLN2015', 'PWA', 'neurodiverse', 'InclusionAward',
              'AbilityWeek',
              'NewTenPoundNote',
              'MSFTSummit', 'CSUNATC19', 'DisAbility', 'DigitalTransformation',
              'NFBWATD', 'likeadyslexic',
              'DeepLearning', 'nowhiteflags', 'TEDxGlasgow2015', 'trust',
              'OfficeforCats', 'linus', 'CBeebies', 'Tech4GoodAwards', 'CSUN18',
              'GAconf', 'BillyT', 'EdTech', 'nonprofits', 'sxsw',
              'GoHawks', 'ForbesUnder30', 'WSD2017', 'SXSW2019', 'fail',
              'DeafAwarenessMonth', 'WoV15', 'msignite2017', 'Apple',
              'WorldStandardsDay', 'IDPD', 'MsIgnite', 'lovemyjob', 'MIEExpert',
              'AltText', 'accessibility', 'rword', 'Word', 'Sundance', 'SOTU',
              'ADA25', 'InternationalLiteracyDay', 'AmericanSignLanguage',
              'ally',
              'AGT',
              'TheFeed', 'NDEAM', 'MicrosoftStream', 'MicrosoftTeams', 'PSA',
              'edchat', 'Braille', 'HKAA18', 'mentalhealthtreatment',
              'aprilfoolsday', 'ignite2017', 'CSUN', 'MondayMotivation',
              'Minecraft',
              'employment',
              'a11y', 'SeattlePride', 'WomensMarchSeattle', 'Microsoft',
              'AgainstAllOdds', 'inclusive', 'windows',
              'VivaTech',
              'IWD2017', 'AutismAtWork', 'SurfacePro', 'ID24',
              'DisabilityAnswerDesk', 'Johnscrazysocks', 'hardofhearing',
              'AACAwarenessMonth', 'StrikeOutALS', 'HumanRightsDay',
              'AutismAwarenessMonth', 'aoda', 'WIRED25', 'teamgleason',
              'Ability2016', 'SkypeTranslator', 'SXSW', 'BillyTNinjacat',
              'edtech',
              'Redmond', 'InclusiveEducation', 'Nominations', 'abilitysummit',
              'InternationalDisabilityDay', 'MVPSummit', 'CommunityStory',
              'ImmersiveReader',
              'grateful', 'UpgradeYourWorld', 'GlobalAccessibilityAwarenessDay',
              'SmartCities', 'InclusionInAction', 'CSUN16', 'windowsinsider',
              'InclusivetheFilm', 'learningtools', 'PurpleTuesday', 'IDPD2015',
              'EUAccessCity', 'Inclusivethefilm', 'hearingloss', 'loveit',
              'disabilityinclusion',
              }

    count = 0
    for status in Cursor(auth_api.user_timeline, id='jennylayfluffy').items():
        count += 1
        if status.entities is not None and "hashtags" in status.entities:
            for entity in status.entities["hashtags"]:
                if entity is not None and entity["text"] is not None and \
                        entity["text"] in j_hashtags:
                    if status.id not in ids:
                        txt = re.sub(r'http\S+', '',
                                     status.text)
                        accbl_twts.append(txt)
                        ids.add(status.id)
                    hashtags.add(entity["text"])

    print("total tweets", count)
    print("total accessibility related tweets", len(accbl_twts))

    with open("jenny_tweets.txt", "w") as f:
        for item in accbl_twts:
            f.write("%s\n" % item)


def read_tweets():
    read_tweets_list = []
    count = 0
    f = open("jenny_tweets.txt", "r")
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
    print(sentiments)

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
    df.to_csv(r'jenny_negative.csv', index = None, header=True)

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
    df.to_csv(r'jenny_positive.csv', index=None, header=True)


def generate_wordcloud():
    f = open("jenny_tweets.txt", "r")
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

    wordcloud = WordCloud(width=800, height=800,
                          background_color='white',
                          stopwords=stopwords,
                          min_font_size=10).generate(comment_words)

    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)

    plt.show()


def main():
    get_tweets_simple()
    read_tweets_list = read_tweets()
    get_sentiment(read_tweets_list)
    generate_wordcloud()


if __name__ == '__main__':
    main()
