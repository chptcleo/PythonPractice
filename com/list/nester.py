import sys
'''The nester.py provide one function called loop_list'''
def loop_list(the_list, level, out=sys.stdout):
    '''This function loop list even if the item is list'''
    for list_item in the_list:
        if isinstance(list_item, list):
            loop_list(list_item, level + 1, out)
        else:
            for tab_stop in range(level):
                print "\t",
            print list_item,out
            
players = ["kobe", "jordan", "james", ["mess", "CR7", ["cruise", "wallace"]]]
loop_list(players, 0)
