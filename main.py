import time


def read_text_file_and_search_keyword(keyword):

    user_tweet_list = []
    user_mentions = []
    user_hashtags = []
    user_sentiments = []

    with open("G:/Downloads/twitter-data-timpestamped.txt", encoding='utf8') as datafile:

        # data = csv.reader(csvfile)

        line = datafile.readline()

        start = time.perf_counter()

        counter = 1
        while line:

            if keyword in line:

                user_tweet = add_user(line)

                if user_tweet is not None:

                    user_tweet_list.append((user_tweet, counter))

                    mention = add_user_mention(line)
                    hashtags = add_user_hashtags(line)

                    # if any(ele in line for ele in sentiments_list):
                    #     user_sentiments.append(add_user_sentiment(line))

                    # if mention is not None means if the list of mentions is greater than 1
                    if mention is not None:
                        user_mentions.append(mention)

                    if hashtags is not None:
                        user_hashtags.append(hashtags)

                    counter += 1

            # user_tweet_list.append((add_user(line), counter))

            line = datafile.readline()

        end = time.perf_counter()

        print("Parsed data in {} seconds".format(end - start))

    # user_tweet_list.remove(None)

    return user_tweet_list, user_mentions, user_hashtags, user_sentiments

def add_user(tweet):

    final_tweet_list = []

    tweet_list = tweet.split("|")
    #print(tweet_list[1])

    try:

        final_tweet_list = [(tweet_list[1], tweet_list[2])]

        # if tweet_list[2] == "":
        #
        #     print(tweet_list)
        #     print(tweet)

    except:

        pass

    if len(final_tweet_list) != 0:

        #return final_tweet_list
        #return [tweet_list[1], tweet_list[2]]
        return tweet_list[1]


def add_user_mention(tweet):

    mention_list = []

    temp_list = []

    temp_list = tweet.split('|')
    temp_list.pop(0)

    temp_list2 = []

    for items in temp_list:

        temp_list2.append(items.split())

    for x in temp_list2:

        for y in x:

            if y.startswith('@'):

                if y.endswith(':'):

                    y = y[0:len(y) - 1]

                mention_list.append(y)

    if len(mention_list) == 1:

        return None

    return mention_list


    #print(mention_list)


def add_user_hashtags(tweet):

    user_hashtags = []

    temp_list = tweet.split('|')
    #print(temp_list)

    user_hashtags.append(temp_list[1])

    for x in temp_list[2].split():

        if x.startswith('#'):

            user_hashtags.append(x)

    #print(user_hashtags)

    if len(user_hashtags) == 1:

        return None

    else:

        return user_hashtags


# def add_user_sentiment(tweet):
#
#     word = [sentiment for sentiment in sentiments_list if(sentiment in tweet)]
#
#     user = tweet.split('|')[1]
#
#     return (user, word[0].strip())