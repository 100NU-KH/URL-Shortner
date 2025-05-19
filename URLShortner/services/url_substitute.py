import hashlib
import random

def compute_cheap_hash(txt, length=6):
    hash = hashlib.sha1()
    hash.update(txt.encode())
    digit4 = "".join(map(str, random.sample(range(0, 9), 4) ))
    return hash.hexdigest()[:length] + digit4