from collections import OrderedDict

def ConvertToRoman(i):
  
  roman = OrderedDict()
  roman[50] = "L"
  roman[40] = "XL"
  roman[10] = "X"
  roman[9] = "IX"
  roman[5] = "V"
  roman[4] = "IV"
  roman[1] = "I"

  def romanNum(i):
    for num in roman.keys():
      quotient, remainder = divmod(i, num)
      yield roman[num] * quotient
      i -= num * quotient
      if i > 0:
        romanNum(i)
      else:
        break

  return ''.join([a for a in romanNum(i)])
