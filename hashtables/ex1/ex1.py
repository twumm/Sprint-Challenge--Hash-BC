#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    for i in range(length):
        hash_table_insert(ht, weights[i], i)
    
    for i in range(length):
        index_in_ht = hash_table_retrieve(ht, (limit - weights[i]))

        if index_in_ht:
            if index_in_ht > i:
                return [index_in_ht, i]
            else:
                return [i, index_in_ht]
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
