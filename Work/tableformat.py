#tableformat.py
#exercise 4.6
from typing import TypeVar, Tuple, Dict, Tuple

type_of_rowdata = TypeVar('type_of_rowdata', str, int, float)
type_of_row = Tuple[type_of_rowdata, ...]

class FormatterError(Exception):
    pass

class TableFormatter:

    def heading(self, header: Tuple[str,...]):
        '''
        print table header
        '''
        raise NotImplementedError()

    def row(self, rowdata: type_of_row):
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
    
    def heading(self, header: Tuple[str, ...]):
        print(*[f'{var:>10s}' for var in header])
        print(('-'*10+' ')*len(header))
    
    def row(self, rowdata: type_of_row):
        print(*[f'{var:>10s}' for var in rowdata])
        # print(f'{rowdata[0]:>10s} {rowdata[1]:10d} {rowdata[2]:10.2f} {rowdata[3]:10.2f}')
    
    def foot(self, count_data: Dict[str, float]):
        print(f'intres: {count_data["intres"]:.2f} total_cost: {count_data["total_cost"]:.2f}')

class CSVTableFormatter(TableFormatter):
    """
    output portfolio data in CSV format
    """
    def heading(self, header: Tuple[str, ...]):
        print(','.join(header))
    
    def row(self, rowdata: type_of_row):
        print(*rowdata, sep=',')

    def foot(self, count_data: Dict[str, float]):
        print(f'intres,{count_data["intres"]:.2f}')
        print(f'total_cost,{count_data["total_cost"]:.2f}')

def createFormatter(fmt: str = 'plantext') -> TableFormatter:
    '''
    creat formatter depend on a str
    '''
    if fmt == 'plantext':
        return TextTableFormatter()
    elif fmt == 'CSV':
        return CSVTableFormatter()
    else:
        raise FormatterError(f'No such formatter "{fmt}"')
    
