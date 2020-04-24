class Block:
    def __init__(self, block_size, tag_size):
        self.data = [0 for x in range(block_size)]
        self.valid = true
        self.tag = [tag_size]
        self.tag_size = tag_size

    def is_valid(self):
        return self.valid

    def set_valid(self, is_valid):
        self.valid = is_valid

    def set_tag(self, new_tag):
        for i in range(tag):
            tag[i] = 1 & (newtag >> tag_size-i)
