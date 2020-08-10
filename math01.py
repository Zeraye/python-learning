# problem: W skarbcu królewskim było k monet. Pierwszego dnia rano skarbnik dorzucił 25 monet, a każdego natępnego ranka
# dorzucał o 2 monety więcej niż dnia poprzedniego. Jednocześnie ze skarbca król zabierał w południe każdego dnia 50
# monet. Oblicz najmniejsza liczkę k, dla której w każdym dniu w skarbcu była co najmniej jedna moneta, a następnie
# dla tej wartości k oblicz, w którym dniu w skarbcu była najmniejsza liczba monet.
i = 0
x = 0
k = 0
while i < 30:
    x += 25
    x -= 50
    while k < i:
        x += 2
        k += 1
    k = 0
    print("k", x)
    i += 1
