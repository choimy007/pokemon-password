import generate_password

if __name__ == "__main__":
  genString = raw_input('List generations separated by space: ')
  genList = map(int, genString.split())
  print generate_password.generatePassword(genList)
  