questions = ("Are you good?",
             "You ok?",
             "Are you fine?",
             'You good?',
             'What is up?')

options = (('a. Im good', 'b. Im ok', 'c,. Fine', 'd. Happu'),
           ('a. i dont know', 'b. not that tired', 'c. keeping up', 'd. on time'),
           ('a. yep', 'b. yes i am', 'c. as usual', 'd. Hmm'),
           ('a. yeah', 'b.  yeah, whats up?', 'c. good good...', 'd. i know that trick'),
           ('a. Yeah whats up?', 'b. NIce', 'c.', 'd. yo whats up'))

answers = ("", '', '', '', '')

guesses = []
score = 0
question_num = 0
for question in questions:
    print('----------------')
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input('Enter (A, B, C, D): ').upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print(
            'Correct'
        )
    else:
        print('INcorrect')
        print(f"{answers[question_num]} is the correct answer")
    question_num +=1