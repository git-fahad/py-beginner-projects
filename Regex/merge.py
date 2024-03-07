class Solution():
    # @staticmethod
    def wordmerge(word1, word2):
        output = word1 + word2
        return output

#if __name__ == "__main__":
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")
merged_word = Solution.wordmerge(word1, word2)
print("Merged word:", merged_word)