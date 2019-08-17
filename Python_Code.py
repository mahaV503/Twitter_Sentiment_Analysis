'''Files Required are
positive_words.txt
negative_words.txt
project_twitter_data.csv


Give this beast these three files it will give you a file resulting_data.csv
'''
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



punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

            
def strip_punctuation(strng):

    
    for letter in strng:
        if letter in punctuation_chars: #statement to check if letter is present in string
            strng=strng.replace(letter,'')
    return strng


def get_pos(tweet):
    
    tweet=tweet.replace("/n",' ')   #To remove multiple lines
    pos_count=0
    tweet_wrds=strip_punctuation(tweet).split(" ")
    for wrd in tweet_wrds:
        if wrd in positive_words:
            pos_count=pos_count+1
    return pos_count


def get_neg(tweet):
    
    
    neg_count=0
    tweet_wrds=strip_punctuation(tweet).split(" ")
    for wrd in tweet_wrds:
        if wrd in negative_words:
            neg_count=neg_count+1
    return neg_count


with open("resulting_data.csv",'w') as resulting_data:
    resulting_data.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
    resulting_data.write('\n')
twitterdata= open("project_twitter_data.csv","r")
twtlst=twitterdata.readlines()
for i in twtlst:
    
        twtfinal=twitterdata.readline().split(",")
        tweet=strip_punctuation(twtfinal[0])
        if twtfinal[1]!='retweet_count':
            row_strng = '{},{},{},{},{}'.format(twtfinal[1].strip(),twtfinal[2].strip(), get_neg(tweet),get_pos(tweet),(get_pos(tweet)-get_neg(tweet)))
            resulting_data.write(row_strng)
            resulting_data.write('\n')
print(resulting_data.csv)
