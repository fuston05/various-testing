questions= {
  'q1': 'Are you doing ok today? ',
}
responses= {
  'r1': 'Good, I\'m glad to hear it.',
  'r2': 'I\'m sorry to hear that.'

}

userInput= ''
curQ= questions['q1']

print('\nType "quit" to exit')

while userInput != 'q' and userInput != 'quit':
  print('********')
  print('')

  userInput= input(curQ).strip().lower()
  
  if curQ == questions['q1']:
    
      if userInput == 'yes':
        curQ= responses['r1']
      elif userInput == 'no':
        curQ= responses['r2']
      else:
        print('invalid entry')

  elif curQ == questions['q1']:
    pass
  elif curQ == questions['q1']:
    pass
  