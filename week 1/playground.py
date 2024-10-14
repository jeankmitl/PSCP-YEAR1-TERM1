def f(x):
    return 2 * x

def g(x):
    return x + 3

# Define a composite function (f ∘ g)
def composite_function(x):
    return f(g(x))

# Test the composite function
result = composite_function(5)
print(result)