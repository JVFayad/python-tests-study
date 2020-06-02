from copy import copy

def complete_series(series):
    series_ = copy(series)
    biggest_number = 0
    
    for x in series:
        del series_[series_.index(x)]
        if x in series_:
            return [0]     

        if x > biggest_number:
            biggest_number = x

    return [x for x in range(0, biggest_number + 1)]