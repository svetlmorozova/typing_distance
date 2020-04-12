from math import sqrt

import click

from typing_distance.utils import KEYBOARDS


@click.command()
@click.option('-s', '--string', help='Input string', prompt='string')
@click.option('-kb', '--keyboard', help='What keyboard to use',
              type=click.Choice(['MAC'], case_sensitive=False), default='MAC')
@click.option('-avg', '--averaged', help='Return average value', type=click.BOOL, default=False)
def get_typing_distance(string, keyboard, averaged):
    """Calculate and return typing distance for a given string"""
    distance = 0
    chosen_kb = KEYBOARDS[keyboard]
    try:
        for i in range(1, len(string)):
            x_1, y_1 = chosen_kb[string[i - 1]]
            x_2, y_2 = chosen_kb[string[i]]
            distance += int(sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2))
        if averaged:
            print(f'Averaged typing distance is {round(distance / ((len(string) - 1 )), 1)}')
        else:
            print(f'Typing distance is {distance}')
    except KeyError:
        print(f'Your line contains chars which are not presented in chosen keyboard: {keyboard}')
