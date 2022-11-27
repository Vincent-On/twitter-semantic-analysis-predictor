import snscrape.modules.twitter as sntwitter
from nltk.tokenize import TweetTokenizer
import pandas as pd

tweet_tokenizer = TweetTokenizer()
query = ["joerogan", "RepMTG", "laurenboebert", "SenRickScott", "RonDeSantisFL", "JesseBWatters", "TuckerCarlson",
         "PierrePoilievre", "ABDanielleSmith", "LindseyGrahamSC", "FoxNews", "benshapiro", "LeaderMcConnell",
         "fordnation", "SenShelby", "lisamurkowski", "SenDanSullivan", "SenTomCotton", "JohnBoozman", "marcorubio",
         "MikeCrapo", "SenatorRisch", "ChuckGrassley", "joniernst", "JerryMoran", "RandPaul", "BillCassidy",
         "SenJohnKennedy", "SenatorCollins", "SenHydeSmith", "SenatorWicker", "SteveDaines", "SenatorFischer",
         "BenSasse", "SenatorBurr", "SenThomTillis", "SenJohnHoeven", "senrobportman", "JimInhofe", "SenatorLankford",
         "SenToomey", "GrahamBlog", "SenatorTimScott", "SenatorRounds", "JohnCornyn", "SenTedCruz", "SenCapito",
         "SenRonJohnson", "SenJohnBarrasso", "SenLummis", "AOC", "JustinTrudeau", "cafreeland", "CNN",
         "theJagmeetSingh", "RachelNotley", "NBCNews", "SenMarkKelly", "TheYoungTurks", "SenFeinstein", "ChrisMurphyCT",
         "SenBlumenthal", "SenatorCarper", "ChrisCoons", "brianschatz", "maziehirono", "SenDuckworth", "SenatorDurbin",
         "ChrisVanHollen", "SenatorCardin", "SenMarkey", "SenWarren", "SenStabenow", "amyklobuchar", "SenTinaSmith",
         "SenatorTester", "SenCortezMasto", "SenatorShaheen", "SenatorHassan", "CoryBooker", "MartinHeinrich",
         "SenGillibrand", "SenSherrodBrown", "RonWyden", "SenJeffMerkley", "SenBobCasey", "SenJackReed",
         "SenWhitehouse", "SenatorLeahy", "timkaine", "MarkWarner", "PattyMurray", "SenatorCantwell", "Sen_JoeManchin",
         "SenatorBaldwin", "gillibrandny", "SenatorLujan", "SenatorHick", "SenatorSinema", "SenAlexPadilla"]

user_tweet_list = []
tweet_list = []
tweet_limit = 100

for i in range(len(query)):
    username = f'https://twitter.com/{query[i]}'
    for tweet in sntwitter.TwitterUserScraper(query[i]).get_items():

        if len(tweet_list) < tweet_limit:
            tokenized_tweet = tweet_tokenizer.tokenize(tweet.content)
            tweet_list.append(tokenized_tweet)
        else:
            break
    user_tweet_list.append([username, tweet_list])
    tweet_list = []

data = pd.DataFrame(user_tweet_list, columns=['User', 'Content'])
alignment = ["right" if i < (len(query)/2) else "left" for i in range(len(query))]

data["alignment"] = alignment


data.to_csv("dataset.csv")
