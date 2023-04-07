import random
list = ["steel","pink","around","mouse","sky","orange","apple","branch","green","store","garden","silver","purple","month","ninth","wolf","open","dangerous","marathon"]
 

def genWords(n): 
    return ' '.join(random.sample(list,n))
