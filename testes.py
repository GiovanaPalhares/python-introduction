import re

texto = "joooooãooo, jooãooo e maria moravam na roça e então decidiram se mudar para cidade, pensaram em se mudar para São Paulo"

print(re.findall(r"[Jj]oão", texto))
print(re.findall(r"jOãO|MARIA", texto, flags=re.I))
# print(re.sub(r"jo+ão+", "felipe", texto, flags=re.I))
# print(re.sub(r"joão"))
print(re.findall(r"jO{2}ãO", texto, flags=re.I))




sentencas = re.split(r' ["d"]+', texto)
print(sentencas)

