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

button = tk.Button(root,text="ボタンだよ",font=("Arial",30),command=button_click)
button.pack()

entry = tk.Entry(root,font=("Arial",30))
entry.pack()
root.mainloop()