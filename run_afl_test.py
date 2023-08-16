import os

# run afl++
#  - fuzz function input type is string.
"""
def fuzz(pgm, input_corpus_path, output_corpus_path, time, run_option, pgm_option):
    fuzzing_command = "afl_fuzz" + run_option + "-i" + input_corpus + "-o" + output_corpus_path + "-t"+ time +  "--" + pgm + pgm_option +"@@"
    os.system(fuzzing_command)

    resultInfo = fuzzerResultInfo(output_corpus_path)



    edge_new = int(resultInfo["edge_new")
    edge_total = int(resultInfo["total_edges"])
    Crash_new_path =
    input_corpus_new_path =

    edgeFound_new = edge_new/edge_total * 100
    # edge

    return edgeFound_new, crash_new_path, input_corpus_new_path


def fuzzerResultInfo(output_corpus_path):
    result_info ={}
    # now location
    fuzzerResultPath = os.popen("pwd")+outpus_corpus_path+"/default/"

    statsFile = open(fuzzerResultPath,"fuzzer_stats",'r')

    for line in statsFile.lines():
        if "edges_found" in line:
            result_info["edge_new"]  = line.split(":")[1]

        else if "total_edges" in line:
            result_info["edge_total"] = line.split(":")[1]

    return result_info
"""




os.chdir("./target/fuzzing_target/")

os.system("afl-fuzz -m none -i ./tiff-4.0.4/test/images/ -o ./out3/ -V 10  -s 123 -- ./install_asan/bin/tiffinfo -D -j -c -r -s -w @@")

# now location
fuzzerResultPath = "./out3/default/"

statsFile = open(fuzzerResultPath+"fuzzer_stats",'r')

for line in statsFile:
    if "edges_found" in line:
        print("*****"+line)
        print(line.split(":"))
    elif "total_edges" in line:
        print("*****" + line)
        print(line.split(":"))

