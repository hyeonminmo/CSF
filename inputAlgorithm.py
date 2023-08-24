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
#    logging.debug('copy new crash file to total crash folder')
#    inputCommand = "find  "+inputNew+" -type f -print0 | xargs -0 -I {} cp -b {} "+ inputTotal
#    os.system(inputCommand)

#    shutil.rmtree(inputTotal)
#    os.mkdir(inputTotal)
     
        
#    file_list = os.listdir(inputNew)
#    file_count = len(file_list)
#    logging.debug('Nubmer of inputs : ' +str(file_count))

#    file_list.remove('.state')

#    for f in file_list:
#        shutil.copy(os.path.join(inputNew,f),inputTotal)

#    logging.debug('copy new input file to total input folder')
#    inputTotal_list = os.listdir(inputTotal)
#    inputTotal_count = len(inputTotal_list)
#    logging.debug('After Number of inputTotal : ' + str(inputTotal_count))


    # delete prior result
#    shutil.rmtree("./out")
#    logging.debug('remove out folder')
