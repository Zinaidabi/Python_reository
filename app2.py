print("Hi, Python!")

num_terms = 10
fibonacci = [0, 1]

while len(fibonacci) < num_terms:
  next_term = fibonacci[-1] + fibonacci[-2]
  fibonacci.append(next_term)
  
print(fibonacci)