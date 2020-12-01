import numpy as np
import TrieNode

'''
Implementation of the Boggle Solver using tries and trienodes. Also uses a stack to implement a Depth First Traversal
through all the valid points on the boggle board. This boggle board works for any M x M board.
'''

# loads the dictionary from the textfile "words.txt"
file = open('words.txt', 'r')
dictionary = []

for word in file:
    # loads all the valid words from the dictionary length >= 3 to be a valid word in boggle
    if len(word) < 4:
        continue
    dictionary.append(word[:-1])

# makes a trie out of all the words in the dictionary
trie = TrieNode.Trie()
trie.add(dictionary)

print("                     |===| ")
print("                    === ===")
print("                  ===     ===")
print("                ===         ===")
print("              ===             ===")
print("            ===                 ===")
print("          ===                     ===")
print("        ===                         ===")
print("      ===                             ===")
print("    ===                                 ===")
print("  ===                                     ===")
print("===                                         ===")
print("====================WELCOME====================")
print("||                                           ||")
print("||        |==|                    |==|       ||")
print("||                     ||                    ||")
print("||                                           ||")
print("||                                           ||")
print("||           |____________________|          ||")
print("|| |  / | \  |  \ |  /  \  \  \   /  |   |   ||")
print("||  / / \ |  /  \ /  |  |  /  | /   \  |  /  ||")
print("|| |\ / | /  |  \ |  /  \  \  \ / /  | \ |   ||")
print("===============================================")

print("\nThis is Santa's Boggle Solver for any M X M board!")

b = 1
while b:
    print("Enter the size of the boggle board to be solved(M)", end=": ")
    SIZE = input()
    if not SIZE.isdigit():
        print("Not a digit. Please try again.")
    else:
        b -= 1
SIZE = int(SIZE)


def get_input():
    array = np.empty([0, 0])
    row = 1
    while row < SIZE + 1:
        print("Enter ", SIZE, " characters for row ", row, sep="", end=": ")
        rows = input()
        count = 0
        for i in rows:
            if i.isalpha():
                count += 1
        if count == SIZE:
            for char in rows:
                if char.isalpha():
                    array = np.append(array, char.lower())
            row += 1

        # else:
        #     print("Invalid input. Remember that the input should be characters! Please try again.")
        else:
            print("Invalid input. Remember that is a 4x4 matrix! Enter", SIZE, "valid characters. Please try again.")

    array = array.reshape((SIZE, SIZE))

    return array


# Takes in a boggle board and returns the set
# of valid words on that boggle board
def solve_boggle(matrix, curr_node=trie):
    # # verifies that the input board is a valid N x M array
    # if not check_valid_matrix(board):
    # 	return ["invalid board"]

    # the solutions will be stored in a set to eliminate duplicates
    solutions = set()

    # from each starting location on the board (every i,j coordinate),
    # we'll collect the set of valid words that begin at that location
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            solutions.update(find_word(i, j, matrix, curr_node))

    return solutions


# Constants for indexing the tuples that contain relevant information
# about which letter we're looking at an what word we're considering
# it to be a part of as we traverse the board
ROW = 0
COL = 1
NODE = 2
GRID = 3


# Returns all the valid words that start at the given
# i,j coordinate on the board
def find_word(i, j, matrix, curr_node):
    solutions = set()

    # stack for depth-first search
    stack = [(i, j, curr_node.root, matrix)]
    # push on the coordinates of the start letter
    # along with the root of the trie

    while len(stack) > 0:

        curr_letter = stack.pop()
        curr_node = curr_letter[NODE]

        # use a helper function to get all the letters to which our current
        # letter is adjacent
        neighbors = find_neighbors(board, curr_letter[ROW], curr_letter[COL])

        # for each of these neighbors,
        for neighbor in neighbors:

            x = neighbor[ROW]
            y = neighbor[COL]

            board_copy = np.array(curr_letter[GRID])

            child = curr_node.get_child(board_copy[x][y])

            # if there isn't a node in the dictionary trie suggesting that
            # this letter is part of any word, we stop going down this path
            # by not pushing these current coordinates onto the stack
            if not child:
                continue

            if child.complete:
                solutions.add(child.complete)

            # essentially marks the node we just visited as visited
            board_copy[x][y] = None

            stack.append((x, y, child, board_copy))

    return solutions


# Takes the current position of the matrix and pushes the coordinates of the neighbors onto the stack
def find_neighbors(mat, i, j):
    rows = len(mat)
    cols = len(mat[0])

    row_start = max(0, i - 1)
    row_end = min(rows, i + 2)

    col_start = max(0, j - 1)
    col_end = min(cols, j + 2)

    neighbors = []

    for row in range(row_start, row_end):
        for col in range(col_start, col_end):

            # We don't want to input coordinate
            # to be in its list of neighbors
            if row != i or col != j:
                neighbors.append((row, col))

    return neighbors


# checks if the matrix given is a valid M x M matrix
def check_valid_matrix(mat):
    length = len(mat[0])

    for row in mat[1:]:
        if len(row) != length:
            return False

    return True


def print_results(res):

    print("                     |===| ")
    print("                    === ===")
    print("                  ===     ===")
    print("                ===         ===")
    print("              ===             ===")
    print("            ===                 ===")
    print("          ===                     ===")
    print("        ===                         ===")
    print("      ===                             ===")
    print("    ===                                 ===")
    print("  ===                                     ===")
    print("===                                         ===")
    print("====================RESULTS====================")
    print("||                                           ||")
    print("||        |==|                    |==|       ||")
    print("||                     ||                    ||")
    print("||                                           ||")
    print("||                                           ||")
    print("||           |____________________|          ||")
    print("|| |  / | \  |  \ |  /  \  \  \   /  |   |   ||")
    print("||  / / \ |  /  \ /  |  |  /  | /   \  |  /  ||")
    print("|| |\ / | /  |  \ |  /  \  \  \ / /  | \ |   ||")
    print("===============================================")

    rank = 1
    # prints the list in based on the words that will score you the most points
    # more letters means more points in the boggle game
    for string in sorted(res, key=len, reverse=True):
        print(rank, ") ", string, sep="")
        rank += 1


if __name__ == "__main__":
    # get input from the user
    board = get_input()

    # solve for boggle
    result = solve_boggle(board)
    print_results(result)
