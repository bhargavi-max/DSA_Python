# TreeNode is node within the tree
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = [] # each childern in the list will be instance of TreeNode class
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self):
        prefix = (' ' * self.level_tree() * 3) + "|__" if self.parent else ""
        print(prefix + self.data)
        for child in self.children:
            child.print_tree()

    def level_tree(self):
        level =0
        p = self.parent
        while p:
            level+=1
            p=p.parent
        return level

def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Lenevo"))
    laptop.add_child((TreeNode("Thinkpad")))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Redmi"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(tv)
    root.add_child(cellphone)
    root.add_child(laptop)

    print(laptop.level_tree())
    return root

if __name__ == '__main__':
    root = build_product_tree()
    root.print_tree()
    pass
