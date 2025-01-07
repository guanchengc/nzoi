import math

class FarmInput:
    num = 1
    args = []
    average = 1

    def __init__(self, num, args):
        self.num = num
        self.args = args
        self.average = sum(args) / num

def checkUnhealthy(inputs):
    for average in inputs:
        if sum(average.args) >= average.num * 12:
            pass
        else:
            return False

    return True

def checkResow(inputs):
    count = sum([i >= 25 for i in inputs[0].args]) 
    if count * 2 >= inputs[0].num:
        return True
    
    return False

def resolveInput(n, c):
        n = int(n)
        args = list(map(int, c.split()))
        return FarmInput(n, args)

def run(inputs):
    if checkUnhealthy(inputs):
        if checkResow(inputs):
            return "resow"
        else:
            return "unhealthy"
    else:
        return"healthy"


def main():    
    inputs = []
    while(len(inputs) < 3):
        inputs.append(resolveInput(input(), input()))
    run(inputs)


def test():
    arg = resolveInput("2", "12 12")
    assert arg.num == 2
    assert len(arg.args) == 2
    assert arg.args[0] == 12

    arg = resolveInput("2", " 12  12 ")
    assert arg.num == 2
    assert len(arg.args) == 2
    assert arg.args[0] == 12

    inputs = [
        resolveInput("2", "12 12"), 
        resolveInput("3", "1 12 12"), 
        resolveInput("4", "12 34 12 12")
        ]
    assert checkUnhealthy(inputs) == False

    print ('ok')


test()