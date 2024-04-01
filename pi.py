txt = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""
py = list(map(len,txt.replace('.', '').replace(',', '').split()))
print(py)
answer = ""
for i in py: 
    answer += str(i)

print(answer)




