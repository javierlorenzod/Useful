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
