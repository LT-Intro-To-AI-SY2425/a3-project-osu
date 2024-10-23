import pandas as pd
import numpy as npclear
from match import match
from typing import List, Tuple, Callable, Any

file_path = '/Users/jonathanhimawan/Documents/IntrotoAI/a3-project-osu-1/imdb_1000.csv'
movie = pd.read_csv(file_path)

print(movie['Runtime'])
##print(imdb_data.info())

def get_title(movie):
    return movie['Series_Title']


def get_director(movie):
    return movie['Director']


def get_year(movie):
    return movie['Released_Year']


def title_by_year(matches):
    """Finds all movies made in the passed in year

    Args:
        matches - a list of 1 string, just the year. Note that this year is passed as a
            string and should be converted to an int

    Returns:
        a list of movie titles made in the passed in year
    """
    result = []
    year = int(matches[0])
    for movie in movie:
        print(get_year(movie))
        print(get_title(movie))
        if get_year(movie) == year:
            result.append(get_title(movie))
            print("FOUND")
    return result

pa_list: List[Tuple[List[str], Callable[[List[str]], List[Any]]]] = [
    (str.split("what movies were made in _"), title_by_year),
]

def search_pa_list(src: List[str]) -> List[str]:
    """Takes source, finds matching pattern and calls corresponding action. If it finds
    a match but has no answers it returns ["No answers"]. If it finds no match it
    returns ["I don't understand"].

    Args:
        source - a phrase represented as a list of words (strings)

    Returns:
        a list of answers. Will be ["I don't understand"] if it finds no matches and
        ["No answers"] if it finds a match but no answers
    """
    for pattern, action in pa_list:
        print(pattern, src, action)
        mat = match(pattern, src)
        print(mat)
        if mat != None:
            result = action(mat)
            if result == []:
                return ["No answers"]
            return result            
    return["I don't understand"]

