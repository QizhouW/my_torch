import torch.nn.functional as F


def nll_loss(output, target):
    return F.nll_loss(output, target)

def mse(output, target):
    return F.mse_loss(output, target)

def bce(output, target):
    return F.binary_cross_entropy(output, target)

