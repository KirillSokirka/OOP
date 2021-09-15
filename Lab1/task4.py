import sys


def get_table(weights, capacity):
    """
        This func create a table of memoization:
            rows - weights of goldbar
            columns - capacity of knapsack from 0 to real capacity
    :param weights: list of golds weights
    :param capacity: capacity of knapsack
    :return: a table of memoization and list of weights
    """
    golds_number = len(weights)
    table = [[0 for gold in range(capacity+1)] for i in range(golds_number+1)]
    for bar in range(golds_number+1):
        for weight in range(capacity+1):
            if bar == 0 or weight == 0:
                table[bar][weight] = 0
            elif weights[bar-1] <= weight:
                table[bar][weight] = max(weights[bar-1] + table[bar-1][weight - weights[bar - 1]], table[bar-1][weight])
            else:
                table[bar][weight] = table[bar-1][weight]

    return table, weights


def get_goldbar_list(weights_list, init_capacity):
    """
        This func use @get_table@ to get table of memoization,
        after looping though it finds the list of right gold bar
    :param weights_list: list of golds weights
    :param init_capacity: capacity of knapsack
    :return: the list of golds` weights that we can put in knapsack
    """
    table, weights = get_table(weights_list, init_capacity)
    golds_number = len(weights)
    capacity = init_capacity
    result = table[golds_number][capacity]
    result_bar_list = []

    for bar in range(golds_number, 0, -1):
        if result <= 0 :
            break
        if result == table[bar-1][capacity]:
            continue
        else:
            result_bar_list.append(weights[bar-1])
            result -= weights[bar-1]
            capacity -= weights[bar-1]

    return result_bar_list


def main():
    capacity = int(sys.argv[1])
    bars = [int(bars) for bars in sys.argv[2::]]
    result = get_goldbar_list(bars, capacity)
    if result:
        print("The list of weights -> ", result)
    print("The weights of bars are too much")


main()