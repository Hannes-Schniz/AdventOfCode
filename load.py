import os
from aocd import get_data
from datetime import datetime
class main:
    def load(day, year):

        filename = year + '/input/' + datetime.today().strftime('%Y-%m-%d')+'_input.txt'

        f = open(filename, 'a')
        f.write(get_data( day, year))
        f.close
        
    def __init__(cls, session):
        aoc_session = session
        os.environ['AOC_SESSION'] = aoc_session