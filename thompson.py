import numpy as np

class Option():
    def __init__(self):
        self.S = 1 # success count
        self.F = 1 # Fail count
        self.prob = 0.0 # success probability
        self.path = ''


# options is dictionary type
def selectOption(options):
    maxProb = 0.0
    for value in options.values():
        value.prob = np.random.beta(value.S, value.F, size = 1)
        print(value.prob)
    max_prob_option = max(options, key=lambda key: options[key].prob) 
    return max_prob_option

def updateOptionPosterior(option,criteria):
    if criteria == 1:
        option.S = option.S + 1
    else:
        option.F = option.F + 1
            

    

        


#    def test(options):
#       for option in options:
#          print(option.prob)



