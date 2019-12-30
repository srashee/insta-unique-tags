import random

def main():
    # Debugging only
    debug = 0

    # Create a set of unique tags
    tags = set()

    # Number of hashtags to use
    hashNum = 18

    totalCount = 0
    uniqueCount = 0
    randNum = 0

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

    for x in range (0, hashNum):
        randNum = random.randint(0,(len(uniqueList) - 1))
        if debug == 1:
            print("Index is ", randNum)
        print(uniqueList[randNum])


    if debug == 1:
        print("The total count is", totalCount)
        print("The unique count is", uniqueCount)

if __name__== "__main__":
    main()
