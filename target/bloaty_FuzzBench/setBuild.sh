cd ../..
mkdir fuzzing_target
cd fuzzing_target/
# download target project
git clone https://github.com/google/bloaty.git
# set target project version
cd bloaty
git checkout 52948c107c8f81045e7f9223ec02706b19cfa882
cd ..


touch build_nothing.sh
chmod 755 build_nothing.sh

echo "cd bloaty\ncmake -G Ninja -DBUILD_TESTING=false -DCMAKE_INSTALL_PREFIX=../install_nothing .\nninja -j$(nproc)\n ninja install" > build_nothing.sh


touch build_asan.sh
chmod 755 build_asan.sh

echo "cd bloaty\ncmake -G Ninja -DBUILD_TESTING=false -DCMAKE_INSTALL_PREFIX=../install_asan .\nninja -j$(nproc)\n ninja install" > build_asan.sh



