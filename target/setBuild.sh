mkdir fuzzing_target
cd fuzzing_target/
wget https://download.osgeo.org/libtiff/tiff-4.0.4.tar.gz
tar -xzvf tiff-4.0.4.tar.gz

touch build_nothing.sh
chmod 755 build_nothing.sh

echo "cd tiff-4.0.4\nmake clean\n./configure --prefix=\"$HOME/CSF_test/target/fuzzing_target/install_nothing/\" --disable-shared \nmake -j4\nmake install" > build_nothing.sh


touch build_asan.sh
chmod 755 build_asan.sh

echo "cd tiff-4.0.4\nmake clean\n./configure --prefix=\"$HOME/CSF_test/target/fuzzing_target/install_asan/\" --disable-shared \nmake -j4\nmake install" > build_asan.sh



