import random
 
list = ["steel","pink","around","bird","flight","mouse","sky","orange","fetch","branch","tree","store","garden"]
 

def genWords(n): 
    return ' '.join(random.sample(list, n))
