# Library of commonly used functions
# v1.00
import csv

def index_by_tree (string, dictionary, next_available_index):
    """   
    The function checks whether string is already present in a tree structure "dictionary".
    If yes, returns its index.
    If not, puts it to the structure and assigns it next_available_index.
    This is returned as index and next_available_index is encrased by 1
    
    Input:
    string - the string to be checked
    dictionary - tree dictionary
    next_available_index
    
    Output:
    index - the index of string in the structure
    next_available_index - the next available index to be used    
    """
    
    # sets the current level of dictinary to the the top one
    current_dictionary = dictionary
    
    for i in range(len(string)):
        current_letter = string[i]
        try:
            current_dictionary = current_dictionary[current_letter]  # if the next level dicionary exists move to it
        except KeyError:
            current_dictionary[current_letter] = {}                  # create a new next level dicionary
            current_dictionary = current_dictionary[current_letter]  # set it as the current dictionary
        
    # when we are at the last level dictionary for this string to the following
    try:
        index = current_dictionary['ind'] # if index exists just return it
    except KeyError:
        index = next_available_index
        current_dictionary['ind'] = next_available_index  # if this proved to be a new string assign it a new index
        next_available_index += 1                         # move next available index to the next available one

    return (index, next_available_index)   

def list_to_file (list, full_path):
    
    '''
    Saves a list of strings to a tab-delimited csv file
    Input:  
    list - a list to be saved
    full_path - a string specifing a full path to a file 
    '''    
    
    with open(full_path, 'w', newline='') as f:
        f_object = csv.writer(f, delimiter='\t')
        for i in range(len(list)):
            f_object.writerow([list[i]])

def list_from_file (full_path):
    '''
    Reads a list from a csv file where eache row contains only 1 element
    
    Input: 
    full_path - a string specifing a full path to a file 
    
    Output:
    list - list with the data loaded from the file
    '''
    list = []
    with open(full_path) as f:
        f_object = csv.reader(f, delimiter='\t')
        for row in f_object:
            list.append(row[0])
    return list

def list_of_lists_from_file (full_path):
    '''
    Reads a list of lists from a csv file
    
    Input: 
    full_path - a string specifing a full path to a file 
    
    Output:
    list - list with the data loaded from the file
    '''
    list = []
    with open(full_path) as f:
        f_object = csv.reader(f, delimiter='\t')
        for row in f_object:
            list.append(row)
    return list

