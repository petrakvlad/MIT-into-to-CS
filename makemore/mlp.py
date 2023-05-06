import torch
import matplotlib.pyplot as plt
import torch.nn.functional as F


words = open("/mnt/c/Users/Vlad/Documents/GitHub/someproj/makemore/names.txt", "r").read().splitlines()
print(len(words))

#mapping of characters
chars = sorted(set(''.join(words)))
stoi = {s:i+1 for i, s in enumerate(chars)}
stoi['.'] = 0
itos = {i:s for s,i in stoi.items()}

# create a dataset
block_size = 3
X, Y = [],[]

for i in words[: 1]:
    # print(i)
    content = [0] * block_size

    for ch in i + '.':
        X.append(content)
        iy = stoi[ch]
        Y.append(iy)
        # print(''.join(itos[n] for n in content), "-->", itos[iy])
        content = content[1:] + [iy]


X = torch.tensor(X)
Y = torch.tensor(Y)

print(X)
print("----------------")

C = torch.randn((25,2))
emb = C[X]
print(emb)
print("----------------")
print(emb[0,2])
