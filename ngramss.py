unigram = ['car', 'house', 'moon', 'sun']
bigram = []
trigram = []
n = 1
count = 0
for current in unigram:
    next = unigram[n + count]
    bi = (current,) + (next,)
    bigram.append(bi)
    if next == unigram[-1]:
        break
    count += 1
print(bigram)
n = 1
count = 0
for current in unigram:
    next = unigram[n + count]
    nextnext = unigram[(n + 1) + count]
    tri = (current,) + (next,) + (nextnext,)
    trigram.append(tri)
    if next == unigram[-2]:
        break
    count += 1
print(trigram)