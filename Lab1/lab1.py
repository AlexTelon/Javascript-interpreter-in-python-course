#1.1 a)
def sum_iter(term, lower, successor, upper):
    def iter (lower, result):
        if lower > upper:
            return result
        else:
            return iter(successor(lower), term(lower) + result)
    return iter(lower,0)

print(sum_iter((lambda n:n), 1, (lambda n:n+1), 10))

# 1.1 b)
# The result is built up all along and never needs to go back go calculate something. 
# When it has reached the end it has the final answer and only need to return it.
# Compare this to "normal" recursion where all the terms are added in the end when all individual
# values are found.

# 1.2 
print("uppgift 1.2");
# 1.2 a
def product_iter(term, lower, successor, upper):
    def iter (lower, result):
        if lower > upper:
            return result
        else:
            return iter(successor(lower), term(lower) * result)
    return iter(lower,1)

# 1.2 b
def factorial(x):
    return product_iter((lambda n:n), 1, (lambda n:n+1), x)
#print(factorial(3))
#print(factorial(4))

# 1.3
def accumulate_iter(combiner, null, term, lower, succ, upper):
    def iter (lower, result):
        if lower > upper:
            return result
        else:
            return iter(succ(lower), combiner(term(lower), result))
    return iter(lower,null)

def accumulate(combiner, null, term, lower, succ, upper):
    if lower > upper:
        return null
    else:
        return combiner(term(lower), accumulate(combiner, null, term, succ(lower), succ, upper))

print("1.3 b")
def sum(term, lower, succ, upper):
    return accumulate((lambda x,y: x+y), 0, term, lower, succ, upper)
#print(accumulate((lambda x,y: x+y),0,(lambda n:n), 1, (lambda n:n+1), 10))

def product(term, lower, succ, upper):
    return accumulate((lambda x,y: x*y), 1, term, lower, succ, upper)
print(product((lambda n:n), 1, (lambda n:n+1), 10));
print("1.3 c")
# it must be symmetric! Division is one that wont work.
# below works for uneven numbers but not even numbers, there they differ.
print(accumulate((lambda x,y: x/y),1,(lambda n:n), 1, (lambda n:n+1), 2))
print(accumulate_iter((lambda x,y: x/y),1,(lambda n:n), 1, (lambda n:n+1), 2))

# 1.4 
# tail recursive version to get left fold
def foldl(f, null, values):
    print("Hello");
    def iter(values,result):
        if not values:
            return result;
        else:
            print(result)
            print(values[0])
            return iter(values[1:], f(values[1], result))
            print("bye")
    return iter(values, null)

# "normal" recursive version to get right fold
def foldr(f, null, values):
        if not values:
            return null;
        else:
            return f(values[1], foldr(f, null, values[1:]))

print("1.4 c")
def my_map(f, seq):
    return foldl((lambda x,y : y.append(f(x))) , [], seq)
# append funkar inte för den ändrar bara in-place och returnerar null, så det går inte fortsätta på
# vi ska inte ändra på seq, den ska va konstant. Vi vill skapa något nytt.

print(my_map((lambda n:n*2), [1,2,3,4]))

        
