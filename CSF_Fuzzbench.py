import os
import sys
import logging
import build_target as bt
import thompson as ts
import run_afl_test as afl
import inputAlgorithm as inputAlgo

logging.basicConfig(level=logging.DEBUG, filename='processCSF.log', filemode='w',format='%(filename)s -  %(funcName)s %(levelname)s - %(message)s')

# input_corpus : string path
# output_corpus : strng path
# target_binary : list string path?

def CSF_MAIN(input_corpus, output_corpus, target_binary):
    # init option
    options = {}
    options["nothing"] = ts.Option()
    options["ASAN"] = ts.Option()
    # test default
    options["nothing"].path = target_binary[0]
    options["ASAN"].path = target_binary[1]

    # initialize variable
    for v in range(len(sys.argv)):
        if v == 1 :
            timeTotal = int(sys.argv[v])
            logging.debug('set total time : ' + str(timeTotal))
        elif v == 2 :
            threshold_init = float(sys.argv[v])
            logging.debug('set threshold_init : ' + str(threshold_init))
    # set path
    totalCrash_path = './out/crash_total/'
    # initilize variable
    edgeFound_prior = 0.0
    threshold_new = threshold_init
    # need to be changed later
    time_cur = 300
    if timeTotal < time_cur:
        time_cur = timeTotal

    run_option ='-m none -t 1000+'
    pgm_option = '-D -j -c -r -s -w'

    exec_count = 1

    while timeTotal > 0:
        # select option
        selectedOption = ts.selectOption(options)
        pgm = options[selectedOption].path 
        # run afl_fuzz with selected option
         if exec_count == 1:
             edgeFound_new, newCrash_path = afl.fuzz(pgm, input_corpus, output_corpus, time_cur, run_option, pgm_option)
         else:
             edgeFound_new, newCrash_path  = afl.fuzz(pgm, '-', output_corpus, time_cur, run_option, pgm_option)
        logging.debug('Selected option: ' + selectedOption)
        logging.debug('Update before Success : ' + str(options[selectedOption].S) + ', Fail : '+str(options[selectedOption].F) + ', Threshold : ' + str(threshold_new))
        # evalute this fuzzer
        if edgeFound_new - edgeFound_prior >= threshold_new:
            ts.updateOptionPosterior(options[selectedOption], 1)
            threshold_new = threshold_new + threshold_init
        else:
            ts.updateOptionPosterior(options[selectedOption], 0)
            threshold_new = threshold_new/2
        logging.debug('Update after  Success : ' + str(options[selectedOption].S) + ', Fail : ' + str(options[selectedOption].F)+ ', Threshold : ' + str(threshold_new))
        if edgeFound_new > edgeFound_prior:
            edgeFound_prior = edgeFound_new
            logging.debug('The new edgeFound is only less than the previous edgeFound')
#        inputAlgo.updateResult(totalCrash_path, newCrash_path)
        timeTotal = timeTotal - time_cur
        for key, value in options.items():
            logging.debug('Result | option : ' + str(key) + ' success : ' + str(value.S) + ' fail : ' + str(value.F))
    


