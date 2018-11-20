import random
# import six
# from ask_sdk_core.handler_input import HandlerInput
# from ask_sdk_core.utils import is_request_type

from . import data_roboti as data

_TRUE_FACTS_ONLY = data.FACTS + [fact['True'] for fact in data.TRUE_OR_FALSE]
_TRUTH_VALUES = ['True', 'False']


def get_random_true_fact():
    return random.choice(data.FACTS_SPEECHONS).format(
        random.choice(_TRUE_FACTS_ONLY),
    )


def get_intermediate_score(score, counter):
    return data.SCORE_STATUS.format(score, counter)


def get_final_score(score, counter):
    return data.FINAL_SCORE.format(
        score, counter, data.FINAL_GREETINGS[score > counter/2],
    )


def get_questions_for_new_quiz():
    questions = []
    stm_nos = random.sample(list(range(len(data.TRUE_OR_FALSE))),
                            k=data.MAX_QUESTIONS)

    for x in stm_nos:
        truth_value = random.choice(_TRUTH_VALUES)
        questions.append({'truth_value': truth_value, 'stm_no': x})

    return questions


def get_question_text(q_data):
    return data.TRUE_OR_FALSE[q_data['stm_no']][q_data['truth_value']]


def check_question_answer(ans, q_data):
    fact_idx = q_data['stm_no']
    if ans.lower() == q_data['truth_value'].lower():
        # The answer is correct
        # TODO
        pass


def get_speechcon(correct):
    if correct:
        return random.choice(data.CORRECT_SPEECHCONS)
    else:
        return random.choice(data.WRONG_SPEECHCONS)


def get_question_feedback(correct, fact_idx):
    pass