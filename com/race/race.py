'''
Created on Jul 2, 2015

@author: walchen
'''
import pickle
class AthleteList(list):
    
    def __init__(self, a_name, a_dob=None, a_times=[]):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)
        
    def top3(self):
        return sorted(set([sanitize(t) for t in self]))[0:3]
        
def sanitize(time):
    if '-' in time:
        splitter = '-'
    elif ':' in time:
        splitter = ':'
    else:
        return time
    (min, sec) = time.split(splitter)
    return str(min + "." + sec)

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.read()
            data_list = data.strip().split(',')
            return AthleteList(data_list.pop(0), data_list.pop(0), data_list)
    except IOError as ioerr:
        print 'file error' + ioerr
        return None

def put_to_store(files_list):
    ath_dict = {}
    for file in files_list:
        athlete = get_coach_data(file)
        ath_dict[athlete.name] = athlete
    try:
        with open('athlete.pickle', 'wb') as athf:
            pickle.dump(ath_dict, athf)
    except IOError as err:
        print 'file error', err
    return ath_dict

def get_from_store():
    ath_dict = {}
    try:
        with open('athlete.pickle', 'rb') as athf:
            ath_dict = pickle.load(athf)
    except IOError as err:
        print 'file error', err
    return ath_dict

files_list = ['james', 'sarah', 'kate', 'lily']
put_to_store(files_list)
ath_dict = get_from_store()
for ath in ath_dict:
    print ath_dict[ath].name, ath_dict[ath].dob, ath_dict[ath]
