from multiprocessing import Pool
import pprint
import os
import time
import spacy
import random

nlp = spacy.load('en_core_web_sm')

def proc_sentence(sentence):
     doc = nlp(sentence)
    # pprint.pprint(sentence)

def main():
    t = time.time()
    nouns = ("puppy", "car", "rabbit", "girl", "monkey")
    verbs = ("runs", "hits", "jumps", "drives", "barfs") 
    adv = ("crazily.", "dutifully.", "foolishly.", "merrily.", "occasionally.")
    adj = ("adorable", "clueless", "dirty", "odd", "stupid")
    sentences = []
    for _ in range(1000):
        num = random.randrange(0,5)
        sentences.append('{} {} {} {}'.format(nouns[num], verbs[num], adv[num], adj[num]))

    p = Pool()
    p.map(proc_sentence, sentences)
    # [proc_sentence(sentence) for sentence in sentences]
    print("Time: ", time.time() - t)

if __name__ == "__main__":
    main()