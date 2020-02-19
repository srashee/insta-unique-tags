import random
import email_myself
from random import randrange

def main():
    # Debugging only
    debug = 0

    # Create a set of unique tags
    tags = set()

    # Number of hashtags to use
    hashNum = 22
    randNum = randrange(4)
    hashNum = hashNum + randNum

    totalCount = 0
    uniqueCount = 0
    randNum = 0
    contentList = []
    contentString = ""

    with open('tags.txt','r') as f:
        for line in f:
            for word in line.split():
                totalCount += 1
                tags.add(word)

    for val in tags:
        uniqueCount += 1
        if debug == 1:
            print(val)

    uniqueList = list(tags)

    # For the number of hashtags we want
    for x in range (0, hashNum):
        randNum = random.randint(0,(len(uniqueList) - 1))
        if debug == 1:
            print("Index is ", randNum)

        # Let's generate the actual hashtag list
        contentList.append(uniqueList[randNum])

    # convert list into string for function call and call e-mail fn
    content = ' '.join(contentList)
    email_myself.email_hashtags(content)

    if debug == 1:
        print(content)
        print("The total count is", totalCount)
        print("The unique count is", uniqueCount)

if __name__== "__main__":
    main()
