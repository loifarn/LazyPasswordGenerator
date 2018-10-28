import json
import os
import random

# Input
lower_case = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "x", "y", "z"]
upper_case = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "X", "Y", "Z"]
special_case = ["`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "{", "[", "}", "}", "|", "\\", ":", ";", "\"", "'", "<", ",", ">", ".", "?", "/"]
num_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
RD = random


def gen_seed(input=None):
    '''
    Takes a 32 bit integer as input for the seed.
    If no input is given systime is used instead
    '''
    if input is not None:
        RD.seed(input)
        print('Seed set')
    else:
        RD.seed()
        print('Seed set')

def generate_password(seed, length=12, lc=True, uc=True, sc=False, numbers=True, verbose=False):
    '''
    Takes in a required 32 bit integer seed and has toggleable switches for additional parameters
    Integer parameters: Length
    Boolean parameters (True/false): Lowercase(lc), Uppercase(uc), Specialcase(sc), numbers, verbose
    '''
    if verbose:
        print('<<<TEST BLOCK>>>\nSeed: {}\nLength: {}\nLower: {}\nUpper: {}\nSpecial: {}\nnumbers: {}'.format(seed, length, lc, uc, sc, numbers))

    password = ''
    while length > 0:
        if lc and RD.randrange(0, 10) > 5:
            password += RD.choice(lower_case)
            length -= 1
        if uc and RD.randrange(0, 10) > 5:
            password += RD.choice(upper_case)
            length -= 1
        if sc and RD.randrange(0, 10) > 5:
            password += RD.choice(special_case)
            length -= 1
        if numbers and RD.randrange(0, 10) > 5:
            password += RD.choice(num_list)
            length -= 1

    return password




    