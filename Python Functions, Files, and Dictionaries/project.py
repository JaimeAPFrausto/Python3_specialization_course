# definitions
# Creating a strip punctuation function 
def strip_punctuation(string):
# iterating through the string
    for item in punctuation_chars:
# replace punctuation with a space if its contained in string
        string = string.replace(item, '')
# Return string
    return string
# creating get_pos definition
def get_pos(str_sentences):
# making sentences lower case
    str_sentences = str_sentences.lower()
# run line through the strip definition
    lines = strip_punctuation(str_sentences)
# counting variable
    count_positive = 0
# iterating through words and increasing positivie count if words in positive_words is true
    for words in lines.split():
        if words in positive_words:
            count_positive += 1
    return count_positive

def get_neg(str_sentences):
# making sentences lower case
    str_sentences = str_sentences.lower()
# run each line through the strip definition
    lines = strip_punctuation(str_sentences)
# counting variable
    count_negative = 0
# Iterate through words and increasing negative count if words in negative_words is true
    for words in lines.split():
        if words in negative_words:
            count_negative += 1
    return count_negative
#---------------------------------------------------------------------------
# Begin  project code
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
#---------------------------------------------------------------------------
# lists for tweet texts, replies, retweets and scores
tweet_text = []
tweet_replies = []
tweet_retweets = []
positive_scores = []
negative_scores = []
net_scores = []
# opening twitter data
with open("project_twitter_data.csv") as twitter_data:
    lines = twitter_data.readlines()[1:]
    for line in lines:
# splitting tweets line by line
        words = line.split(",")
# making all tweets into tuples and appending them to tweet_texts
        for tweets in words[0:1]:
            word = tweets.split()
            aTuple = tuple(word)
            tweet_text.append(aTuple)
# appending the number of retweets to tweet_retweets
        tweet_retweets.append(words[1].strip())
# appending then number of replies to tweet_replies
        tweet_replies.append(words[2].strip())
#---------------------------------------------------------------------------
# calculating positive scores and negative scores for each tweet
for items in tweet_text:
# counting variables
    positive = 0
    negative = 0
# iterating items and counting each positive and negative words.Counts are appended to positive and negative score lists
    for words in items:
        if words in positive_words:
            positive += 1
        if words in negative_words:
            negative +=1
    positive_scores.append(positive)
    negative_scores.append(negative)
# calculating the net scores from positive_scores and negative_scores lists
for a,b in zip(positive_scores,negative_scores):
    net_scores.append(str(a-b))
#---------------------------------------------------------------------------
# writing to resulting_data.csv file
with open("resulting_data.csv","w") as result_data:
# writing headers and data
    result_data.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n")
    for a,b,c,d,e in zip(tweet_retweets, tweet_replies, positive_scores, negative_scores, net_scores):
        result_data.write("{}, {}, {}, {}, {}\n".format(a, b, c, d, e))
