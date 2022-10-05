import torch
import torch.nn as nn
print(torch.__version__)

torch.manual_seed(0)
#making the random values constrained by setting the key 0

net_made_of_seq = nn.Sequential(
    nn.Linear(1000,100),
    nn.ReLU(),
    nn.Dropout(0.3),
    nn.Linear(100,10)
)

print(net_made_of_seq)
#output: Sequential(
#  (0): Linear(in_features=1000, out_features=100, bias=True)
#  (1): ReLU()
#  (2): Dropout(p=0.3, inplace=False)
#  (3): Linear(in_features=100, out_features=10, bias=True)
#)

print(type(net_made_of_seq))
#output: <class 'torch.nn.modules.container.Sequential'> 
