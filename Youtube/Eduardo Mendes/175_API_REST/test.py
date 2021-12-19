print()




a = {
    'André': [45, 'Fortaleza', 30000],
    'Ludmila': [43, 'Fortaleza', 20000]
}



dictOfNames = {
   7 : 'sam',
   8: 'john',
   9: 'mathew',
   10: 'riti',
   11 : 'aadi',
   12 : 'sachin'
}

newDict = dict(filter(lambda elem: elem[0] % 2 == 0, dictOfNames.))


print(newDict)

