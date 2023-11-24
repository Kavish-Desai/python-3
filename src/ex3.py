
def create_files(input_file):
    small_words = []
    large_words = []
    unique_words = set()

    try:
        with open(input_file, 'r') as file:
            text = file.read().split()
            unique_words = set(text)

            for word in unique_words:
                if len(word) < 3:
                    small_words.append(word)
                else:
                    large_words.append(word)

        with open('small-words.txt', 'w') as small_file:
            for word in small_words:
                small_file.write(word + '\n')

        with open('large-words.txt', 'w') as large_file:
            for word in large_words:
                large_file.write(word + '\n')

        return len(unique_words)
    except FileNotFoundError:
        print(f"File '{input_file}' not found.")
        return 0
    



def ex3():
    total_words = create_files("C:\\Users\\f9xuyp3\python-3\\files\\words.txt")
    print(f"Total words: {total_words}.")

ex3()
