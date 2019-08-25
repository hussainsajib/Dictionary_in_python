import json

def loadData():
  return json.load(open('data.json'))

def definition(dict, word):
  retValue = ''
  if word in dict:
    retValue = dict[word]
  else:
    retValue = 'This word doesn\'t exist. Please check the word.'
  return retValue

def main():
  data = loadData()
  exit = True
  while True:
    word = input('Enter Word (:exit to quit): ')
    if word == ':exit':
      break
    else:
      print(definition(data, word))


if __name__ == '__main__': main()