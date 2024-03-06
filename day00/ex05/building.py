# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    building.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hchaguer <hchaguer@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/03/06 21:07:06 by hchaguer          #+#    #+#              #
#    Updated: 2024/03/06 21:08:25 by hchaguer         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import string

def is_upper(_string: str) -> int:
    upper_count = 0 
    for i in range(len(_string)):
        if _string[i].isupper():
            upper_count += 1
            continue
    return upper_count

def is_lower(_string: str) -> int:
    lower_count = 0 
    for i in range(len(_string)):
        if _string[i].islower():
            lower_count += 1
            continue
    return lower_count

def is_space(_string: str) -> int:
    spaces_count = 0 
    for i in range(len(_string)):
        if _string[i].isspace():
            spaces_count += 1
            continue
    return spaces_count


def is_digit(_string: str) -> int:
    digits_count = 0 
    for i in range(len(_string)):
        if _string[i].isdigit():
            digits_count += 1
            continue
    return digits_count


def is_punctuation(_string: str) -> int:
    punc_count = 0
    for i in _string:
        if  i in string.punctuation:
            punc_count += 1
            continue
    return punc_count

def building(string: str):
    print(is_upper(string), "upper letters")
    print(is_lower(string), "lower letters")
    print(is_punctuation(string), "punctuation marks")
    print(is_space(string), "spaces")
    print(is_digit(string), "digits")
    
    

def main():

    try:
        assert len(sys.argv) == 2, "Assertion Error : Invalid Arguments"
        building(sys.argv[1])
    except (AssertionError) as msg:
        print(msg)



if __name__ == "__main__":
    main()