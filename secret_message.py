def find_message(message: str) -> str:
    import re

    upper_letters = re.findall("[A-Z]+", message)
    return "".join(upper_letters)


if __name__ == "__main__":
    print("Example:")
    print(find_message(("How are you? Eh, ok. Low or Lower? " + "Ohhh.")))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert find_message(("How are you? Eh, ok. Low or Lower? " + "Ohhh.")) == "HELLO"
    assert find_message("hello world!") == ""
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD"
    print("Coding complete? Click 'Check' to earn cool rewards!")
