"""
Dataset Creation Module.
"""
import snscrape.modules.twitter as sntwitter
import pandas as pd

# The following lists contain the twitter users of each political leaning.
right = ["joerogan", "RepMTG", "laurenboebert", "SenRickScott", "RonDeSantisFL", "JesseBWatters", "TuckerCarlson",
        "PierrePoilievre", "ABDanielleSmith", "LindseyGrahamSC", "FoxNews", "benshapiro", "LeaderMcConnell",
        "fordnation", "SenShelby", "lisamurkowski", "SenDanSullivan", "SenTomCotton", "JohnBoozman", "marcorubio",
        "MikeCrapo", "SenatorRisch", "ChuckGrassley", "joniernst", "JerryMoran", "RandPaul", "BillCassidy",
        "SenJohnKennedy", "SenatorCollins", "SenHydeSmith", "SenatorWicker", "SteveDaines", "SenatorFischer",
        "BenSasse", "SenatorBurr", "SenThomTillis", "SenJohnHoeven", "senrobportman", "JimInhofe",
        "SenatorLankford",
        "SenToomey", "GrahamBlog", "SenatorTimScott", "SenatorRounds", "JohnCornyn", "SenTedCruz", "SenCapito",
        "SenRonJohnson", "SenJohnBarrasso", "SenLummis"]

left = ["AOC", "JustinTrudeau", "cafreeland", "CNN",
         "theJagmeetSingh", "RachelNotley", "NBCNews", "SenMarkKelly", "TheYoungTurks", "SenFeinstein",
         "ChrisMurphyCT",
         "SenBlumenthal", "SenatorCarper", "ChrisCoons", "brianschatz", "maziehirono", "SenDuckworth",
         "SenatorDurbin",
         "ChrisVanHollen", "SenatorCardin", "SenMarkey", "SenWarren", "SenStabenow", "amyklobuchar", "SenTinaSmith",
         "SenatorTester", "SenCortezMasto", "SenatorShaheen", "SenatorHassan", "CoryBooker", "MartinHeinrich",
         "SenGillibrand", "SenSherrodBrown", "RonWyden", "SenJeffMerkley", "SenBobCasey", "SenJackReed",
         "SenWhitehouse", "SenatorLeahy", "timkaine", "MarkWarner", "PattyMurray", "SenatorCantwell",
         "Sen_JoeManchin",
         "SenatorBaldwin", "gillibrandny", "SenatorLujan", "SenatorHick", "SenatorSinema", "SenAlexPadilla"]

left_test = ["GdnPolitics", "suzemorrison", "BarackObama", "BillGates", "BernieSanders", "HillaryClinton", "NDP",
             "macleans", "CBCPolitics", "MSNBC"]

right_test = ["BreitbartNews", "NEWSMAX", "OANN", "seanhannity", "IngrahamAngle", "jkenney", "globeandmail",
              "calgarysun", "prageru", "ChristianPost"]


def create_aligned_dataset(user_list: list, file_name: str, align_right: bool, create_csv: bool):
    """
    Create a dataset from a list of users.

    Grabs the most recent 100 tweets from each user. Users in user_list should all be of the same political leaning.

    :param create_csv: bool, True if output file is desired else False
    :param user_list: list, containing the twitter handles of the users
    :param file_name: string, desired name of the output file
    :param align_right: bool, True if users lean right, else False
    :return: a copy of the dataset as a pd.DataFrame
    """
    user_tweet_list = []
    tweet_limit = 100
    alignment = -1 if align_right else 1

    # Loop for getting tweets
    print("Retrieving Tweets...")
    for i in range(len(user_list)):
        tweet_list = []
        for tweet in sntwitter.TwitterUserScraper(user_list[i]).get_items():
            if len(tweet_list) < tweet_limit:
                tweet_list.append(tweet.content)
            else:
                break
        user_tweet_list.append([user_list[i], tweet_list, alignment])
    print("All Tweets Retrieved.")
    data = pd.DataFrame(user_tweet_list, columns=['User', 'Content', 'Alignment'])
    if create_csv:
        data.to_csv(file_name)
    return data


def main():
    """
    Drive the program.

    :return: None
    """
    # left_set = pd.read_csv("left_set.csv")
    # right_set = pd.read_csv("right_set.csv")
    # final_set = pd.merge(left_set, right_set, how="outer")
    # final_set.head()
    # final_set.to_csv("custom_set.csv")

    create_aligned_dataset(left_test, "datasets/left_set_test.csv", False, True)
    create_aligned_dataset(right_test, "datasets/right_set_test.csv", True, True)
    left_set_test = pd.read_csv("datasets/left_set_test.csv")
    right_set_test = pd.read_csv("datasets/right_set_test.csv")
    final_set_test = pd.merge(left_set_test, right_set_test, how="outer")
    final_set_test.head()
    final_set_test.to_csv("final_test_set.csv")
    return


if __name__ == "__main__":
    main()
