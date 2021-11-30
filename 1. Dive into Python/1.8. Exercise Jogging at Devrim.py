toplam=0
for i in range(1,6):
    if i<5 :
        hiz=float(input())
        mesafe=float(input())
        toplam+=hiz*mesafe

    elif i == 5:
        yol=float(input())
        print("%.1f" %float(toplam/yol))
