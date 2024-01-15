# %% [markdown]
# # Small Problems

# %% [markdown]
# ## The Fibonacci Sequence

# %%
nums = [0, 1, 1, 2, 3, 5, 8, 13, 21]

# %%
# fib(n) = fib(n - 1) + fib(n - 2)

# %%
def fib1(n: int) -> int:
    if n < 2:
        return n
    return fib1(n - 2) + fib1(n - 1)

# %%
print(fib1(5))

# %%
def fib2(n: int) -> int:
    if n < 2:
        return n
    return fib2(n - 2) + fib2(n - 1)

# %%
print([fib2(c) for c in range(10)])

# %%
def fib3(n):
    ultimo=1
    penultimo=1
    if (n==1) or (n==2):
        print("1")
    else:
        for count in range(2,n):
            termo = ultimo + penultimo
            penultimo = ultimo
            ultimo = termo
            count += 1
        print(termo)

# %%
fib3(4)

# %% [markdown]
# ## Calculating PI

# %%
pi = 4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11

# %%
lista = []
for c in range(1000000):
    if c % 2 == 1:
        lista.append(4/c)

# %%
soma = 0
for c, k in zip(lista, range(len(lista))):
    soma += (-1)**k * c

# %%
soma

# %%
def calculate_pi(n: int) -> int:
    lista = [4/c for c in range(n + 1) if c % 2 == 1]
    nova = [(-1)**k * c for c,k in zip(lista, range(len(lista)))]
    print(sum(nova))

# %%
calculate_pi(100000000)

# %%



