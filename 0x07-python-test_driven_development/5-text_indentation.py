def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
    - text: a string

    Raises:
    - TypeError if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in ".?:":
        text = text.replace(char, "{}\n\n".format(char))

    print(text.strip())
