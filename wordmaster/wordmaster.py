import os
import random
import sys
print('''
                      THE
                   WORDMASTER

            *****WIN IF YOU CAN*****
    ''')
name=input("NAME:")
print('''MENU:
         1. JUMBLE ME UP!
         2. GUESS IF YOU CAN!
     ''')
print('\n Welcome',name,'To THE WORDMASTER')
choice=int(input("Enter your choice:"))
if choice==1:
   
    # create a sequence of words to choose from
    WORDS = ("python", "jumble", "easy", "difficult", "answer",
             "xylophone","rain","intelligent","celcius","inferno"
             )


    print(
    """
               Welcome to Jumble Me Up!
    
       Unscramble the letters to make a word.
    (Press the enter key at the prompt to quit.)
    """
    )


    play=input("Do you want to play? (yes or no)")
    while play=="yes":
        # pick one word randomly from the sequence
        word = random.choice(WORDS)
        # create a variable to use later to see if the guess is correct
        correct = word

        # create a jumbled version of the word
        jumble =""
        while word:
            position = random.randrange(len(word))
            jumble += word[position]
            word = word[:position] + word[(position + 1):]

        print("The jumble is:", jumble)
        points=100
        guess = input("\nYour guess: ")
        while guess != correct and guess != "":
            print("Sorry, that's not it.")
            hint=input("Do you need a hint?")
            if hint=="yes":
                points=int(points)-10
                if correct=="python":
                    print("Its a snake...")
                elif correct=="jumble":
                    print("Rhymes with rumble")
                elif correct== "easy":
                    print("This one is so simple!")
                elif correct=="difficult":
                    print("This is a hard one... its very ________________")
                elif correct=="answer":
                    print("You cant find it? the _________ is ___________")
                elif correct=="xylophone":
                    print("It is a toy...")
                elif correct=="rain":
                    print("It is a season...")
                elif correct=="intelligent":
                    print("Elbert Einstein was very ________ personality")
                elif correct=="celcius":
                    print("we measure temperature in ______")
                elif correct=="inferno":
                    print("It means fire and starts from i")
                print("Thanks for taking the hint...")
            guess = input("Your guess: ")

        if guess == correct:
            print("That's it!  You guessed it!\n")
            print("Your score is: "+str(points))
            play=input("Do you want to play again? (yes or no)")
        elif guess== "":
            print("You failed...")
            play=input("Do you want to play again? (yes or no)")


    print("Thanks for playing.")

    input("\n\nPress the enter key to exit.")

elif choice==2:
    words = [
      'apple',
      'banana',
      'orange',
      'coconut',
      'strawberry',
      'lime', 
      'grapefruit',
      'lemon',
      'mango',
      'blueberry',
      'melon'
    ]

    def clear():
      if os.name == 'nt':
        os.system('cls')
      else:
        os.system('clear')


    def draw(bad_guesses, good_guesses, secret_word):
      clear()

      print('Strikes: {}/7'.format(len(bad_guesses)))
      print('')

      for letter in bad_guesses:
        print(letter, end='')
      print('\n\n')

      for letter in secret_word:
        if letter in good_guesses:
          print(letter, end='')
        else:
          print('_', end='')

      print('')


    def get_guesses(bad_guesses, good_guesses):
      while True:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1:
          print("You can only guess a single letter!")
        elif guess in bad_guesses or guess in good_guesses:
            print("You've already guess that letter!")
        elif not guess.isalpha():
          print("You can only guess letters!")
        else:
          return guess

    def play(done):
      clear()
      secret_word = random.choice(words)
      bad_guesses = []
      good_guesses = []

      while True:
        draw(bad_guesses, good_guesses, secret_word)
        guess = get_guesses(bad_guesses, good_guesses)

        if guess in secret_word:
          good_guesses.append(guess)
          found = True
          for letter in secret_word:
            if letter not in good_guesses:
              found = False
    
          if found:
            print("You win!")
            print("The secret word was {}".format(secret_word))
            done = True

        else:
          bad_guesses.append(guess)
          if len(bad_guesses) == 7:
            draw(bad_guesses, good_guesses, secret_word)
            print("You lost!")
            print("The secret word was {}".format(secret_word))
            done = True

        if done:
          play_again = input("Play again? Y/n ").lower()
          if play_again != 'n':
            return play(done=False)
          else:
            sys.exit()


    def welcome():
      start = input("Press enter/return to start or Q to quit ").lower()
      if start == 'q':
        print("Bye!")
        sys.exit()
      else:
        return True

    print(       """
                   GUESS IF YOU CAN!
    
           Guess the letter of the words related
                    with fruit...
         (guess the letters using lowercase only)
        """
    )

    done = False

    while True:
      clear()
      welcome()
      play(done)
