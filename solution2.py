''' This module taking input which is valid divisible by 2 and 3 '''

def validinput(n):
    ''' validate input '''
    if n%2==0 and n%3==0:
        return True
    return False    

def listofzeros(length):
    ''' returns list f zeros '''
    return [0]*length

def doWork(n):
    ''' this gives output of places where maths students should sit '''
    sitting = [] # sitting[column][row]
    sitting.append(listofzeros(n//2))
    sitting.append(listofzeros(n//2))
    if validinput(n):
        for i in range(2):
            for j in range(i,n//2,2):
                sitting[i][j] = "sit"
        return {
                'retCode': 0,
                'data': sitting
            }
    else:
        return {
                'retCode': 400,
                'error': 'Data is not valid'
            }

if __name__=="__main__":
    n = int(input("Enter number of students"))
    sitting = doWork(n)
    print (sitting)
    print ("Sitting array shows what are all the possible positions for math students to sit")
    for i in range(n//2):
        for j in range(2):
            print (sitting[j][i],end='\t')
        print ("\n")