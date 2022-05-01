def generateDic(string):
    dic = {}

    for letter in string:
        lowered_letter = letter.lower()

        if lowered_letter in dic:
            dic[lowered_letter] += 1
        else:
            dic[lowered_letter] = 1

    return dic


def is_anagram(first_string, second_string):
    dic1 = generateDic(first_string)
    dic2 = generateDic(second_string)

    return dic1 == dic2
