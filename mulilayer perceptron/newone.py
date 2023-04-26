from graphviz import Digraph
import math
import torch

class  Value:
    def __init__(self, data, _children=(), _op = '', label = ''):
        self.data = data
        self._prev = set(_children)
        self._op = _op
        self._backward = lambda: None
        self.label = label
        self.grad = 0.0
    
    def __repr__(self):
        return f"Value(lable = {self.label}; data = {self.data}; grad = {self.grad})"
    
    def __add__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        new = Value(self.data + other.data, (self, other), '+')
        def _backward():
            self.grad += 1.0 * new.grad
            other.grad += 1.0 * new.grad
        new._backward = _backward
        return new
    
    def __mul__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        new = Value(self.data * other.data, (self, other), '*')
  
        def _backward():
            self.grad += other.data * new.grad
            other.grad += self.data * new.grad
        new._backward = _backward

        return new

    def tanh(self):
        n = self.data
        t = (math.exp(2*n) -1)/(math.exp(2*n) + 1)
        out = Value(t, (self, ), 'tanh')

        def _backward():
            self.grad += (1-t**2) * out.grad

        out._backward = _backward
        return out
    
    def __pow__(self, other):
        assert isinstance(other, (int, float)), "only supporting int/float powers for now"
        out = Value(self.data**other, (self,), f'**{other}')

        def _backward():
            self.grad += (other * self.data**(other-1)) * out.grad
        out._backward = _backward

        return out

    def relu(self):
        out = Value(0 if self.data < 0 else self.data, (self,), 'ReLU')

        def _backward():
            self.grad += (out.data > 0) * out.grad
        out._backward = _backward

        return out
    
    def backward(self):
        topo = []
        visited = set()
        def build_topo(v):
            if v not in visited:
                visited.add(v)
                for child in v._prev:
                    build_topo(child)
            topo.append(v)

        self.grad = 1.0
        build_topo(self)
        for node in reversed(topo):
            node._backward()

    def __neg__(self): # -self
        return self * -1

    def __radd__(self, other): # other + self
        return self + other

    def __sub__(self, other): # self - other
        return self + (-other)

    def __rsub__(self, other): # other - self
        return other + (-self)

    def __rmul__(self, other): # other * self
        return self * other

    def __truediv__(self, other): # self / other
        return self * other**-1

    def __rtruediv__(self, other): # other / self
        return other * self**-1
    

def trace(root):
    nodes, edges = set(), set()
    def build(v):
        if v not in nodes:
            nodes.add(v)
            for child in v._prev:
                edges.add((child, v))
                build(child)
    build(root)
    return nodes, edges

def draw_dot(root, format='svg', rankdir='LR'):
    """
    format: png | svg | ...
    rankdir: TB (top to bottom graph) | LR (left to right)
    """
    assert rankdir in ['LR', 'TB']
    nodes, edges = trace(root)
    dot = Digraph(format=format, graph_attr={'rankdir': rankdir}) #, node_attr={'rankdir': 'TB'})
    
    for n in nodes:
        dot.node(name=str(id(n)), label = "{ %s |data %.4f | grad %.4f}" % (n.label, n.data, n.grad), shape='record')
        if n._op:
            dot.node(name=str(id(n)) + n._op, label=n._op)
            dot.edge(str(id(n)) + n._op, str(id(n)))
    
    for n1, n2 in edges:
        dot.edge(str(id(n1)), str(id(n2)) + n2._op)
    
    return dot


"""
x1 = Value(2.0, label = 'x1')
x2 = Value(0.0, label = 'x2')
w1 = Value(-3.0, label = 'w1')
w2 = Value(1.0, label = 'w2')
b = Value(6.88137358, label = 'b')
x1w1 = x1*w1
x1w1.label = 'x1w1'
x2w2 = x2*w2
x2w2.label = 'x2w2'
x1w1x2w2 = x1w1 + x2w2
x1w1x2w2.label = 'x1w1x2w2'
n = x1w1x2w2 + b
n.label = 'n'
o = n.tanh()
o.label = 'o'
"""

# o.backward()
# dot = draw_dot(o)
# print(dot)


# x1 = torch.Tensor([2.0]).double()
# x1.requires_grad = True

# x2 = torch.Tensor([0.0]).double()
# x2.requires_grad = True

# w1 = torch.Tensor([-3.0]).double()
# w1.requires_grad = True

# w2 = torch.Tensor([1.0]).double()
# w2.requires_grad = True

# b = torch.Tensor([6.88137358]).double()
# b.requires_grad = True

# n = x1*w1 + x2*w2 + b
# o = torch.tanh(n)

# print(o.data.item())
# o.backward()

# print('-------')
# print(x1.grad.item())
# print(x2.grad.item())
# print(w1.grad.item())
# print(w2.grad.item())