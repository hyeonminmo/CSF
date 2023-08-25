import os
import logging

def setTarget():
    path ="./bloaty_FuzzBench/setBuild.sh"
    os.chdir("./target")
    os.system(path)

    logging.debug("download target and set build option")

#build option select
def prepare_fuzz_environment():
    os.environ["CC"] = "afl-clang-lto"
    os.environ["CXX"] = "afl-clang-lto++"

    logging.debug("prepare fuzz environment")

def build_target():
    os.chdir("../fuzzing_target")
    os.system("./build_nothing.sh")

    logging.debug("build nothing option")

    os.environ["AFL_USE_ASAN"] =  '1'
    os.system("./build_asan.sh")

    logging.debug("build asan option")

#    delete environment varialbe

    del os.environ["AFL_USE_ASAN"]
    logging.debug("unset asan option")

    os.chdir("../")

