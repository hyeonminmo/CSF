cd fuzzing_tiff
cd tiff-4.0.4
./configure --prefix="$HOME/CSF_test/target/fuzzing_tiff/install/" --disable-shared
make -j4
make install
