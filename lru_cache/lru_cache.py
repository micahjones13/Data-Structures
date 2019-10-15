from doubly_linked_list import DoublyLinkedList


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.ll = DoublyLinkedList()
        self.storage = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        # if the key exits in our storage dict
        if key in self.storage:
            # start searching the LL for it. Start at head of LL
            current = self.ll.head
            while current:
                # find it, move it to the front since it's most recently used
                if key in current.value:
                    self.ll.move_to_front(current)
                current = current.next
            # return the value of the key in the storage dict
            return self.storage[key]
        else:
            # not in the storage dict? then it doesn't exit. return none
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
        # if key exists inside of storage dict, then we want to overwrite it's current value with the incoming value
        if key in self.storage:
            # taking the value that is already stored inside the storage dict at the correct key
            self.storage[key] = value
            current = self.ll.head
            while current:
                # go through LL to find the correct node
                if key in current.value:
                    # once found, overwrite the value with the new incoming vlaue
                    current.value[key] = value
                current = current.next
        # if key doesn't already exist, and the limit hasn't been reached, add it. If limit has been reached, remove oldest node(tail)
        # and add the new one
        else:
            # if the size is at the limit, then remove the tail and delete it from the storage dict
            if self.size == self.limit:
                tail = self.ll.remove_from_tail()
                for i in tail:
                    del self.storage[i]
            # else we can accept new entries. Just add it and increase the size
            else:
                self.size += 1
            self.ll.add_to_head({key: value})
            self.storage[key] = value

    """




    """
