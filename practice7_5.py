text = input("何を記録しますか")
file = open("sample.text","a",encoding="UTF-8")
file_r = open("sample.txt","r",encoding="UTF-8")
file_w = open("sample.txt","w",encoding="UTF-8")
for line in file_r:
    file_w.write(line)
file_r.close()
file_w.close()

