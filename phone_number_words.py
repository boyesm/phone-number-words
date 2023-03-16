phone_number = input("Please enter your phone number to proceed (do not include any non-integer characters):")

number_to_alpha = {
    1: "1",
    2: "abc",
    3: "def",
    4: "ghi",
    5: "jkl",
    6: "mno",
    7: "pqrs",
    8: "tuv",
    9: "wxyz",
}

class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.children = []


root = TreeNode()

def create_tree(dig_i, cur_node):
    my_list = []
    for conv in number_to_alpha[int(phone_number[dig_i])]:
        my_list.append(TreeNode(conv))
    cur_node.children = my_list

    if (dig_i >= len(phone_number)-1):
        return

    for node in cur_node.children:
        create_tree(dig_i + 1, node)

all_possible_conversions = []

def traverse_tree(cur_node, str=""):

    if cur_node.children == []:
        all_possible_conversions.append(str)

    for node in cur_node.children:
        traverse_tree(node, f"{str}{node.data}")

create_tree(0, root)

traverse_tree(root)

# create and filter wordlist (any words under 2 characters are ommitted)
wordlist = []
with open("wordlist.10000.txt") as f:
    for i in range(10000):
        t = f.readline()[:-1].lower().strip()
        if len(t) > 2:
            wordlist.append(t)

good_ones = {}

for conversion in all_possible_conversions:
    occurring_words = []
    for word in wordlist:
        if word in conversion:
            occurring_words.append(word)
    occurring_words.sort()
    if str(occurring_words) not in good_ones:
        good_ones[str(occurring_words)] = conversion
        print(f"{str(occurring_words)}: {conversion}")
