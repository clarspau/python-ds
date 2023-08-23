# # importing the module
# import doctest

# function


def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}

        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """

    result = {}
    phrase = phrase.lower()
    vowels = set("aeiou")

    for ltr in phrase:
        if ltr in vowels:
            result[ltr] = result.get(ltr, 0) + 1

    return result


# # invoking the testmod function
# doctest.testmod(name='vowel_count', verbose=True)
