def pythagorean_triplets(triplet_sum):
    """

    If a, b and c are the Pythagorean triplet, where a <= b <= c, then c = sum - a - b and
    a <= sum // 3 and b <= sum // 2
    :param triplet_sum: {int} is pythagorean sum to find triplets
    :return:
    """

    # check input, raise relevant errors
    if type(triplet_sum) != int:
        raise TypeError("Input param 'sum' was not type of int")
    if triplet_sum < 0:
        raise ValueError("Input param 'sum' was a negative value")

    # loop to find a, b, and c, these loops will always keep the equality a < b < c satisfied
    for a in range(1, triplet_sum // 3):
        for b in range(a + 1, (triplet_sum // 2)):
            c = triplet_sum - a - b
            # if current a, b and c satisfy pythagorean theorem, return each int and their product
            if a * a + b * b == c * c:
                return {"a": a, "b": b, "c": c, "abc": a * b * c}

    return None
