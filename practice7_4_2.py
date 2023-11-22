from math import pi

print(f"円周率は{pi}です")
for num in range(5):
    print(f"小数点第{num+1}位で四捨五入すると{round(pi,num)}です。")
    