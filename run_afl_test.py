import os
import logging

# run afl++
#  - fuzz function input type is string.

def fuzz(pgm, input_corpus_path, output_path, time, run_option, pgm_option):
    fuzzing_command = "afl-fuzz " + run_option + " -i " + input_corpus_path + " -o " + output_path + " -V "+ str(time) +  " -- " + pgm +" "+ pgm_option +" @@"
    os.system(fuzzing_command)

    logging.debug('run afl fuzzing')

    resultInfo ={}
    resultInfo = fuzzerResultInfo(output_path)
    
    edge_new = int(resultInfo["edge_new"])
    edge_total = int(resultInfo["edges_total"])
    crash_new_path = resultInfo["path"]+"crashes"
    input_corpus_new_path = resultInfo["path"]+"queue"

    edgeFound_new = float(edge_new)/edge_total * 100

    logging.debug('calculate edgeFound_new percent :' + str(edgeFound_new))


    return edgeFound_new, crash_new_path, input_corpus_new_path


def fuzzerResultInfo(output_corpus_path):
    result_info ={}
    # now location
    result_info["path"] = output_corpus_path+"/default/"    

    statsFile = open(result_info["path"]+"fuzzer_stats",'r')

    for line in statsFile:
        if "edges_found" in line:
            result_info["edge_new"]  = int(line.split(":")[1])

        elif "total_edges" in line:
            result_info["edges_total"] = int(line.split(":")[1])

    logging.debug('To obtain the fuzzing result information')

    return result_info
