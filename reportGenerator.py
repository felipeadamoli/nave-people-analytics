import pandas as pd
import numpy as np
from functions import calcPercentage
from functions import printLedAndLeader
from functions import printAnalyze
from functions import printTotalAndPercentage


# df = pd.read_csv('sentimentos_old.csv')
df = pd.read_csv('sentimentos.csv')
totalRowCount = len(df.index)

## Analise de quantidade de respostas
withoutPulse = df[df['Classificacao do sentimento'].isnull()]
withPulse = df[np.logical_not(df['Classificacao do sentimento'].isnull())]
withPulseRowCount = len(withPulse.index)

## Analise existencia de tags
rowsWithoutTags = withPulse[withPulse['Tags do sentimento'].isnull()]

## Analise existencia de comentarios
rowsWithoutComments = withPulse[withPulse['Comentarios'].isnull()]
rowsWithComments = withPulse[np.logical_not(withPulse['Comentarios'].isnull())]

print('Fequencia sentimentos')
print(df['Classificacao do sentimento'].value_counts())

print('\n\n\nPorcentagem sentimentos')
print(df['Classificacao do sentimento'].value_counts(normalize=True))

print('\n\n\nMEMBROS COM SENTIMENTOS NEGATIVOS')
print(df[df['Classificacao do sentimento'] == 'Negativo'][["Nome", "Nome do Lider"]])

print('\n\n\nMEMBROS QUE NAO RESPONDERAM AO SENTIMENTO DA SEMANA')
print(withoutPulse[["Nome", "Nome do Lider"]])
print(printTotalAndPercentage(len(withoutPulse.index), totalRowCount))

print('\n\n\nRESPOSTAS SEM TAGS')
print(rowsWithoutTags[["Nome", "Nome do Lider"]])
print(printTotalAndPercentage(len(rowsWithoutTags.index), withPulseRowCount))

print('\n\n\nRESPOSTAS SEM COMENTARIOS')
print(rowsWithoutComments[["Nome", "Nome do Lider"]])
print(printTotalAndPercentage(len(rowsWithoutComments.index), withPulseRowCount))

print('\n\n\nSENTIMENTOS COM COMENTARIOS POREM SEM RESPOSTA DO LIDER')
withoutLeaderComments = 0
for index, row in df.iterrows():
    if isinstance(row['Comentarios'], str):
        if isinstance(row['Nome do Lider'], str): 
            if row['Nome do Lider'] not in row['Comentarios']:
                withoutLeaderComments = withoutLeaderComments + 1
                printLedAndLeader(row)
printTotalAndPercentage(withoutLeaderComments, len(rowsWithComments.index))
print("\n\n\n")