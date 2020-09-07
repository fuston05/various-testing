import sys
import time

questions= {
  'q1': 'Are you doing ok today? ',
  # if yes
  'q2': 'What did you have for breakfast? ',
  # if no
  'q3': 'You wanna tell me about it? Yes or No? ',
  # if yes
  'q4': 'What\'s going on? ',
  # if no
  'q5': '',  
  'q6': '',  
}
responses= {
  # q1 'yes' response
  'r1': '\nGood, I\'m glad to hear it.\n',
  # q1 'no' response
  'r2': '\nI\'m sorry to hear that.\n',
  # q2
  'r3': '\nSounds.... strange to me, but what do I know? lol I had a BYTE but nothing special myself.\n',
  # q2, lengthy description
  'r4': '\nHoly cow, you type a lot!\n',
  'r5': '\nI am a great listener, I can do this til my battery dies. So, lay it on me!\n',
  'r6': '\nOk, I understand. If you change your mind just let me know, I am here for you.\n',
}

userInput= ''
curQ= questions['q1']

print('\nType "quit" to exit')

while userInput != 'q' and userInput != 'quit':
  print('')
  print('********')
  print('')

  userInput= input(curQ).strip().lower()

  if userInput == 'q' or userInput == 'quit':
    print('Goodbye\n')
    sys.exit(1)

  if curQ == questions['q1']:
      if userInput == 'yes':
        print(responses['r1'])
        time.sleep(2)
        curQ= questions['q2']

      elif userInput == 'no':
        print(responses['r2'])
        time.sleep(2)
        curQ= questions['q3']

      else:
        print('invalid entry')

  # breakfast question
  elif curQ == questions['q2']:

    if len(userInput) < 200:
      print(responses['r3'])

    elif len(userInput) >= 200:
      print(responses['r4'])
      time.sleep(1)
      print(responses['r3'])

    else:
      print('invalid entry')

  # wanna tell me about it?
  elif curQ == questions['q3']:
    if userInput =='yes':
      print(responses['r5'])
      curQ= questions['q4']
    elif userInput == 'no':
      print(responses['r6'])
    else:
      print('invalid input')
  