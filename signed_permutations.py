"""
by Joshua Mundinger
for the MathILy-EST REU
July 2, 2022
"""

from sage.combinat.permutation import Permutation
from sage.groups.perm_gps.permgroup import PermutationGroup

def signed_permutations(n):
    """
    Returns the group B_n, implemented as signed permutations of [n].
    INPUT:
    n:  positive integer
    OUTPUT:
    B_n, as a PermutationGroup on [2n]

    c.f. https://en.wikipedia.org/wiki/Hyperoctahedral_group
    for the implementation of B_n as permutations of {+-1, ... +-n}.
    """
    #generators corresponding to simple roots in B_n
    #underlying set is {1,2,...,2n} where n+i is interpreted as -i
    long_generators = [ [(i,i+1),(n+i,n+i+1)] for i in range(1,n)]
    short_generator = [ (n,2*n)]
    return PermutationGroup(long_generators+short_generator)

def signed_cycle_type(n,perm):
    """
    Given a permutation in signed_permutations(n), determine its signed cycle type.
    INPUT:
    n:      positive integer
    perm:   an element of signed_permutations(n)
    OUTPUT
    a list of two lists of positive integers, giving partitions of n according to the signed cycle type.
    """
    signed_cycle_type = [[],[]]
    #convert permutation into list of tuples
    perm_list = Permutation(perm).to_cycles()
    for cycle in perm_list:
        #determine whether the cycle has an even or odd number of sign flips
        is_negative = False
        for i in cycle:
            if n+i in cycle:
                is_negative = True
                break
        if is_negative:
            #the cycle must be even 
            signed_cycle_type[1].append(int(len(cycle)/2))
        else:
            signed_cycle_type[0].append(len(cycle))
    for x in signed_cycle_type:
        x.sort()
        x.reverse()
    #now cut signed_cycle_type[0] in half, since we double-counted them
    signed_cycle_type[0] = signed_cycle_type[0][::2]
    return signed_cycle_type

