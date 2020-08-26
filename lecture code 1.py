# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 12:30:50 2020

@author: 
"""


import random
import string

target = list("Hello World!")

def generate_random_solution(length=12):
    return [random.choice(string.printable) for _ in range(length)]

def evaluate(solution):
    diff = 0
    for i in range(len(target)):
        s = solution[i]
        t = target[i]
        diff += abs(ord(s) - ord(t))
    return diff

def mutate_solution(solution):
    index = random.randint(0, len(solution) - 1)
    solution[index] = random.choice(string.printable)

best = generate_random_solution()
best_score = evaluate(best)

while True:
    print("Best score so far", best_score, "Solution", "".join(best))
    
    if best_score ==0:
        break
    
    new_solution = list(best)
    mutate_solution(new_solution)
    
    score = evaluate(new_solution)
    if score < best_score:
        best = new_solution
        best_score = score
        
        