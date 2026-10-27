def reverse_string(text: str) -> str:
    reversed_text = ""

    for char in text:
        reversed_text = char + reversed_text

    return reversed_text


def count_vowels(text: str) -> int:
    vowels = "aeiouAEIOU"
    count = 0

    for char in text:
        if char in vowels:
            count += 1

    return count


if __name__ == "__main__":
    print("Reverse:", reverse_string("hello"))
    print("Vowels:", count_vowels("Hello World"))
