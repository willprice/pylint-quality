def threeNestedConditionals(self):
    x = 0
    y = 0
    if x > 5:
        if x < 10:
            if y > 5:
                print(x)

def twoNestedConditionals(self):
    x = 0
    if x > 5:
        if x < 10:
            print(x)

def threeConditionals(self):
    x = 0
    if x > 5:
        print(x)
    elif x > 10:
        print(x * 2)
    elif x > 15:
        print(x * 3)

def twoConditionalExpressions(self):
    x = 1 if True else 0
    y = 1 if True else 0

def threeConditionalExpressions(self):
    x = 1 if True else 0
    y = 1 if True else 0
    z = 1 if True else 0

def twoForLoops(self):
    for x in range(10):
        for y in range(10):
            print(x, y)

def threeForLoops(self):
    for x in range(10):
        for y in range(10):
            for i in range(10):
                print(i, x, y)

def twoWhileLoops(self):
    x = 0
    while x < 10:
        y = 0
        while y < 10:
            y = x + y

def threeWhileLoops(self):
    x = 0
    while x < 10:
        y = 0
        while y < 10:
            i = 0
            while i < 10:
                y = x + y + i

def listComprehensionWithTwoLoops(self):
    return [(x, y) for x in range(10) for y in range(10)]

def listComprehensionWithThreeLoops(self):
    return [(i, x, y) for x in range(10) for y in range(10) for i in range(10)]

def twoListComprehensionsWithSingleIteration(self):
    xs = [x for x in range(10)]
    ys = [x for x in range(10)]

def threeListComprehensionsWithSingleIteration(self):
    xs = [x for x in range(10)]
    ys = [x for x in range(10)]
    zs = [x for x in range(10)]
