def cumsum(inds):
    agg = 0
    yield agg
    for i in inds:
        agg += i
        yield agg

def stagger(gen):
    old = next(gen)
    for new in gen:
        yield old, new
        old = new

