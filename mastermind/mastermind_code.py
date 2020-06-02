# encoding: utf-8
from copy import copy


def mastermind(choices, right_choices):
    result = [0, 0]
    choices_ = copy(choices)

    if len(choices) != len(right_choices):
        raise ValueError()

    for x in right_choices:
        if x in choices_:
            result[1] += 1
            del choices_[choices_.index(x)]

    for n, x in enumerate(right_choices):
        if x == choices[n]:
            result[0] += 1
            result[1] -= 1

    return result