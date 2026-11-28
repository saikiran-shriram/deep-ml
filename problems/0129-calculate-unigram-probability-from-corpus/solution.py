def unigram_probability(corpus: str, word: str) -> float:
    # Your code here
    count = 0
    tokens = corpus.split()
    for s in tokens :
        if s == word :
            count += 1
    return round(count/len(tokens),4)
