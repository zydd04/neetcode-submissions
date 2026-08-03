class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        len_strings = 0
        len_word = 0
        counter_chars = Counter(chars)
        for word in words:
            len_word = 0
            counter_word = Counter(word) 
            for key in counter_word.keys():
                print(f"key: {key}")
                if key in counter_chars.keys():
                    if counter_word[key] > counter_chars[key]:
                        print(f"counter_word[key]: {counter_word[key]} > counter_swp[key] {counter_chars[key]}")
                        break
                    else:
                        len_word += counter_word[key]
                        print(f"{word} : {len_word}")
                        if len_word == len(word):
                            print(f"counter: {len_word} = {len(word)}, word: {word}")
                            len_strings += len(word)
                else:
                    print(f"{key} not in chars")
                    break
        return len_strings

                    