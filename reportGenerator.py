import pandas as pd
import numpy as np
from functions import calcPercentage
from functions import printLedAndLeader
from functions import printAnalyze
from functions import printTotalAndPercentage
from functions import findLeaderComments

pd.options.mode.chained_assignment = None


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

## Analise de sentimentos com comentarios de liderados sem resposta dos lideres
rowsWithComments['Sem comentarios lider'] = rowsWithComments.apply(lambda row : findLeaderComments(row['Nome do Lider'], row['Comentarios']), axis = 1)
rowsWithCommentsWithoutLeaderAnswer = rowsWithComments[rowsWithComments['Sem comentarios lider'] == True]

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

print('\n\n\nSENTIMENTOS COM COMENTARIOS DO LIDERADO POREM SEM RESPOSTA DO LIDER')
print(rowsWithCommentsWithoutLeaderAnswer[['Nome', 'Nome do Lider']])
printTotalAndPercentage(len(rowsWithCommentsWithoutLeaderAnswer.index), len(rowsWithComments.index))