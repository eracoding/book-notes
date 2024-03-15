import torch
import torchvision
from time import time

print(torch.version.__version__)

def print_time(a, b):
    start_time = time()
    print('a+b=', a + b)
    end_time = time()
    print('execution time is ', end_time - start_time)

a = torch.ones(3, 3)
print('a=', a)
b = torch.ones(3, 3)
print('b=', b)

print_time(a, b)

a = a.to('cuda')
b = b.to('cuda')

print_time(a, b)
