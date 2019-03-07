"""
Type descriptions of Twitterverse and Query dictionaries
(for use in docstrings)

Twitterverse dictionary:  dict of {str: dict of {str: object}}
    - each key is a username (a str)
    - each value is a dict of {str: object} with items as follows:
        - key "name", value represents a user's name (a str)
        - key "location", value represents a user's location (a str)
        - key "web", value represents a user's website (a str)
        - key "bio", value represents a user's bio (a str)
        - key "following", value represents all the usernames of users this 
          user is following (a list of str)
       
Query dictionary: dict of {str: dict of {str: object}}
   - key "search", value represents a search specification dictionary
   - key "filter", value represents a filter specification dictionary
   - key "present", value represents a presentation specification dictionary

Search specification dictionary: dict of {str: object}
   - key "username", value represents the username to begin search at (a str)
   - key "operations", value represents the operations to perform (a list of str)

Filter specification dictionary: dict of {str: str}
   - key "following" might exist, value represents a username (a str)
   - key "follower" might exist, value represents a username (a str)
   - key "name-includes" might exist, value represents a str to match (a case-insensitive match)
   - key "location-includes" might exist, value represents a str to match (a case-insensitive match)

Presentation specification dictionary: dict of {str: str}
   - key "sort-by", value represents how to sort results (a str)
   - key "format", value represents how to format results (a str)
       
"""

# Write your Twitterverse functions here

# Variable twv is short for twitterverse dictionary.


def process_data(data_file):
    """(file open for reading) -> Twitterverse dictionary
    
    Read data_file and return twv in Twitterverse dictionary format.
    """
    
    twv = {}
    username = data_file.readline().strip()
    
    while username != '':
        
        twv[username] = {}
        twv_sub = {'name':'', 'location':'', 'web':'', 'bio':'',
                            'following':[]}
        twv_sub['name'] += data_file.readline().strip()
        twv_sub['location'] += data_file.readline().strip()
        twv_sub['web'] += data_file.readline().strip()    
        
        # Knowing the order the data appears in data_file ensures the proper 
        # placement of data into dictionary format without evaluating it.
        
        line = data_file.readline() 
        while line != 'ENDBIO\n':
            twv_sub['bio'] += line
            line = data_file.readline()
        twv_sub['bio'] = twv_sub['bio'][0:-1]
        
        # Does not call method strip on above lines to keep the line exactly 
        # the same as in the data file.
        
        line = data_file.readline().strip()    
        while line != 'END':
            twv_sub['following'].append(line)
            line = data_file.readline().strip()
        twv[username] = twv_sub
        username = data_file.readline().strip()
        
    return twv


def process_query(query_file):
    """(file open for reading) -> query dictionary
    
    Read query_file and return query_dict in query dictionary format. 
    """
    
    query_dict = {'search':{'username':'', 'operations':[]},'filter':{}, 
                  'present':{}}
    line = query_file.readline().strip()
    query_dict['search']['username'] += query_file.readline().strip()
    
    line = query_file.readline().strip()    
    while line != 'FILTER':
        query_dict['search']['operations'].append(line)
        line = query_file.readline().strip()
        
    line = query_file.readline().strip()    
    while line != 'PRESENT':
        filter_line = line.split()
        query_dict['filter'][filter_line[0]] = filter_line[1]
        line = query_file.readline().strip() 
    
    line = query_file.readline().strip() 
    while line != '':
        filter_line = line.split()
        query_dict['present'][filter_line[0]] = filter_line[1]
        line = query_file.readline().strip() 
        
    return query_dict


def all_followers(twv, username):
    """(Twitterverse dictionary, str) -> list of str
    
    Return list of str followers, which contains all users, in twitterverse 
    twv, that are following str username.
    
    >>> twv = {\
    'a':{'name':'A', 'location':'', 'web':'', 'bio':'',\
    'following':['JustinTrudeau', 'StephenHarper', 'TomMulcair']},\
    'b':{'name':'B', 'location':'', 'web':'', 'bio':'', 'following':['a']},\
    'c':{'name':'C', 'location':'', 'web':'', 'bio':'',\
    'following':['a', 'b']}}
    >>> result = all_followers(twv, 'a')
    >>> result.sort()
    >>> result
    ['b', 'c']
    
    >>> twv = {\
    '1':{'name':'One', 'location':'', 'web':'', 'bio':'',\
    'following':['Putin', 'XiaopingDeng', 'Obama']},\
    '2':{'name':'Two', 'location':'', 'web':'', 'bio':'', 'following':[]},\
    '3':{'name':'Three', 'location':'', 'web':'', 'bio':'', 'following':[]}}
    >>> all_followers(twv, '1')
    []
    """
    
    followers = []    
    
    for user in twv:
        if username in twv[user]['following']:
            followers.append(user)
            
    return followers


def get_search_results(twv, search_dict):
    """(Twitterverse dictionary, search specification dictionary)
        -> list of str
    
    Perform the specified search on twitterverse twv, and return a list of str
    users that is all usernames in twitterverse twv that match the search 
    criteria. There will not be duplicates in users.   
    
    >>> twv = {\
    'a':{'name':'A', 'location':'', 'web':'', 'bio':'', 'following':[]},\
    'b':{'name':'B', 'location':'', 'web':'', 'bio':'', 'following':['a']},\
    'c':{'name':'C', 'location':'', 'web':'', 'bio':'',\
    'following':['a', 'b']},\
    'd':{'name':'D', 'location':'', 'web':'', 'bio':'',\
    'following':['a', 'b', 'c']},\
    'e':{'name':'E', 'location':'', 'web':'', 'bio':'',\
    'following':['a', 'b','c', 'd' ]},\
    'f':{'name':'F', 'location':'', 'web':'', 'bio':'',\
    'following':['a', 'b','c', 'd', 'e']}}
    >>> query_dict = {'search': {'username': 'f',\
    'operations': ['following', 'following','following']},\
    'filter': {},\
    'present': {'sort-by': '', 'format': ''}}
    >>> get_search_results(twv, query_dict['search'])
    ['a', 'b', 'c']
    
    >>> twv = {\
    '1':{'name':'One', 'location':'', 'web':'', 'bio':'',\
    'following':['Putin', 'XiaopingDeng', 'Obama']},\
    '2':{'name':'Two', 'location':'', 'web':'', 'bio':'', 'following':[]},\
    '3':{'name':'Three', 'location':'', 'web':'', 'bio':'', 'following':[]}}
    >>> query_dict = {\
    'search': {'username': '1', 'operations': ['followers']},\
    'filter': {},\
    'present': {'sort-by': '', 'format': ''}}
    >>> get_search_results(twv, query_dict['search'])
    []
    """
    
    users = [search_dict['username']]
    
    for search_operation in search_dict['operations']:
        if search_operation == 'following':
            follows = []            
            for user in users: 
                if user in twv:
                    follows.extend(twv[user]['following'])
            users = remove_duplicates(follows)
            
        if search_operation == 'followers':
            followers = []
            for user in users:
                followers.extend(all_followers(twv, user))
            users = remove_duplicates(followers)
            
    return users


def remove_duplicates(users_list):
    """(list of str) -> list of str
    
    Return list of str user_list with all duplicated items removed.
    
    >>> remove_duplicates(['a', 'a', 'a', 'b', 'b', 'c', 'c', 'd'])
    ['a', 'b', 'c', 'd']
    
    >>> remove_duplicates([])
    []
    """
    
    users_list.sort()
    
    for i in range(len(users_list)):
        while i < (len(users_list) - 1) and users_list[i] == users_list[i + 1]:
            users_list.pop(i + 1)
            
    return users_list


def get_filter_results(twv, users, filter_dict):
    """(Twitterverse dictionary, list of str, filter specification dictionary)
        -> list of str

    Perform the specified filter on users, and return a list of str 
    filtered_users that is all usernames in users that match the filter 
    criteria. 
    
    >>> twv = {\
    'a':{'name':'A', 'location':'China', 'web':'', 'bio':'', 'following':[]},\
    'b':{'name':'B', 'location':'Germany', 'web':'', 'bio':'',\
    'following':['a']},\
    'c':{'name':'C', 'location':'England', 'web':'', 'bio':'',\
    'following':['a', 'b']},\
    'd':{'name':'D', 'location':'Denmark', 'web':'','bio':'',\
    'following':['a', 'b', 'c']}}
    >>> query_dict = {'search': {'username': '', 'operations': []},\
    'filter': {'location-includes':'E', 'follower':'d'},\
    'present': {'sort-by': '', 'format': ''}}
    >>> users = ['a', 'b', 'c', 'd']
    >>> get_filter_results(twv, users, query_dict['filter'])
    ['b', 'c']
    
    >>> twv = {\
    'a':{'name':'Apple', 'location':'', 'web':'', 'bio':'', 'following':[]},\
    'b':{'name':'Banana', 'location':'', 'web':'', 'bio':'',\
    'following':['a']},\
    'c':{'name':'Cherry', 'location':'', 'web':'', 'bio':'',\
    'following':['a', 'b']},\
    'd':{'name':'Dragonfruit', 'location':'', 'web':'', 'bio':'',\
    'following':['a', 'b', 'c']}}
    >>> query_dict = {'search': {'username': '', 'operations': []},\
    'filter': {'name-includes':'a', 'following':'a'},\
    'present': {'sort-by': '', 'format': ''}}
    >>> users = ['a', 'b', 'c', 'd']
    >>> get_filter_results(twv, users, query_dict['filter'])
    ['b', 'd']
     """
    
    rem_users = []
    for user in users:
        rem_users.append(user)
        
    # rem_users is equivalent to users but not stored in the same id space to
    # not modify the list users        
    
    for filter_operation in filter_dict:
        
        to_remove = []
       
        if filter_operation == 'name-includes':
            for user in rem_users:
                if filter_dict['name-includes'].lower()\
                   not in twv[user]['name'].lower():
                    to_remove.append(user)
        
        elif filter_operation == 'location-includes':
            for user in rem_users:
                if filter_dict['location-includes'].lower()\
                   not in twv[user]['location'].lower():
                    to_remove.append(user)            
        
        elif filter_operation == 'follower':
            for user in rem_users:
                if user not in twv[filter_dict['follower']][
                    'following']:
                    to_remove.append(user)
        else:
            for user in rem_users:
                if user not in all_followers(twv,
                                            filter_dict['following']):
                    to_remove.append(user)
        
        for user in to_remove:
            rem_users.remove(user)
    
    return rem_users
    

def get_present_string(twv, users, present_dict):
    """(Twitterverse dictionary, list of str, 
        presentation specification dictionary) -> str
        
    Format data in list of str users for presentation based on the given 
    presentation specification and return the formatted string.
    
    >>> twv = {\
    'Damon':{'name':'Damon', 'location':'China', 'web':'damon.com',\
    'bio':'Hi','following':['Tina']},\
    'Jaryd':{'name':'Jaryd', 'location':'Vancouver', 'web':'Jaryd.com',\
    'bio':'Hey', 'following':['Tina']},\
    'Tina':{'name':'Tinarific', 'location':'England', 'web':'super.com',\
    'bio':'Hey Cutie', 'following':[]}}
    >>> query_dict = {'search': {'username': '', 'operations': []},\
    'filter': {'name-includes':'', 'following':''},\
    'present': {'sort-by': 'popular', 'format': 'long'}}
    >>> users = ['Damon', 'Jaryd', 'Tina']
    >>> print(get_present_string(twv, users, query_dict['present']))
    ----------
    Tina
    name: Tinarific
    location: England
    website: super.com
    bio:
    Hey Cutie
    following: []
    ----------
    Damon
    name: Damon
    location: China
    website: damon.com
    bio:
    Hi
    following: ['Tina']
    ----------
    Jaryd
    name: Jaryd
    location: Vancouver
    website: Jaryd.com
    bio:
    Hey
    following: ['Tina']
    ----------
    <BLANKLINE>
    
    >>> query_dict = {'search': {'username': '', 'operations': []},\
    'filter': {'name-includes':'', 'following':''},\
    'present': {'sort-by': 'username', 'format': 'short'}}
    >>> users = ['Damon', 'Jaryd', 'Tina']
    >>> get_present_string(twv, users, query_dict['present'])
    "['Damon', 'Jaryd', 'Tina']"
    """
    
    
    if present_dict['sort-by'] == 'username':
        tweet_sort(twv, users, username_first)
    
    elif present_dict['sort-by'] == 'name':
        tweet_sort(twv, users, name_first)
    
    else:
        tweet_sort(twv, users, more_popular)
    
    presentation = ''
    
    if present_dict['format'] == 'long':
        
        if len(users) == 0:
            return '----------\n----------\n'
        
        else:
            for user in users:
                presentation += ('----------\n{0}\nname: {1}\nlocation: {2}' +\
                    '\nwebsite: {3}\nbio:\n{4}\nfollowing: {5}\n').format(user,
                                        twv[user]['name'], 
                                        twv[user]['location'], 
                                        twv[user]['web'], 
                                        twv[user]['bio'], 
                                        twv[user]['following'])
        return presentation + '----------\n'
    
    else:
        return str(users)    
    

# --- Sorting Helper Functions ---
def tweet_sort(twitter_data, results, cmp):
    """ (Twitterverse dictionary, list of str, function) -> NoneType
    
    Sort the results list using the comparison function cmp and the data in 
    twitter_data.
    
    >>> twitter_data = {\
    'a':{'name':'Zed', 'location':'', 'web':'', 'bio':'', 'following':[]}, \
    'b':{'name':'Lee', 'location':'', 'web':'', 'bio':'', 'following':[]}, \
    'c':{'name':'anna', 'location':'', 'web':'', 'bio':'', 'following':[]}}
    >>> result_list = ['c', 'a', 'b']
    >>> tweet_sort(twitter_data, result_list, username_first)
    >>> result_list
    ['a', 'b', 'c']
    >>> tweet_sort(twitter_data, result_list, name_first)
    >>> result_list
    ['b', 'a', 'c']
    """
    
    # Insertion sort
    for i in range(1, len(results)):
        current = results[i]
        position = i
        while position > 0 and cmp(twitter_data, results[position - 1], current) > 0:
            results[position] = results[position - 1]
            position = position - 1 
        results[position] = current  
            
def more_popular(twitter_data, a, b):
    """ (Twitterverse dictionary, str, str) -> int
    
    Return -1 if user a has more followers than user b, 1 if fewer followers, 
    and the result of sorting by username if they have the same, based on the 
    data in twitter_data.
    
    >>> twitter_data = {\
    'a':{'name':'', 'location':'', 'web':'', 'bio':'', 'following':['b']}, \
    'b':{'name':'', 'location':'', 'web':'', 'bio':'', 'following':[]}, \
    'c':{'name':'', 'location':'', 'web':'', 'bio':'', 'following':[]}}
    >>> more_popular(twitter_data, 'a', 'b')
    1
    >>> more_popular(twitter_data, 'a', 'c')
    -1
    """
    
    a_popularity = len(all_followers(twitter_data, a)) 
    b_popularity = len(all_followers(twitter_data, b))
    if a_popularity > b_popularity:
        return -1
    if a_popularity < b_popularity:
        return 1
    return username_first(twitter_data, a, b)
    
def username_first(twitter_data, a, b):
    """ (Twitterverse dictionary, str, str) -> int
    
    Return 1 if user a has a username that comes after user b's username 
    alphabetically, -1 if user a's username comes before user b's username, 
    and 0 if a tie, based on the data in twitter_data.
    
    >>> twitter_data = {\
    'a':{'name':'', 'location':'', 'web':'', 'bio':'', 'following':['b']}, \
    'b':{'name':'', 'location':'', 'web':'', 'bio':'', 'following':[]}, \
    'c':{'name':'', 'location':'', 'web':'', 'bio':'', 'following':[]}}
    >>> username_first(twitter_data, 'c', 'b')
    1
    >>> username_first(twitter_data, 'a', 'b')
    -1
    """
    
    if a < b:
        return -1
    if a > b:
        return 1
    return 0

def name_first(twitter_data, a, b):
    """ (Twitterverse dictionary, str, str) -> int
        
    Return 1 if user a's name comes after user b's name alphabetically, 
    -1 if user a's name comes before user b's name, and the ordering of their
    usernames if there is a tie, based on the data in twitter_data.
    
    >>> twitter_data = {\
    'a':{'name':'Zed', 'location':'', 'web':'', 'bio':'', 'following':[]}, \
    'b':{'name':'Lee', 'location':'', 'web':'', 'bio':'', 'following':[]}, \
    'c':{'name':'anna', 'location':'', 'web':'', 'bio':'', 'following':[]}}
    >>> name_first(twitter_data, 'c', 'b')
    1
    >>> name_first(twitter_data, 'b', 'a')
    -1
    """
    
    a_name = twitter_data[a]["name"]
    b_name = twitter_data[b]["name"]
    if a_name < b_name:
        return -1
    if a_name > b_name:
        return 1
    return username_first(twitter_data, a, b)       


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    