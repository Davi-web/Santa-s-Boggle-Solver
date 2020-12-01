class TrieNode:

    # TrieNode Constructor
    # The nodes have a their own values and their children. Valid is used to store valid
    # words when solving for the boggle game.
    def __init__(self, value):
        self.value = value
        self.children = []
        self.valid = None

    # Adds a child to the node
    def add(self, child):
        self.children.append(child)

    # Returns the child node with the requested value if it
    # exists. If it does not exist, it returns None
    def get_child(self, value):
        for child in self.children:
            if child.value == value:
                return child
        return None

    # toString function
    def __str__(self):
        return str(self.value)


class Trie:

    # Trie Constructor
    # The root of a trie is the empty string
    def __init__(self, lists=None):
        self.root = TrieNode('')

        if lists is not None:
            self.add(lists)

    # Adds the list of words to the trie
    def add(self, lists):

        for word in lists:

            current_node = self.root

            # We search for each letter of the current word on
            # the next level in the children nodes
            for letter in list(word):
                next_node = current_node.get_child(letter)
                if next_node is None:
                    next_node = TrieNode(letter)
                    current_node.add(next_node)
                current_node = next_node

            # Adds it to complete if it it is a valid word.
            current_node.valid = word
