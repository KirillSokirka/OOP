
golds_dict = {'small_g': 1,
         'medium_g': 5,
         'another_medium': 6,
         'big_g': 3,
         'king_g': 7
              }


def get_weights(golds):
    return [golds[item] for item in golds]


def get_table(golds_dict, capacity):
    weights = get_weights(golds_dict)
    golds_number = len(golds_dict)

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


def get_goldsbar_list(golds_dict, init_capacity):
    table, weights = get_table(golds_dict, init_capacity)
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


get_goldsbar_list(golds_dict, 13)
