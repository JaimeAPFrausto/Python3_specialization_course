The final for this course was a course project that consisted of four parts. We are tasked to build a sentiment classifier, which will detect how positive or negative each tweet is. Further more, we create a csv file, which contains columns for the Number of Retweets, Number of Replies, Positive Score (which is how many happy words are in the tweet), Negative Score (which is how many angry words are in the tweet), and the Net Score for each tweet. At the end, the csv file is used to produce a graph of the Net Score vs Number of Retweets.

Part 1:
Define a function called strip_punctuation which takes one parameter, a string which represents a word, and removes characters considered punctuation from everywhere in the word. We are given:
                                                    punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

Part 2:
Copy in your strip_punctuation function and define a function called get_pos which takes one parameter, a string which represents one or more sentences, and calculates how many words in the string are considered positive words. Use the list, positive_words to determine what words will count as positive. The function should return a positive integer - how many occurrences there are of positive words in the text. Note that all of the words in positive_words are lower cased, so you’ll need to convert all the words in the input string to lower case as well. We are given:
                                                    positive_words = []
                                                    with open("positive_words.txt") as pos_f:
                                                        for lin in pos_f:
                                                            if lin[0] != ';' and lin[0] != '\n':
                                                                positive_words.append(lin.strip())
Part 3:
Copy in your strip_punctuation function and define a function called get_neg which takes one parameter, a string which represents one or more sentences, and calculates how many words in the string are considered negative words. Use the list, negative_words to determine what words will count as negative. The function should return a positive integer - how many occurrences there are of negative words in the text. Note that all of the words in negative_words are lower cased, so you’ll need to convert all the words in the input string to lower case as well. We are given:
                                                    negative_words = []
                                                    with open("negative_words.txt") as pos_f:
                                                    for lin in pos_f:
                                                        if lin[0] != ';' and lin[0] != '\n':
                                                            negative_words.append(lin.strip())
Part 4:
Copy in your previous functions and write code that opens the file project_twitter_data.csv which has the fake generated twitter data (the text of a tweet, the number of retweets of that tweet, and the number of replies to that tweet). Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is. Copy the code from the code windows above, and put that in the top of this code window. Now, you will write code to create a csv file called resulting_data.csv, which contains the Number of Retweets, Number of Replies, Positive Score (which is how many happy words are in the tweet), Negative Score (which is how many angry words are in the tweet), and the Net Score (how positive or negative the text is overall) for each tweet. The file should have those headers in that order. 