#tableformat.py
#exercise 4.6
from typing import TypeVar, List, Dict

type_of_rowdata = TypeVar('type_of_rowdata', str, int, float)

class TableFormatter:

    def heading(self, header: List[str]):
        '''
        print table header
        '''
        raise NotImplementedError()

    def row(self, rowdata: List[type_of_rowdata]):
        '''
        print a single row of data
        '''
        raise NotImplementedError()
    
    def foot(self, count_data: Dict[str, float]):
        '''
        print footer of table
        '''
        raise NotImplementedError()

class TextTableFormatter(TableFormatter):
    
    def heading(self, header:List[str]):
        print(f'{header[0]:>10s} {header[1]:>10s} {header[2]:>10s} {header[3]:>10s}')
        print(('-'*10+' ')*4)
    
    def row(self, rowdata: List[type_of_rowdata]):
        print(f'{rowdata[0]:>10s} {rowdata[1]:10d} {rowdata[2]:10.2f} {rowdata[3]:10.2f}')
    
    def foot(self, count_data: Dict[str, float]):
        print(f'intres: {count_data["intres"]:.2f} total_cost: {count_data["total_cost"]:.2f}')