# невисок = 2030
# висок = 2041
score = 0
year = int(input('Введите год: '))
if year % 4 == 0:
    february = 29
else: 
    february = 28
year = [31, february, 31, 30, 31, 30, 31, 30, 31, 30, 31, 31]
for i in range(len(year)):
    for i in range(year[i]):
        i += 1
        if (i > 9):
            i = sum(map(int, str(i)))
        score += i
print(score)    