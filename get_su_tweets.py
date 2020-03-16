import os
import random
import json

#DEFINE THE USER WE WANT TO QUERY
user = '@XXXXXXXXXX'
json_file = 'tweets.json'


#PRINT THE PRESENTATION AND GET THE WORD WE'RE GOING TO QUERY
def presentation():
    print('\n\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('|                                                                    |')
    print('|                            WELCOME TO                              |')
    print('|                      MY OWN TWEET SCRAPPER!                        |')
    print('|                                                                    |')
    print(' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    word = raw_input("\n\nWhat word are we looking for today? :) \n")
    return word


#IF THE JSON FILE ALREADY EXISTS WE DELETE IT FIRST
def check_file_exists():
    try:
        f = open(json_file)
        os.system('rm tweets.json')
    except IOError:
        return

#WE GET THE WORD, PREPARE THE TWINT QUERY AND LAUNCH IT, THE OUTPUT GOES TO json_file
def scrapping(word):
    print("\nOk! We're picking a random tweet of {} containing the word {} !".format(user, word))
    query = "twint -u  {} -s {} -o {} --json >/dev/null".format(user, word, json_file)
    os.system(query)

#WE RECOVER THE CONTENT OF THE JSON FILE AND ADD IT TO AN ARRAY
def read_json_file():
    tweets = []
    for line in open('tweets.json', 'r'):
        tweets.append(json.loads(line))
    return tweets

#WE PRINT A RANDOM TWEET FROM THAT JSON
def printing_tweet(data):
    print('\n')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(data['tweet'])
    print('\nAnd that was the {}'.format(data['date']))
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

#WE CHECK IF json_file ALREADY EXISTS
#THEN GET THE WORD WE WANT TO LOOK FOR AND LAUNCH THE QUERY
#THEN SAVE IT TO A JSON FILE
#READ FROM THAT FILE AND PICK A RANDOM TWEET, THEN PRINT IT
def main():
    check_file_exists()
    word = presentation()
    scrapping(word)
    data = read_json_file()
    length = len(data)-1
    my_number = random.randint(0, length)
    printing_tweet(data[my_number])

if __name__ == '__main__':
    main()
