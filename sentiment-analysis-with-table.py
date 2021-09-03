import csv
import re
import string
import json
import math

jsonfile = open('Tweet 500.json')

jsondata = json.load(jsonfile)
index = 0

searchWords = {'flu': {
    "df": 0,
    "NByDf": 0,
    "logNByDf": 0,
    "Highest Occurence Word Article": {}
},
    'snow': {
    "df": 0,
    "NByDf": 0,
    "logNByDf": 0,
    "Highest Occurence Word Article": {}
},
    'cold': {
    "df": 0,
    "NByDf": 0,
    "logNByDf": 0,
    "Highest Occurence Word Article": {}
}
}


finalArticleTextWithHighestFrequency = ""
finalFByM = 0
finalTotalFrequency = 0

for tweet in jsondata['data']:

    index = index+1
    tweetWords = re.split(" ", tweet)

    for wordy in searchWords:
        if wordy in tweetWords:
            temp = {
                "Article#": index,
                "Article Text": tweet,
                "totalWords": len(tweetWords),
                "frequency": 0,
                "fByM": 0
            }
            for word in tweetWords:
                if word == wordy:
                    temp["frequency"] = temp["frequency"] + 1

            temp["fByM"] = temp["frequency"]/temp["totalWords"]

            if temp["frequency"] > finalTotalFrequency:
                finalArticleTextWithHighestFrequency = tweet
                finalFByM = temp["fByM"]
                finalTotalFrequency = temp["frequency"]
            searchWords[wordy]["Highest Occurence Word Article"] = temp
            searchWords[wordy]["df"] = searchWords[wordy]["df"]+1

    if index == 500:
        break

for word in searchWords:
    if searchWords[word]["df"] != 0:
        searchWords[word]["NByDf"] = 500/(searchWords[word]["df"])
    if searchWords[word]["NByDf"] != 0:
        searchWords[word]["logNByDf"] = math.log10(searchWords[word]["NByDf"])

print("--------------------------------------------------------------------------------------")
print("{:<18} |  {:<18} |  {:<18} |  {:<18} | ".format(
    'Search_Query', 'df', 'NByDf', 'logNByDf'))
print("--------------------------------------------------------------------------------------")
for key, value in searchWords.items():
    Search_Query, df, NByDf, logNByDf = value
    print("{:<18} |  {:<18} |  {:<18} |  {:<18} | ".format(
        key, searchWords[key]["df"], searchWords[key]["NByDf"], searchWords[key]["logNByDf"]))
print("--------------------------------------------------------------------------------------")

displayCold = {'cold': {'cold': searchWords['cold']}}

print(json.dumps(displayCold['cold'], indent = 2))

print("Article with Highest Relative Frequency : ")
print(finalArticleTextWithHighestFrequency)