import time


class Trie:
    head = {}

    def insert(self, word):
        curr = self.head
        for ch in word:
            if ch not in curr:
                curr[ch] = {}
            curr = curr[ch]
        curr['is_end'] = True

    def get_start_indeces_of_suffixes(self, word):
        curr = self.head
        if len(word) <= 0 or word[0] not in curr:
            return []
        
        curr = curr[word[0]]
        start_indeces_of_suffixes = []
        
        for i in range(len(word)-1):
            if 'is_end' in curr:
                start_indeces_of_suffixes.append(i + 1)
                
            if word[i + 1] not in curr:
                break
            
            curr = curr[word[i+1]]
            
        if 'is_end' in curr:
            start_indeces_of_suffixes.append(i + 2)
            
        return start_indeces_of_suffixes

"""
We built the trie for given word.
Loopover each word and repeat the logic. 
Find valid prifices, and append their suffices to stack so, 
we can perform the saem logic with them till we found no any valid prifices or 
suffice become empty string that means we found a combination to divide the word into smaller words.
"""
def solve_logest_compound_word(file_path):
    start_time = time.time()
    with open(file_path, 'r') as file:
        words = file.read().split('\n')

    trie = Trie()
    for word in words:
        trie.insert(word)

    longest_compound_word = ''
    second_longest_compound_word = ''
    for word in words:
        queue = [word]
        while len(queue) > 0:
            suffix = queue.pop()
            indeces = trie.get_start_indeces_of_suffixes(suffix)
            for i in indeces:
                if i == len(suffix) and len(word) > len(longest_compound_word) and i != len(word):
                    second_longest_compound_word = longest_compound_word
                    longest_compound_word = word
                    break
                queue.append(suffix[i:])

    print(f'longest compound word: {longest_compound_word}')
    print(f'second songest compound word: {second_longest_compound_word}')
    print(f'time taken: {(time.time() - start_time)} seconds')


print()
print('File: Input_01.txt')
solve_logest_compound_word('Input_01.txt')
print()
print('File: Input_02.txt')
solve_logest_compound_word('Input_02.txt')
print()
