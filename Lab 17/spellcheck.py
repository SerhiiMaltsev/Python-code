#Serhii Maltsev sm5zj
import urllib.request

stream = urllib.request.urlopen("http://cs1110.cs.virginia.edu/files/words.txt")
text = stream.readlines()

arrayOfWords = []
for line in text:
    arrayOfWords.append(line.decode("UTF-8").strip(".?!,()\"'\n").split("|"))

#
for i in arrayOfWords:
    i[0] = i[0].lower()
#

print("Type text; enter a blank line to end.")
line = "Start"

while line != "":
    line = input("")
    if line != "":
        exist = False
        arrayForSentence = line.strip(".?!,()\"'\n").split()

        for i in range(0, len(arrayForSentence)):
            arrayForSentence[i] = arrayForSentence[i].replace(",", "")
            arrayForSentence[i] = arrayForSentence[i].replace("?", "")
            arrayForSentence[i] = arrayForSentence[i].replace("!", "")
            arrayForSentence[i] = arrayForSentence[i].replace(".", "")
            arrayForSentence[i] = arrayForSentence[i].replace("(", "")
            arrayForSentence[i] = arrayForSentence[i].replace(")", "")
            arrayForSentence[i] = arrayForSentence[i].replace("\"", "")
            arrayForSentence[i] = arrayForSentence[i].replace("'", "")
            arrayForSentence[i] = arrayForSentence[i].replace("\n", "")


        for i in range(0, len(arrayForSentence)):
            exist = False
            word = ""
            word += arrayForSentence[i]
            word = word.lower()
            for j in range (0, len(arrayOfWords)):
                if (word == arrayOfWords[j][0]):
                    exist = True
            if exist == False:
                print("  MISSPELLED: " + arrayForSentence[i])
