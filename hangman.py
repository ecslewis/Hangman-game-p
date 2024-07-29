wrong_guesses_count=0
HANGMAN = ['''
  +---+
  |   |
      |
      |
      |
      |    
=========''', '''

  +---+
  |   |
  o   |
      |
      |
      |    
=========''', '''

  +---+
  |   |
  o   |
  |   |
      |
      |    
=========''', '''

  +---+
  |   |
  o   |
 /|   |
      |
      |    
=========''', '''

  +---+
  |   |
  o   |
 /|\  |
      |
      |    
=========''', '''

  +---+
  |   |
  o   |
 /|\  |
 /    |
      |    
=========''', '''

  +---+
  |   |
  o   |
 /|\  |
 / \  |
      |    
=========''']

def getRandomWord(wordList):
   ''' returns a random word from a chosen list of words'''
   import random
   wordIndex = random.randint(0, len(wordList) - 1)
   return wordList[wordIndex]

menu= """
Let's Plan Hangman:
1. Enter player's first name
2. Choose a word category
3. Play a game
4. Exit
Enter your selected option:"""
menu2="""
Choose a category(1,2 or 3):
1) Fruits
2) Countries
3) Veggies
Enter your selected option:"""
Fruits= ['orange', 'nectarine', 'banana', 'grapefruit', 'watermelon',
         'cantaloupe', 'raspberry', 'apricot', 'mandarin', 'cherry']
Countries= ['vietnam','canada','nigeria','cameroon','france','switzerland','germany','brazil',
            'argentina','portugal']
Veggies= ['lettuce','carrot','broccoli','potato','garlic','tomato','onions',
          'mushroom','cucumber','pickle']
info1= False
info2= False
choice=1
while True:
   choice=int(input(menu))
   if choice==1:
      name=input("Enter your name:")
      if not name[0].isupper():
         print('Invalid, capitalize')
         continue
      if not name.isalpha():
         print('Invalid, please enter only letters')
         continue
      info1=True
   elif choice==2:
      category=input(menu2)
      if category=='1':
         random=getRandomWord(Fruits)
      elif category=='2':
         random=getRandomWord(Countries)
      elif category=='3':
         random=getRandomWord(Veggies)
      else:
         print("Please input a valid choice")
         continue
      info2=True
   elif choice==3:
      wrong_guesses_count=0
      if not info1:
         print("Please enter your name")
         continue
      if not info2:
         print("Please choose a category")
         continue
      length=len(random)*'_'
      wordguess=list(length)
      print('Your guess:', wordguess)
      word=list(random)
      MissedLetters=[]
      stop=False
      stop1=False
      stop2=False
      while wrong_guesses_count<=7:
         if stop:
            break
         elif stop2:
            break
         guess=input("Guess a letter:")
         if guess in word:
            some=0
            for i in word:
               if guess==i:
                  x=word.index(i,some)
                  wordguess[x]=guess
                  some=x+1
               if ''.join(wordguess)==''.join(word):
                  print(wordguess)
                  print("You got it, the word was", ''.join(word))
                  print('It took you', wrong_guesses_count, 'wrong tries to get the answer')
                  stop=True
                  stop1=True
                  break
            if stop1:
               break
            print('Your guess:', wordguess)
            print(HANGMAN[wrong_guesses_count])
            print("Wrong guesses:", MissedLetters)
         elif guess in MissedLetters:
            print("Already typed, try another letter")
            print('Your guess:', wordguess)
            print(HANGMAN[wrong_guesses_count])
            print('Already guessed:', MissedLetters)
            continue
         else:
            wrong_guesses_count+=1
            if wrong_guesses_count==7:
               print("out of tries, the answer was:", ''.join(word))
               break
            else:
               MissedLetters.append(guess)
               print(wordguess)
               print(HANGMAN[wrong_guesses_count])
               print("Wrong guesses:", MissedLetters)


   elif choice==4:
      print('Exiting...')
      break
   else:
      print('Invalid option, choose a valid option')
      
