import math
import torch
import newone
import random
from graphviz import Digraph

dot = Digraph()

class Neuron:
    def __init__(self, nin):
        self.w = [newone.Value(random.uniform(-1,1)) for i in range(nin)]
        self.b = newone.Value(random.uniform(-1,1))

    def __call__(self, x):
        act = sum(wi*xi for wi,xi in zip(self.w, x)) + self.b
        out = act.tanh()
        return out

    def parameters(self):
        return self.w + [self.b]
    
class Layer:
    def __init__(self, nin, nrons):
        self.neurons = [Neuron(nin) for i in range(nrons)]

    def __call__(self, x):
        outs = [i(x) for i in self.neurons]
        return outs[0] if len(outs) == 1 else outs
    
    def parameters(self):
        return [p for neuron in self.neurons for p in neuron.parameters()]
    
class MLP:
    def __init__(self, nin, nouts):
        sz = [nin] + nouts
        self.layers = [Layer(sz[i], sz[i+1]) for i in range(len(nouts))]
                       
    def __call__(self, x):
        for l in self.layers:
            x = l(x)
        return x
    
    def parameters(self):
        return [p for layer in self.layers for p in layer.parameters()]


n = MLP(3, [4,4,1])



xs = [
    [2.0, 3.0, -1.0],
    [1.0, 2.0, 1.0],
    [0.0, 1.0, 1.0],
    [1.0, 1.0, 1.0],
]

ys = [1.0, -1.0, -1.0, 1.0]

# newdot = newone.draw_dot(loss)
# newdot.render(filename='graph', format='pdf')

for k in range(20):
    #forward pass
    ypred = [n(x) for x in xs]
    loss = sum([(yout - ygt)**2 for ygt, yout in zip(ys, ypred)])

    #backward pass
    for p in n.parameters():
        p.grad
    loss.backward()

    #parameneter update
    for g in n.parameters():
        g.data += -0.05*g.grad
    
    print(loss)

print(ypred)
