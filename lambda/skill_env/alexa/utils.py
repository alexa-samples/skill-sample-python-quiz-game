import random
import six
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_core.utils import is_request_type

from . import data_roboti as data

_TRUE_FACTS_ONLY = [fact['True'] for fact in data.FACTS]
_TRUTH_VALUES = ['True', 'False']


def get_random_true_fact():
    return random.choice(_TRUE_FACTS_ONLY)


def get_intermediate_score(score, counter):
    return data.SCORE_STATUS.format(score, counter)


def get_final_score(score, counter):
    return data.FINAL_SCORE.format(
        score, counter, data.FINAL_GREETINGS[score > counter/2],
    )
