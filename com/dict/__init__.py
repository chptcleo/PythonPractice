def sanitize(time_string):
    if '-' in time_string:
        splitter='-'
    elif ':' in time_string:
        splitter=':'
    else:
        return time_string
    (mins, secs)=time_string.split(splitter)
    return mins + "." + secs

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data=f.read()
            data_list=data.strip().split(',')
            return {'name':data_list.pop(0),'birth':data_list.pop(0),'times':str(sorted(set(sanitize(t) for t in data_list))[0:3])}
    except IOError as ioerr:
        print 'file error' + ioerr
        return None

player_dict=get_coach_data('james')
print player_dict['name'],' fast time is ',player_dict['times']