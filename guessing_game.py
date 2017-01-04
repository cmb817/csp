import random
def guess_game(options=['Amy', 'Bill', 'Cathy']):
    '''Gets user input until what?
    
    options is a list of what types?
    returns what?
    '''
    
    # Explain this line of code
    answer = random.choice(options) 
    
    ###
    # Summarize the following section of code here
    ###
    option_list = ''
    for option in options[:-1]: # Why leave out the last element?
        option_list += option + ', '
    option_list += 'or ' + options[-1] # Explain this line here
    
    ###
    # Summarize the following section of code here
    ###
    
    # What is the purpose of the next three lines?
    guesses = 1 
    print('Guess which one is the secret I\'ve picked: ' + option_list)
    print('Guess: ')
    guess = raw_input()
    
    # Summarize the purpose of the loop
    while guess != answer:
        print('Guess again: ')
        guess = raw_input()
        guesses += 1
    
    # Explain the next two
    print('You guessed in ' + str(guesses) + ' guesses!') 
    return guesses
