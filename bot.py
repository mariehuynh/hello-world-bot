import tweepy # for tweeting
import secrets # shhhh
import nltk # for sentence parsing
import random
import sys

#nltk.download('punkt')

def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")

def get_next_chunk():
  # open text file
  text_file = open('book.txt', 'r+')
  text_string = text_file.read()
  # separate the text into sentences
  tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
  sentences = tokenizer.tokenize(text_string)

  # pick a random sentence of the right length
  chunk = random.choice(sentences)

  while (len(chunk)>134):
      chunk = random.choice(sentences)


  # delete what we just tweeted from the text file
  #text_file.seek(0)
  #text_file.write(text_string[len(chunk):len(text_string)])
  #text_file.truncate()

  text_file.close()
  return chunk

def tweet(message):

  message = message + " #pydxbots"
  auth = tweepy.OAuthHandler(secrets.consumer_key, secrets.consumer_secret)
  auth.set_access_token(secrets.access_token, secrets.access_token_secret)
  api = tweepy.API(auth)
  auth.secure = True
  print("Posting message: {}".format(message))
  api.update_status(status=message)

message = get_next_chunk()
print("Generated message: {}".format(message))

if(query_yes_no("tweet?")):
  tweet(message)
#tweet(message)

