import os

# input : target project name

def select_target():
    path ="./setBuild.sh"
    os.chdir("./target/")
    os.system(path)

#build option select
def prepare_fuzz_environment():
    os.environ["CC"] = "afl-clang-lto"
    os.environ["CXX"] = "afl-clang-lto++"

def build_target():
    os.chdir("../fuzzing_target")
#    delete environment varialbe
#    del os.environ["AFL_USE_ASAN"])
    os.system("./build_nothing.sh")
    os.environ["AFL_USE_ASAN"] =  '1'
    os.system("./build_asan.sh")
    del os.environ["AFL_USE_ASAN"]
    os.chdir("../")

# clone libtiff project 
#select_target()

#prepare_fuzz_environment()

# run build_option
#build_target()

#print(os.environ)
