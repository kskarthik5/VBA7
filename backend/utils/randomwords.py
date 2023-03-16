import random
 
list = ["steel","pink","around","goat","flight","mouse","sky","orange"]
 

def genWords(n): 
    return ' '.join(random.sample(list, n))
