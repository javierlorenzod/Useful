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

# Debugging input tensor to network

One useful way of looking directly to the input data to the network is by using [`torchvision.utils.make_grid`](https://pytorch.org/docs/stable/torchvision/utils.html#torchvision.utils.make_grid). It returns a tensor which can be visualized as an standard image. You have to pass the input tensor with shape [B x C x H x W] where B is Batch size, C in the number of Channels, H is the Height of input image and W is the Width. Here is an example (from the notebook linked in documentation):
```python
import torch
import matplotlib.pyplot as plt
from torchvision.utils import make_grid

def show(img):
    npimg = img.numpy()
    plt.imshow(np.transpose(npimg, (1,2,0)), interpolation='nearest')

B = 16  # Always multiples of 2 (I do not know exactly the reason)
C = 3   # Usually, images depth is 3 --> RGB channels (Red, Green and Blue, respectively)
H = 224 # 224 is the input height for ResNet models in torchvision.models
W = 224 # same as height, but it could be different. In Convolutional Neural Networks, the input is usually squared in order to simplify calculus.

input_tensor = torch.randn(B, C, H, W)
show(make_grid(input_tensor, padding=100, normalize=True))
plt.show()
```
