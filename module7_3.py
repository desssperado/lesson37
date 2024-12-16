import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    text = file.read().lower()
                    text = text.translate(str.maketrans('', '', string.punctuation.replace('-', '')))
                    words = text.split()
                    all_words[file_name] = words
            except FileNotFoundError:
                print(f"Файл {file_name} не найден.")
            except Exception as e:
                print(f"Произошла ошибка при обработке файла {file_name}: {e}")
        return all_words

    def find(self, word):
        result = {}
        all_words = self.get_all_words()
        word_lower = word.lower()
        for name, words in all_words.items():
            if word_lower in words:
                result[name] = words.index(word_lower)
        return result

    def count(self, word):
        result = {}
        all_words = self.get_all_words()
        word_lower = word.lower()
        for name, words in all_words.items():
            result[name] = words.count(word_lower)
        return result

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))      # 3 слово по счёту
print(finder2.count('teXT'))     # 4 слова teXT в тексте всего
