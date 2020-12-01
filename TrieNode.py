class TrieNode:

    # Each node in the trie has a value, a list of children,
    # and a "complete" value that keeps track of whether that
    # node completes a word in the trie. It contains "None" if
    # it doesn't. If it does, it contains the word, which will
    # be equal to the concatenation of the values of all the
    # nodes on the path from the root to this node
    def __init__(self, value):
        self.value = value
        self.children = []
        self.complete = None

    # Adds a child to the node
    def add(self, child):
        self.children.append(child)

    # Returns the child node with the requested value if it
    # exists, and returns None otherwise. Allows us to search
    # the trie for a word letter-by-letter
    def get_child(self, value):
        for child in self.children:
            if child.value == value:
                return child
        return None

    # Tells Python that, when we call "print" on a node,
    # we want to print its value field
    def __str__(self):
        return str(self.value)


class Trie:

    # The root of a trie is the empty string
    def __init__(self, lists=None):
        self.root = TrieNode('')

        # If we pass in the optional listy parameter,
        # the list of words is added to the trie
        if lists is not None:
            self.add(lists)

    # Takes a list of words and adds all of them to the trie
    def add(self, lists):

        for word in lists:

            current_node = self.root

            # We search for each letter of the current word on
            # the next level of the trie by looking for it in the
            # current TrieNode's children. If it isn't there, we
            # add it and keep going.
            for letter in list(word):
                next_node = current_node.get_child(letter)
                if next_node is None:
                    next_node = TrieNode(letter)
                    current_node.add(next_node)
                current_node = next_node

            # Once each word has completed, we add it to the 'complete'
            # field of the current node to indicate that the current node,
            # which iss the last letter in the word, completes that word.
            current_node.complete = word
