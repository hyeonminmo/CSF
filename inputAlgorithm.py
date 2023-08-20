import os
import glob
import shutil
import logging

# input: pgm, inputCorpus_new, inputCorpus_global, crash_new, crash_global, pgm_option, input_unique
# no return. Because this function is only update crash and input file and delete duplication seed input
# 



def updateResult(crashTotal,crashNew, inputTotal, inputNew):

    # copy new input corpus and crash to total input and crash
#    shutil.copy2(crashNew+"/*",crashTotal)
#    shutil.copy2(inputNew+"/*",inputTotal)
    crashCommand = "cp -b "+crashNew+"/* " + crashTotal
    os.system(crashCommand)
    logging.debug('copy new crash file to total crash folder')
    inputCommand = "cp -b "+ inputNew+"/* " + inputTotal
    os.system(inputCommand)
    logging.debug('copy new input file to total input folder')

    # delete prior result
    shutil.rmtree("./out")
    logging.debug('remove out folder')
