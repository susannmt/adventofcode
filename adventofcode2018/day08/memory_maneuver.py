class Node:
    def __init__(self, n_children, n_meta):
        self.n_children = n_children
        self.children = []
        self.n_meta = n_meta
        self.meta = []

    def add_child(self, node):
        self.children.append(node)

    def add_meta(self, value):
        self.meta.append(value)

ALL_META = 0

def make_node(string_list, index):
    global ALL_META
    node = Node(int(string_list[index]), int(string_list[index+1]))
    i = index+2
    while len(node.children) < node.n_children:
        child_node, i = make_node(string_list, i)
        node.add_child(child_node)

    while len(node.meta) < node.n_meta:
        node.add_meta(int(string_list[i]))
        i += 1

    ALL_META += sum(node.meta)

    return node, i




input_text = open("input.txt", "r").read().split()
tree, _ = make_node(input_text, 0)
print(ALL_META)


def find_value(tree):
    if tree.n_children == 0:
        return sum(tree.meta)

    value = 0
    for reference in tree.meta:
        if reference == 0:
            continue
        if reference > tree.n_children:
            continue
        value += find_value(tree.children[reference-1])

    return value

print(find_value(tree))
