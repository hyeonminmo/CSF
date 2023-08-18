import os
import glob
import shutil

# input: pgm, inputCorpus_new, inputCorpus_global, crash_new, crash_global, pgm_option, input_unique
# no return. Because this function is only update crash and input file and delete duplication seed input
# 



def updateResult(crashTotal,crashNew, inputTotal, inputNew,pgm, pgm_option):

    # copy new input corpus and crash to total input and crash
    crashCommand = "cp "+crashNew+"/* " + crashTotal
    os.system(crashCommand)
    inputCommand = "cp "+ inputNew+"/* " + inputTotal
    os.system(inputCommand)

    # delete duplication seed input
    os.system("afl-cmin -i "+inputTotal+" -o ./inputsUnique -- " + pgm +" "+ pgm_option + "@@")

    os.system("rm -rf "+ inputTotal+"/id*")
    os.system("cp ./inputsUnique/* " + inputTotal)
   


    # delete prior result
    try:  
        shutil.rmtree("./out")
    except OSError as e:
        print("Error: remove ./out: %s" % (e.strerror))
    try:
        shutil.rmtree("./inputsUnique")
    except OSError as e:
        print("Error: remove ./inputsUnique: %s" % (e.strerror))




