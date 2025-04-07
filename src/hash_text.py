import hashlib
from itertools import combinations

def get_ngrams(text, n=3):
    words = text.split()
    return [' '.join(words[i:i+n]) for i in range(len(words) - n + 1)]

def hash_ngram(ngram):
    return hashlib.blake2b(ngram.encode('utf-8'), digest_size=4).hexdigest()

def get_hashed_shingles(text, n=3):
    ngrams = get_ngrams(text, n)
    return set(hash_ngram(ng) for ng in ngrams)
