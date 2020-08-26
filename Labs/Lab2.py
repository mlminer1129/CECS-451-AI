# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 11:34:26 2020

@author: 
"""
from __future__ import print_function, division

import numpy as np
import numpy.random as rn
import matplotlib.pyplot as plt
import matplotlib as mpl

from scipy import optimize
import seaborn as sns




def annealing(random_start, cost_function, random_neighbour, acceptance, temperature, maxsteps=1000, debug=True):
    """ Optimize the black-box function 'cost_function' with the simulated annealing algorithm."""
    state = random_start()
    cost = cost_function(state)
    states, costs = [state], [cost]
    for step in range(maxsteps):
        fraction = step / float(maxsteps)
        T = temperature(fraction)
        new_state = random_neighbour(state, fraction)
        new_cost = cost_function(new_state)
        if debug:  print("Step #{:>2}/{:>2} :T = {:>4.3g}, state = {:>4.3g}, cost = {:>4.3g}, new_state = {:>4.3g}, new_cost = {:>4.3g} ...".format(step, maxsteps, T, state, cost, new_state, new_cost))
        if acceptance_probability(cost, new_cost, T) > rn.random():
            state, cost = new_state, new_cost
            states.append(state)
            costs.append(cost)
            # print(" ==> Accept it!")
        # else:
            # print(" ==> Reject it...")
    return state, cost_function(state), states, costs

interval = (-10, 10)

def f(x):
    """ Function to minimize."""
    return x ** 2
def clip(x):
    """ Force x to be in the interval."""
    a, b = interval
    return max(min(x, b), a)

def random_start():
    """ Random point in the interval."""
    a, b = interval
    return a + (b - a) * rn.random_sample()

def cost_function(x):
    """ Cost of x = f(x)."""
    return f(x)

def random_neighbour(x, fraction=1):
    """Move a little bit x, from the left or the right."""
    amplitude = (max(interval) - min(interval)) * fraction / 10
    delta = (-amplitude/2.) + amplitude * rn.random_sample()
    return clip(x + delta)

def acceptance_probability(cost, new_cost, temperature):
    if new_cost < cost:
        # print(" - Acceptance probabilty = 1 as new_cost = {} < cost = {}...".format(new_cost, cost))
        return 1
    else:
        p = np.exp(- (new_cost - cost) / temperature)
        # print(" - Acceptance probabilty = {:.3g}...".format(p))
        return p

def temperature(fraction):
    """ Example of temperature dicreasing as the process goes on."""
    return max(0.01, min(1, 1 - fraction))

def see_annealing(states, costs):
    plt.figure()
    plt.suptitle("Evolution of states and costs of the simulated annealing")
    plt.subplot(121)
    plt.plot(states, 'r')
    plt.title("States")
    plt.subplot(122)
    plt.plot(costs, 'b')
    plt.title("Costs")
    plt.show()
    
def visualize_annealing(cost_function):
    state, c, states, costs = annealing(random_start, cost_function, random_neighbour, acceptance_probability, temperature, maxsteps=1000, debug=False)
    see_annealing(states, costs)
    return state, c

visualize_annealing(lambda x: x**2)
visualize_annealing(lambda x: x**3)
visualize_annealing(lambda x: np.cos(x))
visualize_annealing(lambda x: abs(x))

'''
annealing(random_start, cost_function, random_neighbour, acceptance_probability, temperature, maxsteps=30, debug=True)
state, c, states, costs = annealing(random_start, cost_function, random_neighbour, acceptance_probability, temperature, maxsteps=1000, debug=False)
y = x**2
y = x**3
y = cos(x)
y = abs(x)
'''