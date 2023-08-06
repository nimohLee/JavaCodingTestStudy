A, B = input().split()

def setFiveOrSix(number):
    five_ver = ''
    six_ver = ''
    for i in number:
      if i == '5':
          five_ver += i
          six_ver += '6'
      elif i == '6':
          five_ver += '5'
          six_ver += i
      else:
          five_ver += i
          six_ver += i
    return five_ver, six_ver

five_A, six_A = setFiveOrSix(A)
five_B, six_B = setFiveOrSix(B)
print(f'{int(five_A) + int(five_B)} {int(six_A) + int(six_B)}')
