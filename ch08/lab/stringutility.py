class StringUtility:
    def __init__(self, string):
        self.string = string
        self.vowel_list = ['a', 'e', 'i', 'o', 'u']
        self.alphabet_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.alphabet_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    '''
    returns string when used as string
    @param: None
    @returns: str
        self.string
    '''
    def __str__(self) -> str:
        return self.string

    '''
    Vowel counter
    @param: None
    @returns: str
        'many' if number of vowels in string are greater than 5, else string of the number of vowels
    '''
    def vowels(self) -> str:
        return 'many' if len(''.join([x for x in self.string if x.lower() in self.vowel_list])) >= 5 else str(len(''.join([x for x in self.string if x.lower() in self.vowel_list])))

    '''
    string splitter
    @param: None
    @returns: str
        empty string if string <= 2, else a string of the first two and last two letters in a string
    '''
    def bothEnds(self) -> str:
        return '' if len(self.string) <= 2 else (self.string[:2] + self.string[-2:])

    '''
    replaces values in a string based off of first letter
    @param: None
    @returns: str
        string with all letters that are the first letter replaced with '*', besides the first letter
    '''
    def fixStart(self) -> str:
        return self.string if len(self.string) <= 1 else self.string[0] + ''.join([('*' if x == self.string[0] else x) for x in self.string[1:]])

    '''
    sum of ascii values
    @param: None
    @returns: int
        sum of all ascii values in a string
    '''
    def asciiSum(self) -> int:
        return sum([ord(x) for x in self.string]) 

    '''
    performs a rot_x cipher where x is the length of the string
    @param: None
    @returns: str
        rotated string
    '''
    def cipher(self) -> str:
        return ''.join(
            ' ' if x == ' ' else (
                self.alphabet_upper[(self.alphabet_upper.index(x) + len(self.string)) % 26].upper() if x.isupper() else self.alphabet_lower[(self.alphabet_lower.index(x) + len(self.string)) % 26]
            ) for x in self.string
        )

def main():
    pass

if __name__ == '__main__':
    main()


