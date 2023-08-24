import numpy as np
import logging

class Option():
    def __init__(self):
        self.S = 1 # success count
        self.F = 1 # Fail count
        self.prob = 0.0 # success probability
        self.path = ''


# options is dictionary type
def selectOption(options):
    maxProb = 0.0
    logging.debug('First line is nothing. Second line is ASAN.')

    # calcuate option probability
    for value in options.values():
        value.prob = np.random.beta(value.S, value.F, size = 1)
        logging.debug('Success: ' + str(value.S) + ', Fail: '+str(value.F)+ ', Prob: '+str(value.prob))

    max_prob_option = max(options, key=lambda key: options[key].prob) 

    logging.debug('selected option: ' +str(max_prob_option))

    return max_prob_option


# update the number of successes or failures of an option
def updateOptionPosterior(option,criteria):
    if criteria == 1:
        option.S = option.S + 1
        logging.debug('Update option function - Success')
    else:
        option.F = option.F + 1
        logging.debug('Update option function - Fail')
            
