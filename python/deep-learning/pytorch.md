# PyTorch Notes

- Get Properties of CUDA GPU with GPUID `n`:
```python
import torch.cuda as cdtrch
n = 0
gpu_properties = cdtrch.get_device_properties(n)
print(f"GPU Name: {gpu_properties.name}\n Total memory (Bytes): {gpu_properties.total_memory}")
```
