import csv 
import codecs

def parseCSV(filename):
    with codecs.open(filename, mode='rb', encoding=None, errors='strict', buffering=1) as csvFile:
        fileReader = csv.reader(csvFile)
        return [' '.join([elem.strip().title() for elem in row]).strip() for row in fileReader]

def generatePhrasePairs(phrasesA, phrasesB):

    pairs = []

    for phraseA in phrasesA:
        for phraseB in phrasesB:
            pairs.append((phraseA, phraseB))

    return pairs

def generatePermutationsOfPhrasePairs(phrases):
    permutations = []
    for phrasePair in phrases:
        permutation = generatePermutationsOfPhrasePair(phrasePair)
        permutations.append(permutation)
    return permutations

def generatePermutationsOfPhrasePair(phrasePair):
    phraseAList = phrasePair[0].split(' ')
    phraseBList = phrasePair[1].split(' ')
    print("List A: ", phraseAList)
    print("List B: ", phraseBList)

    wordsFlattened = phraseAList + phraseBList
    revWordsFlattened =  list(reversed(wordsFlattened))

    combinations = [] 
    for ind in range(len(wordsFlattened)):
        wordA = wordsFlattened[ind]
        wordB = revWordsFlattened[ind]

        for x in range(ind + 1, len(wordsFlattened)):

            combinations.append(wordA + " " + wordsFlattened[x])
            combinations.append(wordB + " " + revWordsFlattened[x])

            print(wordA + " " + wordsFlattened[x])
            print(wordB + " " + revWordsFlattened[x])

    print("_________________________________\n\n")
    return combinations

def main():
    computingPhrases = parseCSV('Computing Phrases.csv')
    personalPhrases = parseCSV('Personal Phrases.csv')

    phrasePairs = generatePhrasePairs(computingPhrases, personalPhrases)

    phrasePairPermutations = generatePermutationsOfPhrasePairs(phrasePairs)
    #print(phrasePairPermutations)

main()