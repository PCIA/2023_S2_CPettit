words = {}
words['large'] = {'definition':'Having much size.', 'synonyms':['big','volumous','grande'],'UseCount':5}
words['small'] = {'definition':'Having low size.', 'synonyms':['little','mini'],'UseCount':10}
words['gray'] = {'definition':'A neutral color that is neither black nor white.', 'synonyms':['grey','ash'],'UseCount':15}

def averageWordUse():
   total = 0
   for word in words:
        currentWord = words[word]

        currentWord = currentWord + words['UseCount']
   return total / len(words)

print(averageWordUse())