# definitions
# Creating a strip punctuation function 
def strip_punctuation(string):
# loop to iterate through the string
    for item in punctuation_chars:
# replace punctuation with a space if its contained in string
        string = string.replace(item, '')
# Return string
    return string
# creating get_pos definition
def get_pos(str_sentences):
# making sentences lower case
    str_sentences = str_sentences.lower()
# run each line through the strip definition
    lines = strip_punctuation(str_sentences)
# counting variable
    count_pos = 0
# looping lines
    for words in lines.split():
        if words in positive_words:
            count_pos += 1
    return count_pos

def get_neg(str_sentences):
# making sentences lower case
    str_sentences = str_sentences.lower()
# run each line through the strip definition
    lines = strip_punctuation(str_sentences)
# counting variable
    count_negative = 0
# looping lines
    for words in lines.split():
        if words in negative_words:
            count_negative += 1
    return count_negative
# ----------------------------------------------------------------------
# Begin code
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
#----------------------------------------------------
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
#  appending tweets to tweet_texts
        tweet_text.append(words[0].strip())
# appending the number of retweets to tweet_retweets
        tweet_retweets.append(words[1].strip())
# appending then number of replies to tweet_replies
        tweet_replies.append(words[2].strip())
#---------------------------------------------------------------
# calculating positive scores and negative scores for each tweet
for tweets in tweet_text:
# for each tweet, returned value is appended to positive_scores
    positive_scores.append(get_pos(tweets))
# for each tweet, returned value is appended to negative_scores
    negative_scores.append(get_neg(tweets))
# calculating the net scores from positive_scores and negative_scores lists
for a,b in zip(positive_scores,negative_scores):
    net_scores.append(a-b)
#---------------------------------------------------------------------------
# writing to resulting_data.csv file
with open("resulting_data.csv","w") as result_data:
# writing headers and data
    result_data.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n")
    for a,b,c,d,e in zip(tweet_retweets, tweet_replies, positive_scores, negative_scores, net_scores):
        result_data.write("{}, {}, {}, {}, {}\n".format(a, b, c, d, e))
