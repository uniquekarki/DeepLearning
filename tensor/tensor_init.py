import torch

my_tensor = torch.tensor([[1,2,3],[4,5,6]], dtype = torch.float32, device = 'cpu', requires_grad = True)

print(my_tensor)