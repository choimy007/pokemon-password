# coding=utf-8
import bs4 
import urllib
import re
import unicodedata
import int_to_roman

def ExtractNames(arg):

  # loop through input & generate a list of all pokemon
  def generateList(*arg):
    pokeList = []
    for gen in arg:
      # generate url & variable names based on arg
      # Thank Arceus for Wikipedia
      roman = int_to_roman.ConvertToRoman(gen)
      url = urllib.urlopen('https://en.wikipedia.org/wiki/List_of_generation_' + roman + '_Pokémon').read()

      # find all span id of Pokemon and turn them into a string array
      span = bs4.BeautifulSoup(url, "html.parser").table.find_all('span', {'id' : re.compile('\S*')})
      dex = [pokemon.get('id').encode('ascii','replace') for pokemon in span]

      pokeList = pokeList + deleteMegas(dex)

    return pokeList
    
  # Delete all mega evolutions, primal forms & clean up all non-word characters 
  def deleteMegas(dex):
    nonAbc = re.compile('[^a-zA-Z]')
    newdex = [nonAbc.sub('' ,pokemon) for pokemon in dex if not (pokemon.startswith('Mega_') or pokemon.startswith('Primal'))]
    return newdex

  return generateList(*arg)


