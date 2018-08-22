''' Temparatures are sent for two sensors seperatly 
and temparature values are increasing order '''


def validparams(parameters):
    ''' This checks if the parameters are valid '''
    if len(parameters) == 3:
        if parameters[0] in [1,2] and len(str(parameters[1]))==5:
            return True
        else:
            return False
    else:
        return False

def doWork(records,duration):
    ''' performs average for every second '''
    timeperioddict = {}
    starttime = records[0][1]
    for record in records: #getting least time 
        if validparams(record):
            if record[0] == 2:
                if starttime>record[1]:
                    starttime=record[1]
                break            
        else:
            return {
                'retCode': 400,
                'error': 'Data is not valid'
            }
    entered = False #make it True if processing 2nd sensor data
    timeperioddict[starttime] = [] #making first list
    lowerlimit = starttime
    for record in records:
        if validparams(record):
            if record[0] == 2 and not entered:
                lowerlimit = starttime
                entered = True
            while True:
                if record[1] < lowerlimit+duration:
                    if lowerlimit not in timeperioddict.keys():
                        timeperioddict[lowerlimit] = [] #making next list
                    timeperioddict[lowerlimit].append(record[2])
                    break
                lowerlimit += duration
        else:
            return {
                'retCode': 400,
                'error': 'Data is not valid'
            }
    result = []
    for key in timeperioddict.keys():
        arry = timeperioddict[key]
        avrg = float(sum(arry))/len(arry)
        avrg = float("{:.2f}".format(avrg))
        period = str(key)+'-'+str(key+duration-1)
        result.append([period, avrg]) 
    return {
        'retCode': 0,
        'data': result
    }


if __name__ == "__main__":
    records = [[1,10000,40],[1,10002,45],[1,11015,50],[2,10005,42],[2,11051,45],[2,12064,42],[2,13161,42]]
    duration = int(input("Enter duration for configuration in milli seconds"))
    result = doWork(records, duration)
    print (result)