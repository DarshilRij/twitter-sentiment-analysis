import csv
import re
import string
import json

jsonfile = open('Tweet 500.json')

jsondata = json.load(jsonfile)
index = 0

outputDictionary = {
    "Tweet Number": index,
    "Tweet Message": "",
    "Bag Of Words": {},
    "Matched Words": [],
    "Polarity": "",
    "Positive Words": 0,
    "Negative Words": 0
}


def checkForPositiveWords():
    # Taken this Positive Words List from https://gist.github.com/mkulakowski2/4289437
    with open('PositiveWords.txt', 'r') as f:
        for line in f:
            for word in line.split():
                if word in tweetWords:
                    outputDictionary["Matched Words"].append(word)
                    outputDictionary['Positive Words'] = outputDictionary['Positive Words'] + 1


def checkForNegativeWords():
    # Taken this Negative Words List from https://gist.github.com/mkulakowski2/4289441
    with open('NegativeWords.txt', 'r') as f:
        for line in f:
            for word in line.split():
                if word in tweetWords:
                    outputDictionary["Matched Words"].append(word)
                    outputDictionary['Negative Words'] = outputDictionary['Negative Words'] + 1


for tweet in jsondata['data']:

    tweetWords = re.split(" ", tweet)
    index = index + 1

    outputDictionary["Tweet Number"] = index

    outputDictionary["Tweet Message"] = tweet

    for tweetWord in tweetWords:
        if tweetWord not in outputDictionary["Bag Of Words"]:
            outputDictionary["Bag Of Words"][tweetWord] = 0
        outputDictionary["Bag Of Words"][tweetWord] += 1

    checkForPositiveWords()

    checkForNegativeWords()

    if outputDictionary["Positive Words"] > outputDictionary['Negative Words']:
        outputDictionary["Polarity"] = "positive"
    elif outputDictionary["Positive Words"] < outputDictionary['Negative Words']:
        outputDictionary["Polarity"] = "negative"
    else:
        outputDictionary["Polarity"] = "neutral"
    outDict = []
    outDict.append(str(outputDictionary["Tweet Number"]))
    outDict.append(outputDictionary["Tweet Message"])
    outDict.append(str(outputDictionary["Matched Words"]))
    outDict.append(outputDictionary["Polarity"])

    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Tweet Number : " + str(outputDictionary["Tweet Number"]))
    print("Tweet Message : " + outputDictionary["Tweet Message"])
    print("Matched Words : " + str(outputDictionary["Matched Words"]))
    print("Polarity : " + outputDictionary["Polarity"])

    outputDictionary = {
        "Tweet Number": index,
        "Tweet Message": "",
        "Bag Of Words": {},
        "Matched Words": [],
        "Polarity": "",
        "Positive Words": 0,
        "Negative Words": 0
    }
    if index == 500:
        break
print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
