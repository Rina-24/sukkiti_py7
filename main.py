import tkinter as tk

root = tk.Tk()
root.geometry("1280x720")
label = tk.Label(root,text="初めてのGUI",font=("Arial",30))
label2 = tk.Label(root,text="初めてのGUI",font=("Arial",30))
label3 = tk.Label(root,text="初めてのGUI",font=("Arial",30))
label4 = tk.Label(root,text="初めてのGUI",font=("Arial",30))
label5 = tk.Label(root,text="初めてのGUI",font=("Arial",30))
label6 = tk.Label(root,text="初めてのGUI",font=("Arial",30))
label7 = tk.Label(root,text="初めてのGUI",font=("Arial",30))

# label2.grid(row=0,column=0)
# label.grid(row=0,column=1)
# label4.grid(row=0,column=2)
# label5.grid(row=0,column=3)

label7.place(x=40,y=100)
# labe6.pack() # packした順に真ん中の上の場所にどんどん追加されていく。
def button_click():
    text = entry.get()
    print(text)

# button = tk.Button(root,text="ボタンだよ",font=("Arial",30),command=button_click)
# button.pack()

# entry = tk.Entry(root,font=("Arial",30))
# entry.pack()

# 画像を表示
# load_image = tk.PhotoImage(file="chopper.png") # 画像の読み込み（ファイルの選択）
# img = tk.Label(root,image=load_image) # 画像パーツの作成
# img.pack() # 画像をウィンドウに配置

# 複数行のメッセージ
# msg = tk.Message(
#     root,
#     text="このキャラクターはチョッパーです。トナカイです。",
#     font="white",
#     width=300
# )

# msg.pack()

canvas = tk.Canvas(root,bg="black")
canvas.pack()

 # 第一、二引数はキャンバスのｘ座標とy座標 第三引数はテキスト内容 第四引数以降は他の調整
 # TKインターキャンバスは左上が（0，0）になる。そのため特に指定しないと0,0の座標になるので見切れる。
 # （基準位置（アンカー）は指定した文字の中心が0，0にくる）"nw"で指定すると（northとwest）北西がアンカーになる。真ん中はセンター
canvas.create_text(0,0,text="テスト",fill="white",font=("Arial",20),anchor="nw")
root.mainloop()
