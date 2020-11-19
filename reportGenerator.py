import pandas as pd
from functions import calcPercentage
from functions import printLedAndLeader
from functions import printAnalyze
from functions import printTotalAndPercentage

df = pd.read_csv('sentimentos.csv')
# df = pd.read_csv('sentimentos_old.csv')

totalRowCount = len(df.index)
negativeFeelings = 0
withoutComments = 0
withoutLeaderComments = 0

print('Fequencia sentimentos')
print(df['Classificacao do sentimento'].value_counts())

print('\n\n\nPorcentagem sentimentos')
print(df['Classificacao do sentimento'].value_counts(normalize=True))


print('\n\n\nPESSOAS COM SENTIMENTOS NEGATIVOS')
for index, row in df.iterrows():
    if isinstance(row['Classificacao do sentimento'], str): 
        if row['Classificacao do sentimento'] == 'Negativo':
            negativeFeelings = negativeFeelings + 1
            printLedAndLeader(row)
printTotalAndPercentage(negativeFeelings, totalRowCount)

printAnalyze('NAO RESPONDEU', df, 'Classificacao do sentimento')

printAnalyze('SEM TAGS', df, 'Tags do sentimento')

printAnalyze('SEM COMENTARIOS', df, 'Comentarios')

print('\n\n\nSENTIMENTOS COM COMENTARIOS POREM SEM RESPOSTA DO LIDER')
for index, row in df.iterrows():
    if isinstance(row['Comentarios'], str): 
        if row['Nome do Lider'] not in row['Comentarios']:
            withoutLeaderComments = withoutLeaderComments + 1
            printLedAndLeader(row)
printTotalAndPercentage(withoutLeaderComments, totalRowCount - withoutComments)
print("\n\n\n")