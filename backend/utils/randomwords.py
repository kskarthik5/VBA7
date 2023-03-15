import random
 
list = ["sheep","pink","around","seven","flight","mouse","sky","orange"]
 

def genWords(n): 
    return ' '.join(random.sample(list, n))
