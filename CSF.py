import os
import sys
import logging
import build_target as bt
import thompson as ts
import run_afl_test as afl
import inputAlgorithm as inputAlgo

logging.basicConfig(level=logging.DEBUG, filename='processCSF.log', filemode='w',format='%(filename)s -  %(funcName)s %(levelname)s - %(message)s')

def buildTarget():
    bt.setTarget()
    bt.prepare_fuzz_environment()
    bt.build_target()
    logging.debug('complete build target')

# init option
options = {}
options["nothing"] = ts.Option()
options["ASAN"] = ts.Option()


# build target
#buildTarget()

# test default
options["nothing"].path = './fuzzing_target/install_nothing'
options["ASAN"].path = './fuzzing_target/install_asan'

# initialize variable
for v in range(len(sys.argv)):
    if v == 1 :
        timeTotal = int(sys.argv[v])
        logging.debug('set total time : ' + str(timeTotal))

    elif v == 2 :
        threshold_init = float(sys.argv[v])
        logging.debug('set threshold_init : ' + str(threshold_init))

# set path
totalCrash_path = './result/crash_total/'
seedInput_path = './result/seedInput'

# initilize variable
edgeFound_prior = 0.0
threshold_new = threshold_init

# need to be changed later
time_cur = 300
if timeTotal < time_cur:
    time_cur = timeTotal

run_option ='-m none -t 1000+'
pgm_option = ''
targetPgm = '/bin/bloaty'

exec_count = 1

while timeTotal > 0:
    # select option
    selectedOption = ts.selectOption(options)  
    pgm = options[selectedOption].path + targetPgm

    # run afl_fuzz with selected option
    if exec_count == 1:
        edgeFound_new, newCrash_path = afl.fuzz(pgm, seedInput_path, './out', time_cur, run_option, pgm_option)
    else:
        edgeFound_new, newCrash_path  = afl.fuzz(pgm, '-', './out', time_cur, run_option, pgm_option)

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
    
    inputAlgo.updateResult(totalCrash_path, newCrash_path)
    exec_count+=1

    timeTotal = timeTotal - time_cur

for key, value in options.items():
    logging.debug('Result | option : ' + str(key) + ' success : ' + str(value.S) + ' fail : ' + str(value.F))


print("nothing result: "+str(options["nothing"].S) +" "+str(options["nothing"].F))
print("ASAN result: "+str(options["ASAN"].S) +" "+str(options["ASAN"].F))
