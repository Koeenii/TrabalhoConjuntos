## Importar livrarias utilizadas
import os.path

## Definição de Variaveis iniciais
keepRunning = True

## Requisita um Input do tipo Boolean
def getBooleanInput(message, trueString, falseString):
    boolInput = input(message).lower()
    while boolInput != trueString and boolInput != falseString:
        print("Input invalido, tente novamente")
        boolInput = input(message).lower()
    if boolInput == trueString:
        return True
    else:
        return False

## Requisita o Arquivo que o usuario deseja lêr, retornando o arquivo TXT caso encontrado ou Retornando Falso para arquivos invalidos
def requestFile():
    print("Digite o Nome do arquivo que deseja lêr sem adicionar a extensão ao final, note que o arquivo deve estar na pasta 'examples' e ser do formato TXT.")
    fileName = input("Nome do Arquivo: ")
    filePath = "examples/" + fileName + ".txt"

    if os.path.exists(filePath):
        file = open(filePath, 'r')
        return file
    else:
        print('Arquivo com este nome não existe.')
        return False

## Transforma uma String em um Conjunto de Números e o retorna
def stringToGroup(string):
    group = []
    currString = ''
    for x in range(len(string)):
        if string[x] == ',':
            group.append(int(currString))
            currString = ''
        elif x == len(string) - 1:
            group.append(int(currString + string[x]))
        else:
            currString += string[x]
    return group

## Transforma um grupo em uma String Formatada e a retorna
def groupToFString(group):
    count = 1
    currString = '{'
    for x in group:
        currString += str(x)
        if count < len(group):
            count += 1
            currString += ','
    currString += '}'
    return currString


## Resolve uma Conjunção entre 2 grupos e imprime o resultado no Console
def conjuctionOperation(group1, group2):
    resultGroup = []
    for x in group1:
        resultGroup.append(x)
    for x in group2:
        if not resultGroup.count(x):
            resultGroup.append(x)
    
    print("União: conjunto 1", groupToFString(group1) + ",", "conjunto 2", groupToFString(group2) + ".", "Resultado:", groupToFString(resultGroup))

## Resolve uma Interseção entre 2 grupos e imprime o resultado no Console
def intersectionOperation(group1, group2):
    resultGroup = []
    for x in group1:
        if group2.count(x) and not resultGroup.count(x):
            resultGroup.append(x)

    print("Interseção: conjunto 1", groupToFString(group1) + ",", "conjunto 2", groupToFString(group2) + ".", "Resultado:", groupToFString(resultGroup))

def differenceOperation(group1, group2):
    resultGroup = []
    for x in group1:
        if not group2.count(x) and not resultGroup.count(x):
            resultGroup.append(x)

    print("Diferença: conjunto 1", groupToFString(group1) + ",", "conjunto 2", groupToFString(group2) + ".", "Resultado:", groupToFString(resultGroup))

def cartesianOperation(group1, group2):
    count = 1
    resultString = "{"
    for x in group1:
        for y in group2:
            resultString += "(" + str(x) + "," + str(y) + ")"
            if count < len(group1) * len(group2):
                count += 1
                resultString += ","
    resultString += "}"
    print("Produto Cartesiano: conjunto 1", groupToFString(group1) + ",", "conjunto 2", groupToFString(group2) + ".", "Resultado:", resultString)

## Interpreta uma Operação
def interpretOperation(operationType, group1, group2):
    if operationType == 'U':
        conjuctionOperation(group1, group2)
    elif operationType == 'I':
        intersectionOperation(group1, group2)
    elif operationType == 'D':
        differenceOperation(group1, group2)
    elif operationType == 'C':
        cartesianOperation(group1, group2)
    else:
        print("Tipo de operação inválido.")

## Interpreta incialmente o Arquivo
def interpretFile(file):
    lines = file.readlines()
    operationCount = int(lines[0].replace("\n",""))
    for x in range(operationCount):
        step = 3 * x

        operationType = lines[step + 1].replace("\n","")
        group1 = stringToGroup(lines[step + 2].replace("\n",""))
        group2 = stringToGroup(lines[step + 3].replace("\n",""))

        interpretOperation(operationType, group1, group2)

## Loop Principal do Programa
while keepRunning:
    file = requestFile()

    if file:
        interpretFile(file)
    else:
        print('Tente Novamente.')

    file.close()

    keepRunning = getBooleanInput("Deseja continuar o programa? (s/n): ", "s", "n")