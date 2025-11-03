"""

python function to capatalise strings in a list

"""

def capitalise_strings(listy:list) -> list:

    """
    function to capatalise the first letter of every strign in a list
    """
    title_list = []

    for word in listy:
        title_list.append(word.title())

    return title_list

