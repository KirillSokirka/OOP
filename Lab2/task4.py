import os
import re


class TextProcessor:

    def __init__(self, filename):
        if not os.path.exists(filename):
            raise NameError
        self.filename = filename
        self.text = TextProcessor.__read_file(filename)
        pass

    @staticmethod
    def __read_file(filename):
        with open(filename, "r", encoding="utf8") as file:
            return file.read()

    def get_characters(self) -> {}:
        character_dict = {}
        for char in self.text:
            if char in character_dict:
                character_dict[char] += + 1
            else:
                character_dict[char] = 1
        return character_dict

    def __get_words(self) -> []:
        temp = self.text
        temp = temp.replace("\n", " ")
        temp = re.sub(r"[?.!,]", " ", temp)
        words = temp.split()
        words.sort()
        return words

    def get_words(self) -> {}:
        words_dict = {}
        words = self.__get_words()
        for word in words:
            if word in words_dict:
                words_dict[word] += 1
            else:
                words_dict[word] = 1
        return words_dict

    def get_sentances(self):
        sentances = re.split(r"(?<=[.!?])\s+", self.text)
        for i in range(0, len(sentances)):
            if sentances[i] is None:
                continue
            if not i+1 == len(sentances):
                if sentances[i+1][0].islower():
                    sentances[i] += " " + sentances[i + 1]
                    sentances[i+1] = None
            sentances[i] = sentances[i].strip()
        result_sentances = []
        for sentance in sentances:
            if sentance is not None:
                result_sentances.append(sentance)
        return result_sentances


def main():
    text = TextProcessor("text.txt")
    write_to_file("sentances.txt", text.get_sentances())
    write_to_file("words.txt", text.get_words())
    write_to_file("characters.txt", text.get_characters())


def write_to_file(filename, data):
    with open(filename, "w") as file:
        if isinstance(data, dict):
            for item in data:
                file.write(f"{item} - {data[item]}\n")
        else:
            for item in data:
                file.write(f"{item}\n")

main()
