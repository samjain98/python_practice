#######################################################################################################################
#
#   Homework 3
#   Released: September 21, 2016
#   Due: September 27, 7pm
#   Topic: Arrays and Loops
#
#######################################################################################################################


# Nth Largest Element
#
# Write a function that, given an unsorted array, returns the nth largest
# element in that array. So, if n is 1, return the largest element, if n is
# 2 return the second-largest element, and so on.
#
# Note: You may not use any built in sorting methods for this problem.
#
#
# Example(s)
# ----------
# Example 1:
#   Input: [3,1,5,2,4], 3
#   Output:
#   3
#
# Example 2:
#   Input: [-331, -776, 917, 399, -768, -183, -116, 278, -544, -669], 5
#   Output:
#   -183
#
# Parameters
# ----------
# arr : List[int]
#   An unsorted list of integers
#
# n : int
#   An integer in range 1 < n < len(arr)
#
# Returns
# -------
# int
#   The nth largest element in arr
#
def nth_largest_element(arr, n):
    for i in xrange (n - 1):
        arr.remove(max(arr))

    return max(arr)




# Subset Sum
#
# Given a list of unsorted integers and another integer k, determine if you can
# sum an arbitrary number of elements of the list and get exactly k.
#
# Note: You can use each element in the list exactly once while calculating the
#       sum.
#
# Example(s)
# ----------
# Example 1:
#   Input: [1,5,4,3,6,2,5,17], 24
#   17 + 4 + 2 + 1 = 24
#   Output:
#   True
#
# Example 2:
#   Input: [1,18,5], 10
#   No elements will sum to 10
#   Output:
#   False
#
# Parameters
# ----------
# arr : List[int]
#   An unsorted list of integers
#
# k : int
#   The integer you are trying to sum to
#
# Returns
# -------
# bool
#   Whether or not k can be constructed from a subset sum of arr
#
def subset_sum(arr, k):
    import itertools
    i = 0
    while (i < (len(arr) + 1)):
        for set in itertools.combinations(arr, i):
            total = 0
            for j in set:
                total += j
                
                if total == k:
                    return True
        i+=1
    return False

# Reverse Block
#
# Given a list/array and a number n, reverse the list in blocks of n.
#
# Let's say the list is [1, 2, 3, 4, 5, 6, 7] and we are given the number 3.
# That must mean that the list must be reversed in groups of 3.
# [3, 2, 1, 6, 5, 4, 7]
#
# Restriction(s)
# --------------
# Block_size will always be a positive integer.
#
# Example(s)
# ----------
# Example 1:
#   Input 1: [1, 2, 3, 4, 5, 6, 7]
#   Input 2: 3
#   We take the list and reverse the elements in groups of 3.
#   Output:
#   [3, 2, 1, 6, 5, 4, 7]
#
# Parameters
# ----------
# arr: list
#   The list/array that must be reversed
# block_size: int
#   The size of each group that we will reverse.
#
# Returns
# -------
# list
#   A list with groups of `block_size` reversed.
def reverse_block(arr, block_size):

    new_arr = []
    final_arr = []
    for i in xrange (0, len(arr), block_size):
        new_arr= sorted(arr[i:(i+block_size)], reverse=True) 
        for i in xrange(0, len(new_arr)):
            final_arr.append(new_arr[i])
        
    return final_arr


# Lazy Trainer
#
# Recently, there has been extensive research done on Pokomon's (don't sue us) training method.
# Turns out, we have made a rapid advancements in how Pokomon gain experience! We can now gain
# experience base on our Pokomon's current strength.
#
# Now the Pokomon we are training can either
# 1. Tackle -- This will defeat the enemy Pokomon and
#              increase our Experience by Current Strength * The Enemy's hitpoints.
# 2. Belly Drum -- This will increase our Pokomon's Strength by 1, and the battle ends
#    (I guess Pokomon are afraid of belly drums).
#
# But as a 8th Time Entrier in the Hall of Fame, we have become very very lazy.
#
# Given a sequence of Pokomons to fight (with corresponding Hit Points), return the maximum
# experience we can gain with our new battle method! (Correction: ) You can fight the Pokomon in any order.
# i.e. You can fight Pokomon #4 without fighting Pokomon #1.
#
# The Pokomon starts with Strength = 1 and Experience = 0. We are interested in training lots of
# Pokomon after all!
#
# Restriction(s)
# --------------
# All Enemy Pokomons will have positive hitpoints!
# You may not use recursion.
#
# Example(s)
# ----------
# Example 1:
#   Input 1: [3, 2, 2]
#   We should use Belly Drum on the second Pokomon to get Strength = 2.
#   Then we should use Tackle to defeat the the rest to get Experience = 10.
#   This is the maximum experience we can gain from the series of battles.
#
#   Output:
#   10
#
# Parameters
# ----------
# pokomon: list
#   The list/array given with the sequence of Pokomons we must fight.
#
# Returns
# -------
# int
#   The maximum experience a Pokomon can gain.
#
# Note
# ----
# This is a difficult question. Come to office hours *wink wink* for help!
def lazy_trainer(pokomon):
    pokomon.sort()
    
    max_exp = 0;
    
    #print len(pokomon)
    for i in xrange( int(0.4 * len(pokomon)), len(pokomon) ):
        exp = 0;
        str = 1;
        
        for j in xrange (0, i):
            str +=1
            
        for k in xrange (i, len(pokomon) ):
            exp += str*pokomon[k]
        
        #print exp, " at index ", i
        
        if exp>max_exp:
            max_exp = exp
        elif exp < max_exp:
            break
        
    return  max_exp
# findRing
#
# You are a secret agent in the CIA tasked with finding a ring of Moles in the organization!
# Rumor has it that moles hang out at Red Lion (the bar). There's a whole row of agents seated at the bar.
# You start by talking to the agent seated on the left-most stool on the bar. However, the agent redirects you to another
# agent.  To your great annoyance, that agent redirects you to yet another agent!!
# And on and on it goes. Standard regulation requires each agent to have a tattoo on the back of his/her neck representing a unique integer and you
# decide to ID each agent by his/her number. Each agent redirects to a different agent, other than him/herself. Because of this,
# it is guaranteed that you will start going in loops talking to them.
# The moles are trying to trick you by creating an endless chain of references! Find the size of the ring and report
# back to headquarters.
# Write a function findRing(agents) which returns the number of agents which form a loop, given that you start by
# talking to the left-most agent, 0. numbers will be an array of non-negative integers such that number[m] is the
# number of the agent to whom agent m redirects. No agent redirects to himself. The left-most agent is number 0,
# the next is number 1, and so on. Each element in the numbers list will be in the range [0, n-1] where n is the length
# of the numbers list.
#
# Restriction(s)
# --------------
# The number of agents will be at least 2 and no more than 1000.
# You may not use recursion.
#
# Example(s)
# ----------
# Example 1:
# Suppose the numbers list were [1, 3, 0, 1]. Then agent 0 redirects to agent 1, who redirects to
# agent 3, who redirects back to agent 1. There is a loop of two agent: 1, 3. Thus the answer would be 2.
# Note that even though you started with agent 0, he is not part of the ring.
#
# Output: 2
#
# Parameters
# ----------
# agents: list
#   The list/array given with the sequence of agents in the bar.
#
# Returns
# -------
# int
#   The number of agents in the ring.
#
# Note
# ----
# This is a Google interview question. If you can solve this problem in under 30 minutes, you would have passed 1 of 2 rounds.
def findRing(agents):
    accesses = [0]*len(agents)
    
    proceed = True
    i = 0;
    step_count = 0;
    while proceed:
        if accesses[i] == 1:
            step_count+=1
            accesses[i] += 1
            i = agents[i]
        elif accesses[i] == 2:
            proceed = False
        else:
            accesses[i] += 1
            i = agents[i]
    
    return step_count
