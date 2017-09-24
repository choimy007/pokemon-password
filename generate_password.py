import extract_names
import random

# generate password using pokedex
# Input: list of wanted pokemon generation
# Output: Simple xkcd-style password
def generatePassword(arg):
  pokeList = []
  dex = extract_names.ExtractNames(arg)
  for x in range(0, 4):
    pokeList.append(random.SystemRandom().choice(dex))
  password = ''.join(pokeList)
  
  return password

