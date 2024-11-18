"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(layers):
    """Calculate the reuqired preparation time in minutes depending on the number of layers.

    :param layers: int - number of layers in the lasagna.
    :return: int - preparation time (in minutes) needed.    
    """
    return 2*layers


def elapsed_time_in_minutes(layers, time):
    """Calculate the elapsed time in minutes by considering the number of layers.

    :param layers: int - number of layers in the lasagna.
    :param time: int - elapsed time (in minute) in the oven.
    :return: int - total elapsed time in minute.
    """
    return preparation_time_in_minutes(layers)+time
