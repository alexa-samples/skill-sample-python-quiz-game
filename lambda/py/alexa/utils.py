import random
# import six
# from ask_sdk_core.handler_input import HandlerInput
# from ask_sdk_core.utils import is_request_type

from . import data_roboti as data

_TRUE_FACTS_ONLY = [fact['True'] for fact in data.TRUE_OR_FALSE]
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
    return random.choice(data.QUESTION_STARTS).format(
        data.TRUE_OR_FALSE[q_data['stm_no']][q_data['truth_value']]
    ).strip('.')


def correct_answer(ans, q_data):
    return (ans.lower() in ['yes', 'true'] and q_data['truth_value'].lower() == 'true') \
        or (ans.lower() in ['no', 'false'] and q_data['truth_value'].lower() == 'false')


def get_question_feedback(correct, fact_idx, truth_value):
    return data.QUESTION_FEEDBACK_TEMPLATE[truth_value][correct].format(
        random.choice(data.FEEDBACK_SPEECHONS[correct]),
        data.TRUE_OR_FALSE[fact_idx]['True'],
    )


def check_answer_and_get_new_question(q_data, ans, attr, last_one):
    correct = correct_answer(ans, q_data)

    attr['counter'] += 1
    if correct:
        attr['score'] += 1
    feedback = get_question_feedback(
        correct, q_data['stm_no'], q_data['truth_value'],
    )

    if last_one:
        score = get_final_score(attr['score'], attr['counter'])

        return '{}. {}.'.format(feedback, score), None

    score = get_intermediate_score(attr['score'], attr['counter'])
    next_q_data = attr['questions'][0]

    attr['last_question'] = next_q_data
    attr['questions'] = attr['questions'][1:]

    q = get_question_text(next_q_data)

    return '{}. {}. The next question is: {}?'.format(feedback, score, q), \
           '{}?'.format(q)
