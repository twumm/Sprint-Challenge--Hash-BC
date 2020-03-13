#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    # set a current location of none
    # insert tickets into hashtable
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    # get first ticket with NONE as source
    # first_ticket = hash_table_retrieve(hashtable, 'NONE')
    # set that ticket in the route list as the first index
    # route[0] = first_ticket
    # set a location user is in
    user_location = "NONE"
    for i in range(length):
        route[i] = hash_table_retrieve(hashtable, user_location)
        user_location = route[i]

    return route[:-1]