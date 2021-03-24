import doctest, csv, codecs, operator
from typing import List, Tuple, Dict, TextIO

DATE   = 0
NAME   = 1
YEAR   = 2
USER   = 4
LB_URL = 3
RATING = 4

NEW_NAME      = 0
NEW_YEAR      = 1
NEW_RATING    = 2
NEW_USER      = 3
COUNT_INDEX   = 4
MASTERLIST    = []

def first_entry(filename: str):
    write = 'w'
    create_masterlist(filename, write)


def create_masterlist(filename: str, add_write: str):
    file_handle = csv.reader(open(filename))
    full_info   = list(file_handle)
    
    file_use = open('masterlist.txt', add_write)
    prompt   = ('Who\'s file is this? ')
    user     = input(prompt)
    
    for film in full_info[1:]:
        name   = film[NAME]
        year   = film[YEAR]
        rating = film[RATING]
        info   = (name + ' | ' + year + ' | ' + rating + ' | ' + user)
        file_use.write(f'{info}\n')
        
    file_use.close()
    

def add_entry(filename: str):
    add = 'a'
    create_masterlist(filename, add)
    

def average(filename: str, order: str) -> dict:
    file_handle   = codecs.open(filename, mode='r', encoding='utf-8')
    all_averages  = {}
    checked = []
    master  = []
    limit   = 7
    
    for line in file_handle:
        #opens and reads the file
        line    = line.rstrip()
        lofilms = line.split(' | ')
        master.append(lofilms)  
    
    for film1 in master:
        title1  = film1[NEW_NAME]
        rating1 = float(film1[NEW_RATING])
        user1   = film1[NEW_USER]
        count   = 1
        i = 1
        
        if ((title1 in checked) == False):
            checked.append(title1)
            total  = rating1  
            
            for film2 in master[i:]:
                i += 1
                user2 = film2[NEW_USER]
                title2  = film2[NEW_NAME]
                rating2 = float(film2[NEW_RATING])
                
                if (title1 == title2):
                    total += rating2
                    count += 1
        else:
            i += 1
            
        if count >= limit:
            avg   = total/count
            all_averages[title1] = avg
    print(avg)
    
    if order == 'top':
        all_averages = dict( sorted(all_averages.items(), key=operator.itemgetter(1),reverse=True))
    else:
        all_averages = all_averages = dict( sorted(all_averages.items(), key=operator.itemgetter(1),reverse=False))
    
    return all_averages

                
def topfilms(masterlist: str, length: int) -> str:
    file_use   = open('toplist.txt', 'w')    
    dict_films = average(masterlist, 'top')
    count = 0        
    
    for film, avg in dict_films.items():
        count += 1
        if (count <= length):        
            films  = (str(count) + ' - ' + film + ': ' + str(avg))
            file_use.write(f'{films}\n')
            
    file_use.close()
    return 'Check the .txt file hun'

def bottomfilms(masterlist: str, length: int) -> str:
    file_use   = open('bottomlist.txt', 'w')    
    dict_films = average(masterlist, 'bottom')
    count = 0        
    
    for film, avg in dict_films.items():
        count += 1
        if (count <= length):        
            films  = (str(count) + ' - ' + film + ': ' + str(avg))
            file_use.write(f'{films}\n')
            
    file_use.close()
    return 'Check the .txt file'