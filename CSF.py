import os
import sys
import build_target as bt
import thompson as ts
import run_afl_test as afl
import inputAlgorithm as inputAlgo



def buildTarget():
    bt.select_target()
    bt.prepare_fuzz_environment()
    bt.build_target()

# init option
options = {}
options["nothing"] = ts.Option()
options["ASAN"] = ts.Option()


# build target
# buildTarget()

# test default
options["nothing"].path = './fuzzing_target/install_nothing'
options["ASAN"].path = './fuzzing_target/install_asan'

# initialize variable

for v in range(len(sys.argv)):
    if v == 1 :
        timeTotal = int(sys.argv[v])

    elif v == 2 :
        threshold_init = float(sys.argv[v])

# set path
totalCrash_path = './result_total/crash_total/'
totalInput_path = './result_total/input_total/'

# initilize variable
edgeFound_prior = 0.0
threshold_new = threshold_init

# need to be changed later
time_cur = 300
run_option ='-m none'
pgm_option = '-D -j -c -r -s -w'

#for value in options.values():
#    print(value.S)

checkThreshold_result = []
checkSelectedOption = []

while timeTotal > 0:
    # select option
    selectedOption = ts.selectOption(options)
    
    checkSelectedOption.append(selectedOption)

    # run afl_fuzz with selected option
    edgeFound_new, newCrash_path, newInput_path = afl.fuzz("/bin/tiffinfo",totalInput_path,'./out', time_cur,options[selectedOption], run_option, pgm_option)

    # evalute this fuzzer
    if edgeFound_new - edgeFound_prior >= threshold_new:
        ts.updateOptionPosterior(options[selectedOption], 1)
        threshold_new = threshold_new + threshold_init
    else:
        ts.updateOptionPosterior(options[selectedOption], 0)
        threshold_new = threshold_new/2

    checkThreshold_result.append(threshold_new)
    if edgeFound_new > edgeFound_prior:
        edgeFound_prior = edgeFound_new
    
    inputAlgo.updateResult(totalCrash_path, newCrash_path, totalInput_path, newInput_path, options[selectedOption].path + "/bin/tiffinfo", pgm_option)

    timeTotal = timeTotal - time_cur


print(checkSelectedOption)
print(checkThreshold_result)
print("nothing result: "+str(options["nothing"].S) +" "+str(options["nothing"].F))
print("ASAN result: "+str(options["ASAN"].S) +" "+str(options["ASAN"].F))
