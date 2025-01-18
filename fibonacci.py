user_input=0
fib_seq=[0,1]


while len(fib_seq)<user_input:
  next_fib=fib_seq[-1]+fib_seq[-2]
  fib_seq.append(next_fib)

print(fib_seq)