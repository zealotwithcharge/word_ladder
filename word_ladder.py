#!/bin/python3

from collections import deque
import copy


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny', 'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots', 'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''

    if start_word == end_word:
        return [start_word]

    with open(dictionary_file) as f:
        words = f.readlines()
        words = set([word.strip() for word in words])

    queue = deque([[start_word]])
    while len(queue) > 0:
        stack = queue.pop()
        for word in list(words):
            if _adjacent(word, stack[-1]):
                stack_copy = copy.deepcopy(stack)
                stack_copy.append(word)
                if word == end_word:
                    return stack_copy
                queue.appendleft(stack_copy)
                words.remove(word)


def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.
    '''

    if ladder == []:
        return False
    for i in range(len(ladder) - 1):
        if not _adjacent(ladder[i], ladder[i + 1]):
            return False
    return True


def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''

    if len(word1) != len(word2):
        return False

    num_diffs = 0
    for c1, c2 in zip(word1, word2):
        if c1 != c2:
            num_diffs += 1

    return num_diffs == 1
