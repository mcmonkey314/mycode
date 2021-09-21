#!/usr/bin/env python3

message = 'Your current grade is a'

# wrap connection in a float() to accept decimals as numbers

while True:
  val = input("Enter your test score:")
  try: 
    TestScore=int(val)
    break;
  except ValueError:
    try: 
      TestScore=float(val)
      break;
    except ValueError:  
      print("that's not a number")



if TestScore >=90:
  message = message + 'n A.  Nerd!'
elif TestScore >=80:
  message = message + ' B.  You may need to study a bit harder."'
elif TestScore >=70:
  message = message + ' C.  Slacker!!!'
elif TestScore >=60:
  message = message + ' D.  Hope you like summer school.'
else:
  message = message + 'n F.  You BIG Dummy!!!'

print(message)

#GetInput()


