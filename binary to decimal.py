def convert_to_decimal(binary):
  reversed_binary=binary[::-1]
  decimal=0
  for i in range(len(reversed_binary)):
    two_powered = (2**i)*int(reversed_binary[i])
    decimal=decimal+int(two_powered)

  return decimal

binary = '1011'

decimal=convert_to_decimal(binary)
print(f"{binary} to decimal is {decimal}")