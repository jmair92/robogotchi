def sum_with_exceptions(a, b):
    _sum = a + b
    if _sum < 0:
        raise NegativeSumError
    else:
        return _sum


class NegativeSumError(Exception):
    pass
