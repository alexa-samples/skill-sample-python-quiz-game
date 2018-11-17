TRUE_OR_FALSE = [
    {'True': 'fact 1 true', 'False': 'fact 1 false'},
    {'True': 'fact 2 true', 'False': 'fact 2 false'},
    # TODO: ADD MORE
]

FACTS = [
    # TODO: ADD STAND-ALONE FACTS
]

SKILL_TITLE = 'Eco Minds'

CORRECT_SPEECHCONS = ['Booya', 'All righty', 'Bam', 'Bazinga', 'Bingo',
                      'Boom', 'Bravo', 'Cha Ching', 'Cheers', 'Dynomite',
                      'Hip hip hooray', 'Hurrah', 'Hurray', 'Huzzah',
                      'Oh dear.  Just kidding.  Hurray', 'Kaboom', 'Kaching',
                      'Oh snap', 'Phew', 'Righto', 'Way to go', 'Well done',
                      'Whee', 'Woo hoo', 'Yay', 'Wowza', 'Yowsa']

WRONG_SPEECHCONS = ['Argh', 'Aw man', 'Blarg', 'Blast', 'Boo', 'Bummer',
                    'Darn', "D'oh", 'Dun dun dun', 'Eek', 'Honk', 'Le sigh',
                    'Mamma mia', 'Oh boy', 'Oh dear', 'Oof', 'Ouch', 'Ruh roh',
                    'Shucks', 'Uh oh', 'Wah wah', 'Whoops a daisy', 'Yikes']

QUESTION_STARTS = ['Is it true that {}?', 'Do you believe that {}?',
                   'Is it correct that {}?', 'Is the following fact genuine? {}'
                   'Is it accurate that {}?', 'Is it correct that {}?',
                   'Is it right that {}?']


MAX_QUESTIONS = 5

WELCOME_MESSAGE = ('Heya! Welcome to the Eco Minds quiz game! You can ask me '
                   'for facts about ecology or you can start a new quiz. What '
                   'would you like to do?')

QUIZ_START_MESSAGE = ("Ok, let's get it started then! I will start stating {} "
                      'facts, to which you will have to reply with True of '
                      'False. The first question is: {}')

SCORE_STATUS = 'Your score is {} out of {}.'

FINAL_SCORE = 'All done! Your final score is {} out of {}! {}'

FINAL_GREETINGS = {
    True: 'Congratulations!',
    False: 'Better luck next time!'
}

HELP_MESSAGE = ('I know lots of things about ecology. You can ask me for facts '
                'related to this or you can start a quiz.')

FALLBACK_MESSAGE = 'Sorry, I cannot help you with that. {}'.format(HELP_MESSAGE)

EXCEPTION_MESSAGE = 'Sorry. An error occurred. Please try again!'

EXIT_MESSAGE = 'Bye! Hope to see you again soon!'

FACT_TEMPLATE = '{}. {}.'

CORRECT_ANSWER = "That's correct!"

INCORRECT_ANSWER = 'Actually,'

ANSWER_TRUE_TEMPLATE = "{}! {} {}."

ANSWER_FALSE_TEMPLATE = "{}! {} {}. {}"
