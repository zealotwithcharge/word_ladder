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
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny',
    'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots',
    'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''
    stack = []
    stack.append(start_word)
    q = deque([])
    q.append(stack)
    if start_word == end_word:
        return [start_word]
    with open(dictionary_file, 'r', encoding='utf-8') as dict_file:
        dictionary = dict_file.read()
        dictionary = dictionary.split('\n')
        while len(q) != 0:
            working_stack = q.popleft()
            dict_copy = copy.deepcopy(dictionary)
            for word in dict_copy:
                if _adjacent(word, working_stack[-1]):
                    if word == end_word:
                        if end_word not in working_stack:
                            working_stack.append(end_word)
                        # answers.append(working_stack)
                        # continue
                            # pprint.pprint(q)
                            # for i in range(len(q)):
                            #    temp = q.popleft()
                            #    if temp[7] == 'chile' or temp[7] ==
                            #    'chili' or temp[7] == 'chill':
                            #        print(temp)
                            return working_stack
                    stack_copy = copy.deepcopy(working_stack)
                    stack_copy.append(word)
                    q += deque([stack_copy])
                    dictionary.remove(word)
    return
    # if answers == []:
    #    return
    # else:
    #    smallest = 0
    #    for i,ladder in enumerate(answers):
    #        if len(answers[smallest]) > len(answers[i]):
    #           smallest = i
    #    return answers[smallest]


def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.

    >>> verify_word_ladder(['stone', 'shone', 'phone', 'phony'])
    True
    >>> verify_word_ladder(['stone', 'shone', 'phony'])
    False
    '''

    for i, word in enumerate(ladder):
        if i != len(ladder) - 1:
            if not _adjacent(ladder[i], ladder[i + 1]):
                return False
    if len(ladder) == 0:
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

    counter = 0

    if abs(len(word1) - len(word2)) > 1:
        return False
    elif abs(len(word1) - len(word2)) == 1:
        return word1 in word2 or word2 in word1
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            counter += 1
    return counter == 1


def check_links(goal):
    with open('words5.dict', 'r', encoding='utf-8') as dict_file:
        dictionary = dict_file.read()
        dictionary = dictionary.split('\n')
        answers = []
        for word in dictionary:
            if _adjacent(word, goal):
                answers.append(word)
        print(answers)
