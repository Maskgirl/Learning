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
        start_indeces_of_suffixes = []
        for i, ch in enumerate(word):
            if ch not in curr:
                break
            if 'is_end' in curr:
                start_indeces_of_suffixes.append(i + 1)
            curr = curr[ch]
        if 'is_end' in curr:
            start_indeces_of_suffixes.append(i + 1)
        return start_indeces_of_suffixes


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
            for i in trie.get_start_indeces_of_suffixes(suffix):
                if i == len(suffix) and i > len(longest_compound_word):
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
