import random
 
list = ["steel","pink","around","bird","flight","mouse","sky","orange","apple","branch","green","store","garden"]
 

def genWords(n): 
    return ' '.join(random.sample(list, n))
