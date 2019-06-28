# PyTorch Notes

- Get Properties of CUDA GPU with GPUID `n`:
```python
import torch.cuda as cdtrch
n = 0
gpu_properties = cdtrch.get_device_properties(n)
print(f"GPU Name: {gpu_properties.name}\n Total memory (Bytes): {gpu_properties.total_memory}")
```
Image Backend
=============
Torchvision currently supports the following image backends:

* `Pillow`_ (default)

* `Pillow-SIMD`_ - a **much faster** drop-in replacement for Pillow with SIMD. If installed will be used as the default.

* `accimage`_ - if installed can be activated by calling :code:`torchvision.set_image_backend('accimage')`

.. _Pillow : https://python-pillow.org/
.. _Pillow-SIMD : https://github.com/uploadcare/pillow-simd
.. _accimage: https://github.com/pytorch/accimage
