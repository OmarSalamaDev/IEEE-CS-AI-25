'''
    Write a Python function that takes in a list of values and returns the probability
    distribution of those values. Assume the values are discrete.

    Input:
    data = [1, 2, 3, 4, 5, 1, 2, 3, 4, 1] 

    Output:
    {1: 0.3, 2: 0.2, 3: 0.2, 4: 0.2, 5: 0.1}
'''


def probability_distribution(data: list[int]) -> dict[int, float]:
    size = len(data)
    prob_dist = {}
    for i in range(size):
        prob_dist[data[i]] = prob_dist.get(data[i], 0) + 1 / size
    return prob_dist

print(probability_distribution([1, 2, 3, 4, 5, 1, 2, 3, 4, 1]))



'''
    Write a Python function that calculates the conditional probability of
    event B given event A, given two lists of events A and B.

    Input:
    event_a = [1, 0, 1, 0, 1]
    event_b = [1, 1, 0, 0, 1]

    Output:
    2/3
'''


def conditional_probability(event_a: list[int], event_b: list[int]) -> float:
    count_a = sum(event_a)
    count_a_and_b = sum(a & b for a, b in zip(event_a, event_b))
    return count_a_and_b / count_a if count_a > 0 else 0

print(conditional_probability([1, 0, 1, 0, 1], [1, 1, 0, 0, 1]))



'''
    Write a Python function that implements Bayes' theorem to calculate the
    probability of event A given event B, given the prior probability of A and B,
    and the conditional probability of B given A.

    Input:
    prior_a = 0.3
    prior_b = 0.6
    conditional_b_given_a = 0.8

    Output:
    0.4
'''


def bayes_theorem(prior_a: float, prior_b: float, conditional_b_given_a: float) -> float:
    return (conditional_b_given_a * prior_a) / prior_b if prior_b > 0 else 0

print(bayes_theorem(0.3, 0.6, 0.8))


