# Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word
# within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also
# often referred to as Pascal case).


def to_camel_case(text):
    words = text.replace('-', ' ').replace('_', ' ').split()
    return words[0] + ''.join([word.capitalize() for word in words[1:]]) if text != "" else ""


if __name__ == '__main__':
    print(to_camel_case("the-stealth-warrior"))
    print(to_camel_case("The_Stealth_Warrior"))
    print(to_camel_case("the_stealth_warrior"))
    print(to_camel_case(""))