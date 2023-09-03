import torch
import matplotlib.pyplot as plt
import torch.nn.functional as F


words = open("/mnt/c/Users/Vlad/Documents/GitHub/someproj/makemore/names.txt", "r").read().splitlines()
g = torch.Generator().manual_seed(2147483647)

#mapping of characters
chars = sorted(set(''.join(words)))
stoi = {s:i+1 for i, s in enumerate(chars)}
stoi['.'] = 0
itos = {i:s for s,i in stoi.items()}

# create a dataset
block_size = 4
X, Y = [],[]

for i in words:
    content = [0] * block_size

    for ch in i + '.':
        X.append(content)
        iy = stoi[ch]
        Y.append(iy)
        # print(''.join(itos[n] for n in content), "-->", itos[iy])
        content = content[1:] + [iy]

# make it tensor
X = torch.tensor(X)
Y = torch.tensor(Y)

#make random tensor
C = torch.randn((27,10), generator = g)

# now second layer of the NN

# random weights and biases for the first layer
W1 = torch.randn((40, 300), generator = g)
b1 = torch.randn(300, generator = g)

# random weights and biases for the second layer
W2 = torch.randn((300, 27), generator = g)
b2 = torch.randn(27, generator = g)


parameters = [C, W1, b1, W2, b2]
num_parameters = sum(p.nelement() for p in parameters)
print(num_parameters)

#make sure we have grads
for p in parameters:
    p.requires_grad = True


# forward pass
for i in range(100000):
    #minibatch
    ix = torch.randint(0, X.shape[0], (32,))
    #weights for X
    emb = C[X[ix]]
    # we need emb to be not [12,3,2] but [12,6] so we need to concatinate
    ccc = emb.view(-1, 40)
    # multiply inputs by weights and add bias
    h = torch.tanh(ccc @ W1 + b1)

    logits = h @ W2 + b2
    loss = F.cross_entropy(logits, Y[ix])

    #backward pass
    for p in parameters:
        p.grad = None
    loss.backward()

    for p in parameters:
        ixi = 0.1
        if i > 80000:
            ixi = 0.01
        p.data += -ixi * p.grad



emb = C[X]
ccc = emb.view(-1, 40)
h = torch.tanh(ccc @ W1 + b1)
logits = h @ W2 + b2
loss = F.cross_entropy(logits, Y)
print(loss)


for i in range(10):
    out = []
    context = [0] * block_size
    while True:
        emb = C[torch.tensor([context])]
        h = torch.tanh(emb.view(1, -1) @ W1 + b1)
        logits = h @ W2 + b2
        probs = F.softmax(logits, dim=1)
        ix = torch.multinomial(probs, num_samples=1, generator=g).item()
        context = context[1:] + [ix]
        out.append(ix)
        print(itos[ix])
        if ix == 0:
            break

    print(''.join(itos[i] for i in out))

