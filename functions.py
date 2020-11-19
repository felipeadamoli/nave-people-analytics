def printLedAndLeader(row):
    if not isinstance(row['Nome do Lider'], str):
        print('Membro: ' + row['Nome'])
    else:
        print('Membro: ' + row['Nome'] + ' | Lider: ' + row['Nome do Lider'])

def calcPercentage(part, whole):
  return str(100 * float(part)/float(whole)) + '%'

def printTotalAndPercentage(part, whole):
    print("\nTOTAL: " + str(part) + "\nPORCENTAGEM: " + calcPercentage(part, whole))

def printAnalyze(title, df, analizedRow):
    totalCount = 0
    print('\n\n\n' + title)
    for index, row in df.iterrows():
        if not isinstance(row[analizedRow], str): 
            printLedAndLeader(row)
            totalCount = totalCount + 1 
    printTotalAndPercentage(totalCount, len(df.index))