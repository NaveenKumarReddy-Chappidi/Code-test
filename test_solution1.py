''' Write test cases for solution1 '''

import pytest as pytest
from solution1 import doWork

@pytest.fixture #can pass as arguments to test cases
def dataList():
    ''' provide data list obj '''
    return [[1,10000,40],[1,10002,45],[1,11015,50],[2,10005,42],[2,11051,45],[2,12064,42],[2,13161,42]]

@pytest.fixture #can pass as arguments to test cases
def durObj():
    ''' provide duration in millisec '''
    return 1000

def test_allsuccess(dataList, durObj): #testfunc name should be started with test
    ''' run the case where everything is fine '''
    result = doWork(dataList, durObj)
    assert result == {'retCode': 0, 'data': [['10000-10999', 42.33], ['11000-11999', 47.5], ['12000-12999', 42.0], ['13000-13999', 42.0]]}

def test_dataerror(dataList, durObj):
    ''' provide the data wrong '''
    dataList[0][1] = 20
    result = doWork(dataList, durObj)
    assert result == {'retCode': 400, 'error': 'Data is not valid'}