import os
import glob
import shutil
import logging

# input: pgm, inputCorpus_new, inputCorpus_global, crash_new, crash_global, pgm_option, input_unique
# no return. Because this function is only update crash and input file and delete duplication seed input
# 



def updateResult(crashTotal,crashNew):

#    inputTotal_list = os.listdir(inputTotal)
#    inputTotal_count = len(inputTotal_list)
#    logging.debug('Befor Number of inputTotal : ' + str(inputTotal_count))


    # copy new input corpus and crash to total input and crash
    crashCommand = "find  "+crashNew+" -type f -print0 | xargs -0 -I {} cp -b {} "+ crashTotal
    os.system(crashCommand)
