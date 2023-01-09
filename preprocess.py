from collections import namedtuple
import json

Word = namedtuple('Word', ['tag', 'word', 'responses'])


def create():
    sentences = [
        "Hello World".lower(),
        "Bye World".lower()
    ]
    words = []
    for sentence in sentences:
        words.extend(sentence.split(' '))

    data = json.loads(open('intents.json').read())

    intents = data["intents"]
    word_taglist = []
    common_words: list[Word] = []
    for item in intents:
        word_taglist.append(item["tag"])

        for word in item["patterns"]:
            common_words.append(Word(
                tag=item["tag"],
                word=word,
                responses=item["responses"]
            ))

    bow = [[0] * len(words[0])] * len(word_taglist)

    for i in range(len(words)):
        word_set = words[i]
        for j in range(len(word_set)):
            word = word_set[j]
            for common_word in common_words:
                if common_word.word == word:
                    bow[i][j] = 1

    print(bow)
    print(word_taglist)
    return bow, word_taglist
