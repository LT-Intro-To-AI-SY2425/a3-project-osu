import pandas as pd
from match import match
from typing import List, Tuple, Callable, Any

file_path = '/Users/jonathanhimawan/Documents/imdb_top_1000.csv'
movie = pd.read_csv(file_path)

##print(imdb_data.info())

def get_title(movie: Tuple[str, str, int, List[str]]) -> str:
    return movie[0]


def get_director(movie: Tuple[str, str, int, List[str]]) -> str:
    return movie[1]


def get_year(movie: Tuple[str, str, int, List[str]]) -> int:
    return movie[2]


def get_actors(movie: Tuple[str, str, int, List[str]]) -> List[str]:
    return movie[3]

def title_by_year(matches: List[str]) -> List[str]:
    """Finds all movies made in the passed in year

    Args:
        matches - a list of 1 string, just the year. Note that this year is passed as a
            string and should be converted to an int

    Returns:
        a list of movie titles made in the passed in year
    """
    result = []
    year = int(matches[0])
    print(year)
    for movie in movie:
        print(get_year(movie))
        print(get_title(movie))
        if get_year(movie) == year:
            result.append(get_title(movie))
            print("FOUND")
    return result


