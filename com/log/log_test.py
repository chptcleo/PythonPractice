'''
@author: Wallace Chen
'''
import logging

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filename='mylog.log')
    logging.info('Start program')
    logging.debug('1 divide 0')
    logging.info('After divide')
    logging.info('End program')