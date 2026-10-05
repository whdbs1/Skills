import random
from printer import printf
def rdm(t):
    res = []
    c = random.choice
    cs = random.sample
    if t == 0:
        m=list('123456700')
        leaf=list('123456700')
        random.shuffle(m)
        random.shuffle(leaf)
        return [''.join(m),''.join(leaf)]
    if t == 1:
        pass
    if t == 2:
        pass
    return res
