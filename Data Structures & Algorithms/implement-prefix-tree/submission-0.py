class PrefixTree:

    def __init__(self):
        # Initialize our root as an empty dictionary.
        # Inside, characters will map to nested dictionaries.
        self.root = {}
        

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            # If the character isn't a child yet, create an empty sub-dictionary
            if char not in curr:
                curr[char] = {}
            # Move our pointer deeper into the tree
            curr = curr[char]
        # Mark the end of the word using a special marker key
        curr["*"] = True


    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            # If a character path doesn't exist, the word isn't in the tree
            if char not in curr:
                return False
            curr = curr[char]
        # The path exists, but it's only an exact match if our end marker is present
        return "*" in curr
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            # If the prefix path breaks anywhere, return False
            if char not in curr:
                return False
            curr = curr[char]
        # If we successfully matched every letter of the prefix, return True
        return True