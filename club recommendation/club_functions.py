""" CSC108 Assignment 3: Club Recommendations - Starter code."""
from typing import List, Tuple, Dict, TextIO


# Sample Data (Used by Doctring examples)

P2F = {'Jesse Katsopolis': ['Danny R Tanner', 'Joey Gladstone',
                            'Rebecca Donaldson-Katsopolis'],
       'Rebecca Donaldson-Katsopolis': ['Kimmy Gibbler'],
       'Stephanie J Tanner': ['Michelle Tanner', 'Kimmy Gibbler'],
       'Danny R Tanner': ['Jesse Katsopolis', 'DJ Tanner-Fuller',
                          'Joey Gladstone']}

P2C = {'Michelle Tanner': ['Comet Club'],
       'Danny R Tanner': ['Parent Council'],
       'Kimmy Gibbler': ['Rock N Rollers', 'Smash Club'],
       'Jesse Katsopolis': ['Parent Council', 'Rock N Rollers'],
       'Joey Gladstone': ['Comics R Us', 'Parent Council']}


# Helper functions 

def update_dict(key: str, value: str,
                key_to_values: Dict[str, List[str]]) -> None:
    """Update key_to_values with key/value. If key is in key_to_values,
    and value is not already in the list associated with key,
    append value to the list. Otherwise, add the pair key/[value] to
    key_to_values.

    >>> d = {'1': ['a', 'b']}
    >>> update_dict('2', 'c', d)
    >>> d == {'1': ['a', 'b'], '2': ['c']}
    True
    >>> update_dict('1', 'c', d)
    >>> d == {'1': ['a', 'b', 'c'], '2': ['c']}
    True
    >>> update_dict('1', 'c', d)
    >>> d == {'1': ['a', 'b', 'c'], '2': ['c']}
    True
    """

    if key not in key_to_values:
        key_to_values[key] = []
        
    if value not in key_to_values[key]:
        key_to_values[key].append(value)
    
                               
#Required functions

def load_profiles(profiles_file: TextIO) -> Tuple[Dict[str, List[str]],
                                                  Dict[str, List[str]]]:
    """Return a two-item tuple containing a "person to friends" dictionary
    and a "person_to_clubs" dictionary with the data from profiles_file.

    NOTE: Functions (including helper functions) that have a parameter of type
          TextIO do not need docstring examples.
    """
    person_to_friends = {}
    person_to_clubs = {}
    
    profiles = profiles_file.read().split('\n\n')
    for person in profiles:
        friends = []
        clubs = []
        name = person.split('\n')[0]
        j = name.find(',')
        persons_name = name[j + 2:] + ' ' + name[0:j]
        
        for line in person.split('\n')[1:len(profiles)]:
            if not ',' in line:
                clubs.append(line)
                clubs.sort()
                person_to_clubs[persons_name] = clubs
            else:
                i = line.find(',')
                friend_name = line[i + 2 : len(line)]+ ' ' + line[0 : i]
                friends.append(friend_name)
                friends.sort()
                person_to_friends[persons_name] = friends
                    
                    
    return person_to_friends, person_to_clubs
                        
                
def get_average_club_count(person_to_clubs: Dict[str, List[str]]) -> float:
    """Return the average number of clubs that a person in person_to_clubs
    belongs to.

    >>> get_average_club_count(P2C)
    1.6
    """
    if person_to_clubs == {}:
        return 0.0
    total = 0
    for club in person_to_clubs:    
        total += len(person_to_clubs[club])
    return total / len(person_to_clubs)


            
    
def get_last_to_first(person_to_friends: Dict[str, List[str]])\
    -> Dict[str, List[str]]:
    """Return a "last name to first name(s)" dictionary with the people from the
    "person to friends" dictionary person_to_friends.

    >>> get_last_to_first(P2F) == {
    ...    'Katsopolis': ['Jesse'],
    ...    'Tanner': ['Danny R', 'Michelle', 'Stephanie J'],
    ...    'Gladstone': ['Joey'],
    ...    'Donaldson-Katsopolis': ['Rebecca'],
    ...    'Gibbler': ['Kimmy'],
    ...    'Tanner-Fuller': ['DJ']}
    True
    """
    last_to_first = {}
    for name in person_to_friends:
        i = name.rfind(' ')
        lastname = name[i+1:]
        firstname = name[:i]
        if lastname not in last_to_first:
            last_to_first[lastname] = [firstname]
            
        elif lastname in last_to_first and firstname not in \
             last_to_first[lastname]:
            last_to_first[lastname].append(firstname)
        else:
            last_to_first = last_to_first
            
            
        for friend in person_to_friends[name]:
            j = friend.rfind(' ')
            lastname = friend[j+1:]
            firstname = friend[:j]
            if lastname in last_to_first and firstname in \
               last_to_first[lastname]:
                last_to_first = last_to_first
            elif lastname not in last_to_first:
                last_to_first[lastname] = [firstname]
            else:
                last_to_first[lastname].append(firstname)
                    
    for name in last_to_first:
        last_to_first[name].sort()
    return last_to_first
        
                    

def invert_and_sort(key_to_value: Dict[object, object]) -> Dict[object, list]:
    """Return key_to_value inverted so that each key is a value (for
    non-list values) or an item from an iterable value, and each value
    is a list of the corresponding keys from key_to_value.  The value
    lists in the returned dict are sorted.

    >>> invert_and_sort(P2C) == {
    ...  'Comet Club': ['Michelle Tanner'],
    ...  'Parent Council': ['Danny R Tanner', 'Jesse Katsopolis',
    ...                     'Joey Gladstone'],
    ...  'Rock N Rollers': ['Jesse Katsopolis', 'Kimmy Gibbler'],
    ...  'Comics R Us': ['Joey Gladstone'],
    ...  'Smash Club': ['Kimmy Gibbler']}
    True
    """
    inverted_dict = {}
    clubs_list = []
    
    for name in key_to_value:
        for club in key_to_value[name]:
            if club not in clubs_list:
                clubs_list.append(club)
        
    for club in clubs_list:
        inverted_dict[club] = []
        for name in key_to_value:
            if club in key_to_value[name]:
                inverted_dict[club].append(name)
                
    for club in inverted_dict:
        inverted_dict[club].sort()
    return inverted_dict
                

def get_clubs_of_friends(person_to_friends: Dict[str, List[str]],
                         person_to_clubs: Dict[str, List[str]],
                         person: str) -> List[str]:
    """Return a list, sorted in alphabetical order, of the clubs in
    person_to_clubs that person's friends from person_to_friends
    belong to, excluding the clubs that person belongs to.  Each club
    appears in the returned list once per each of the person's friends
    who belong to it.

    >>> get_clubs_of_friends(P2F, P2C, 'Danny R Tanner')
    ['Comics R Us', 'Rock N Rollers']
    """
    clubs_found = []
    if person in person_to_friends:
        for friend in person_to_friends[person]:
            if friend in person_to_clubs:
                for club in person_to_clubs[friend]:
                    clubs_found.append(club)
        if person in person_to_clubs:
            persons_club = person_to_clubs[person]
            for club in clubs_found:
                if club in persons_club:
                    clubs_found.remove(club)
           
    clubs_found.sort()
    return clubs_found
    
            

                          
def recommend_clubs(
        person_to_friends: Dict[str, List[str]],
        person_to_clubs: Dict[str, List[str]],
        person: str,) -> List[Tuple[str, int]]:
    """Return a list of club recommendations for person based on the
    "person to friends" dictionary person_to_friends and the "person
    to clubs" dictionary person_to_clubs using the specified
    recommendation system.

    >>> recommend_clubs(P2F, P2C, 'Stephanie J Tanner',)
    [('Comet Club', 1), ('Rock N Rollers', 1), ('Smash Club', 1)]
    """
    my_dict = {}
    recommended_clubs = []
    
    clubs = get_clubs_of_friends(person_to_friends, person_to_clubs, person)
    
    for club in clubs:
        if club not in my_dict:
            my_dict[club] = 1
        else:
            my_dict[club] += 1
                
    
    
    for item in my_dict:
        recommended_clubs.append((item, my_dict[item]))
    return recommended_clubs
                                

            

if __name__ == '__main__':
    #pass

    # If you add any function calls for testing, put them here.
    # Make sure they are indented, so they are within the if statement body.
    # That includes all calls on print, open, and doctest.

    import doctest
    doctest.testmod()