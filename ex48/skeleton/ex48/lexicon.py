lex = {'north': 'direction', 'south': 'direction', 'east': 'direction',
      'go': 'verb', 'kill': 'verb', 'eat': 'verb',
      'the': 'stop', 'in': 'stop', 'of': 'stop',
      'bear': 'noun', 'princess': 'noun'
      }




def scan(phrase):
    #Creates a list that will be returned by the programm
    list = []
    #Slices the phrase passed to the function in single words
    words = phrase.split()

    for i in words:
        #Try to convert the words in numbers
        #If they are not numbers, the exception raises
        try:
            turp = ('number', int(i))
            list.append(turp)

        except ValueError:
            #Removing all the upper cases
            lower_words = i.lower()
            #Appending to the list all the words in the dictionary lex
            if lower_words in lex:
                turp = (lex[lower_words], lower_words)
                list.append(turp)
            #Handling the words not recognized
            else:
                turp = ('error', i)
                list.append(turp)

    return list
