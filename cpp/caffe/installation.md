## Fix hdf5 problem
__**Note**__: based on the [section](https://gist.github.com/wangruohui/679b05fcd1466bb0937f#fix-hdf5-naming-problem) of this caffe installation gist.

After configuring **Makefile.config** file and beginning compilation of caffe using `make` appears the following error:
```
In file included from src/caffe/solver.cpp:8:0:
./include/caffe/util/hdf5.hpp:6:18: fatal error: hdf5.h: No such file or directory
compilation terminated.
```
[HDF5](https://support.hdfgroup.org/HDF5/whatishdf5.html) is a unique technology suite that makes possible the management of extremely large and complex data collections.

I basically copy the process to fix that issue, because it is perfectly explained (it is used oriented to Ubuntu 15.10, but it works with Ubuntu 16.04 so I changed only that aspect) :

This error is because of the change of default path and name of `hdf5` head files and libraries in Ubuntu 16.04. To solve this problem, we can simply modify `Makefile` files. 

Append `/usr/include/hdf5/serial/` to `INCLUDE_DIRS` at line 85 in `Makefile.config`.
```
--- INCLUDE_DIRS := $(PYTHON_INCLUDE) /usr/local/include
+++ INCLUDE_DIRS := $(PYTHON_INCLUDE) /usr/local/include /usr/include/hdf5/serial/
```

Modify `hdf5_hl` and `hdf5` to `hdf5_serial_hl` and `hdf5_serial` at line 173 in `Makefile`
```
--- LIBRARIES += glog gflags protobuf boost_system boost_filesystem m hdf5_hl hdf5
+++ LIBRARIES += glog gflags protobuf boost_system boost_filesystem m hdf5_serial_hl hdf5_serial
```
## CUDA 9 : Unsupported gpu architecture 'compute_20'
__**Note**__: based on the [issue](https://github.com/kaldi-asr/kaldi/issues/1918) in kaldi repository.

In CUDA 9, Fermi (aka 2.x) architecture is removed instead of deprecated as in CUDA 8. If the **Makefile.config** is not recent enough, maybe it will show that error:
```
nvcc fatal   : Unsupported gpu architecture 'compute_20'
```
If that is the case, the way of fixing it consist in deleting the following lines in **Makefile.config** :
```
-gencode arch=compute_20,code=sm_20 \
-gencode arch=compute_20,code=sm_21 \
```
## OpenCV 3 error
If you have an error like the following:
```
src/caffe/layers/resample_layer.cu:10:31: fatal error: opencv2/gpu/gpu.hpp: No such file or directory
```
Do not worry, there is a fix to it!

In recent versions of OpenCV (>3)
