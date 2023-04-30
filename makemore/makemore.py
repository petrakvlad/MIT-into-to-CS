import torch
import matplotlib.pyplot as plt
import torch.nn.functional as F

# Bigram language model

words = open("/mnt/c/Users/Vlad/Documents/GitHub/someproj/makemore/names.txt", "r").read().splitlines()
print(len(words))

# N = torch.zeros((27,27), dtype=torch.int32)

chars = sorted(set(''.join(words)))
stoi = {s:i+1 for i, s in enumerate(chars)}
stoi[','] = 0

itos = {i:s for s,i in stoi.items()}

# for w in words:
#     chr = [','] + list(w) + [',']
#     for w1, w2 in zip(chr, chr[1:]):
#         N[stoi[w1], stoi[w2]] += 1

# plt.figure(figsize=(28,28))
# plt.imshow(N, cmap='Blues')
# for i in range(27):
#     for j in range(27):
#         chstr = itos[i] + itos[j]
#         plt.text(j, i, chstr, ha='center', va='bottom', color='gray')
#         plt.text(j, i, N[i,j].item(), ha='center', va='top', color='gray')
# plt.axis('off')
# plt.show()

# g = torch.Generator().manual_seed(2147483647)
# p = (N+2).float()
# p = p/p.sum(1, keepdim=True)

# for _ in range(10):
#     out = []
#     ix = 0
#     while True:
#         r = p[ix,:]
#         ix = torch.multinomial(r, 1, replacement=True, generator=g).item()
#         out.append(itos[ix])
#         if ix == 0:
#             break

#     print(''.join(out))

# loglike = 0
# n = 0

# for w in ["andrejq"]:
#     chr = [','] + list(w) + [',']
#     for w1, w2 in zip(chr, chr[1:]):
#         logprob = torch.log(p[stoi[w1], stoi[w2]])
#         print(w1, w2, p[stoi[w1], stoi[w2]], logprob)
#         loglike += logprob
#         n +=1

# negloglike = -loglike
# l = negloglike/n
# print(l)

xs, ys = [],[]
numeex = 0

for w in words:
    chr = [','] + list(w) + [',']
    for w1, w2 in zip(chr, chr[1:]):
        xs.append(stoi[w1])
        ys.append(stoi[w2])
        numeex += 1
xs = torch.tensor(xs)# input letters tensor
ys = torch.tensor(ys)# correct output letters tensor
print("number of examples", numeex)


# initialise random initial weights for a neuron, each neuron takes 27 inputs
g = torch.Generator().manual_seed(2147483647)
w = torch.randn((27,27), generator = g, requires_grad=True)

for i in range(100):
    #forward pass
    xenc = F.one_hot(xs, num_classes = 27).float() # encode tensor of integers into tensor of (5, 27) dims
    logits = xenc@w
    counts = torch.exp(logits)
    probs = counts/counts.sum(1, keepdims = True)#probabilities for the next character
    loss = -probs[torch.arange(len(xs)), ys].log().mean()
    print(loss)

    #backward pass
    w.grad = None #set grad to zero
    loss.backward()

    #update
    w.data += -50 * w.grad 

print(w[0])