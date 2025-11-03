"""
python function to clean lists by removing duplicates

"""

def remove_duplicates(listy:list) -> list:

    """
    function to remove duplicates in a list
    """

    empty_list = []

    for element in listy:
        if element not in empty_list:
            empty_list.append(element)

    return empty_list


if __name__ == '__main__':
    print('This module has been executed directly.')
