# PyTorch tests

In this file I will summarize several tests carried out during my research. It will allow me to avoid **repeating** them in the future

## Test PT_1

[`ConsensusModule`](https://github.com/yjxiong/tsn-pytorch/blob/master/ops/basic_ops.py) used in TSM repository is only a mean of the input tensor in a specific dimension. This test is to assure that both operations obtain the same gradients by calling backward

```python
import torch
from models.modules import ConsensusModule  # Here this is the hardcoded path of ConsensusModule in one project. Consider changing
x1 = torch.ones(2, 2, requires_grad=True)
x2 = torch.ones(2, 2, requires_grad=True)
y1 = x1 + 2
y2 = x2 + 2
z1 = y1 * y1 * 3
z2 = y2 * y2 * 3
consensus = ConsensusModule('avg')
o1 = torch.mean(z1)
o2 = consensus(z2)
print(x1.grad)
print(x2.grad)
```
Both are the same.

## Test PT_2: Reproducibility

### Test PT_2_1: Dropout layer

I tried this with the following environment:
- pytorch-lightning 1.1.4
- python 3.8.5
- pytorch 1.7.1 (py3.8_cuda11.0.221_cudnn8.0.5_0)
- Operating System: Ubuntu 18.04.5 LTS
- Kernel: Linux 4.15.0-135-generic
- Architecture: x86-64
- Driver Version: 450.102.04
- CUDA Version: 11.0

The first part creates a vector b and saves it in a temporal file.

```python
import torch
import torch.nn as nn
from pytorch_lightning import seed_everything
seed_everything(47)
m = nn.Dropout(p=0.5).to("cuda")
a = torch.rand(10).to("cuda")
b = m(a)
torch.save(b, "b_previous_borrar")
```

After that, the python console is reinitialized and the same code is executed. After loading the previous vector b, both are compared and the result is that **both contains the same data**

```python
import torch
import torch.nn as nn
from pytorch_lightning import seed_everything
seed_everything(47)
m = nn.Dropout(p=0.5).to("cuda")
a = torch.rand(10).to("cuda")
b = m(a)
b_prev = torch.load("b_previous_borrar")
b.equal(b_prev)
```
