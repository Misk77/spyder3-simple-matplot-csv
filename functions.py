import matplotlib.pyplot as plt
import csv
fileName="DATA.csv"
 
def makeplot(fileName):
    x=[]
    y=[]
    try: 
        with open(fileName, 'r') as csvfile:
            plots= csv.reader(csvfile, delimiter=',')
            for row in plots:
                x.append(int(row[0]))
                y.append(int(row[1]))
        
        plt.plot(x,y, marker='o')
        
        plt.title('Data from the CSV File: {}'.format(fileName))
        
        plt.xlabel('Year Dec')
        plt.ylabel('Depth Dec')
        
        plt.show()
    except IOError:
        print ("File not found!")
        
    
def highest_depth():
    """
    This function calc highest depth
    """
    
def min_depth():
    """
    This function calc min depth
    """
    
    
def needed_or_NOT():
    """
    Place for any other function?
    calc medium depth? calc diff, calc ????
    needed_or_NOT
    This function ???
    """
