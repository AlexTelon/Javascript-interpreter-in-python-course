
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
    def iter(values,result):
        if not values:
            return result;
        else:
            return iter(values[1:], f(values[0], result))
    return iter(values, null)

# "normal" recursive version to get right fold
def foldr(f, null, values):
        if not values:
            return null;
        else:
            return f(values[0], foldr(f, null, values[1:]))

print("1.4 c")
def my_map(f, seq):
    return foldl((lambda x,y : y + [f(x)]) , [], seq)

def reverse_r(seq):
    return foldr((lambda x,y : y + [x]) , [], seq)

def reverse_l(seq):
    return foldl((lambda x,y : [x] + y) , [], seq)

print(my_map((lambda n:n*2), [1,2,3,4]))
print(reverse_r([1,2,3,4]));
print(reverse_l([1,2,3,4]));

print("uppgift 1.5");

def repeat(f, n):

    if n == 0:
        return (lambda x: x)
    else:
        fprev = repeat(f, n-1)
        return (lambda x: f( fprev(x) ))        
sq = lambda x: x*x
sq_twice = repeat(sq,2)
print sq_twice(5)

print("uppgift 1.5 b");
#the input type has to be the same as the output type.
print("uppgift 1.5 c");

def compose(f, g):
    return lambda x : f( g(x) )

print(compose(lambda x: x*2, lambda x: x + 3)(2))
print("uppgift 1.5 d");
def repeated_application(f, n):
    return accumulate((lambda x,y : compose(x, y)), (lambda x:x), (lambda x: f), 1, (lambda x: x+1), n)

sq_twice2 = repeated_application(sq,2)
print sq_twice2(5)
print("uppgift 1.6 a");
def smooth(f):
    dx = 0.01;
    return (lambda x: (f(x - dx) + f(x) + f(x + dx))/3)


print(smooth(lambda x: x*x)(4))

print("uppgift 1.6 b");
def n_fold_smooth(f, n):
    rep = repeat(smooth,n)
    return rep(f)

    #    return repeat(smooth(f),n);


five__smoothed_square = n_fold_smooth(sq,5);
#print(five__smoothed_square(4))
print (smooth(smooth(smooth(smooth(smooth(sq))))))(4)
print five__smoothed_square(4)

print("#################DEL 2######################")
# 2.1 - applicative will crash. normal will expand and depending on if its satisfied with the function call only then everything will be fine, but if it will try to find its definition when expanding then it will crash too.

print("2.2")
x = 10
def f():
    print ("In f: ", x)
def g(x):
    print("In g: ", x)
    f()
def keep_val(value):
    def f():
        print("---- x={0}, value={1}\n".format(x,value))
    return f

print_mess = keep_val("Stored") #lambda created, no print
value = "New and updated."
print_mess() #execute the print with Stored since that was the parameter sent.
g(5000) # 5000 as parameter is the value of x in g. f does not have parameter (local) so it uses global
x = 0 # new global
g(5000) # same as before for g, new global value for f.

# b 
# print_mess() would output "new and updated." instead
# f would output 5000 both times as it would have access too its "parents" local variables.

# 2.3

