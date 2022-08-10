import random

def calc_probability(scores,genome=True):
    if genome:
        scores = [i.score for i in scores]
    min_score = min(scores)
    add = 0.00000000000001
    if min_score<0:
        add -= min_score
    sum_scores = sum(scores)+len(scores)*add
    prev = 0
    probabilities = []
    for i in scores:
        now = prev+(i+add)/sum_scores
        probabilities.append([prev,now])
        prev = now
    probabilities[-1][1] = 1
    return probabilities

def select(probabilities):
    value = random.uniform(0,1)
    for i in range(len(probabilities)):
        if value>=probabilities[i][0] and value<probabilities[i][1]:
            return i
    return len(probabilities)-1
