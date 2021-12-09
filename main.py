import streamlit as st

st.title('サイコロを振るプログラム')

"""
##### tkinterを用いたGUIアプリです
```python
import tkinter as tk
import random
number = 0

#ボタンが押された時の動作
def btn_click():
    global number
    canvas.delete('p1')
    number = random.randint(0,5)
    # キャンバスにイメージを表示
    canvas.create_image(0, 0, image=images[number], anchor=tk.NW, tag='p1')
    
#ウィンドウの作成
root = tk.Tk()
root.title("サイコロ")
root.geometry("200x180")
root['bg']='lightgrey'

# キャンバス作成
canvas = tk.Canvas(root, bg="#deb887", height=98, width=98)
# キャンバス表示
canvas.place(x=50, y=40)
images = [
    tk.PhotoImage(file='img/1.png'),
    tk.PhotoImage(file='img/2.png'),
    tk.PhotoImage(file='img/3.png'),
    tk.PhotoImage(file='img/4.png'),
    tk.PhotoImage(file='img/5.png'),
    tk.PhotoImage(file='img/6.png')
]
canvas.create_image(0, 0, image=images[number], anchor=tk.NW, tag='p1')

#ボタン
Button = tk.Button(text=u'サイコロをふる',command=btn_click)
Button.pack()

root.mainloop()
```
"""

link = '[こちら](https://ict119.com/dice_png/)'
st.markdown(f'サイコロの画像データは {link}を使用しました', unsafe_allow_html=True )