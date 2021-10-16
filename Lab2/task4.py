import os
import re


class TextProcessor:

    def __init__(self, filename):
        if not os.path.exists(filename):
            raise NameError
        self.filename = filename

    @staticmethod
    def __read_file(filename):
        with open(filename, "r", encoding="utf8") as file:
            return file.read()

    def get_info(self, mode):
        pass

    def get_characters(self) -> {}:
        character_dict = {}
        with open(self.filename, "r", encoding="utf8") as file:
            for line in file:
                for char in line:
                    if char in character_dict:
                        character_dict[char] += + 1
                    else:
                        character_dict[char] = 1
        return character_dict

    def __get_words(self) -> []:
        temp = ""
        with open(self.filename, "r", encoding="utf8") as file:
            for line in file:
                line = line.replace("\n", " ")
                temp += re.sub(r"[?.!,]", " ", line)
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
        sentances = re.split(r"(?<=[.!?])\s+", TextProcessor.__read_file(self.filename))
        for i in range(len(sentances)):
            if not sentances[i]:
                continue
            if not i+1 == len(sentances):
                if sentances[i+1][0].islower():
                    sentances[i] += " " + sentances[i + 1]
                    sentances[i+1] = None
        result_sentances = []
        for sentance in sentances:
            if sentance:
                result_sentances.append(sentance)
        return result_sentances


def main():
    text = TextProcessor("TextFiles/text.txt")
    write_to_file("TextFiles/sentances.txt", text.get_sentances())
    write_to_file("TextFiles/words.txt", text.get_words())
    write_to_file("TextFiles/characters.txt", text.get_characters())



def write_to_file(filename, data):
    with open(filename, "w") as file:
        if isinstance(data, dict):
            for item in data:
                file.write(f"'{item}' - {data[item]}\n")
        else:
            for item in data:
                file.write(f"{item}\n")


main()
