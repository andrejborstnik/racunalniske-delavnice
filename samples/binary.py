def to_binary(n = 0):
    """ Converts an integer to the correcponding binary string.

    :param int n: A number to convert.
    :returns: Number n as a binary string.
    :rtype: str
    :raises: TypeError

    >>> to_binary(0)
    '0'
    >>> to_binary(-2)
    '-10'
    >>> to_binary(5)
    '101'
    >>> to_binary(1023)
    '1111111111'
    >>> to_binary(3.14)
    Traceback (most recent call last):
    ...
    TypeError: Argument must be an integer.
    """
    if not isinstance(n, int): raise TypeError("Argument must be an integer.")
    if n == 0: return '0'
    s = []
    poz = n > 0
    n = abs(n)
    while n > 0:
        s.append(str(n % 2))
        n = n // 2
    if poz:
        return ''.join(s[::-1])
    else:
        return '-{0}'.format(''.join(s[::-1]))

if __name__ == '__main__':
    import doctest
    doctest.testmod()