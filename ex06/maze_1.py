import tkinter
import random
import tkinter.messagebox

key = ""
def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

mx = 1
my = 1
yuka = 0
def main_proc():
    global mx,my,yuka
    if key == "Shift_L" and yuka > 1: #左のシフトを押すとやり直し
        canvas.delete("PAINT") #ピンクの画像を全て削除
        mx = 1 #キャラクターを初期位置に移動
        my = 1 #キャラクターを初期位置に移動
        yuka = 0 #床を塗った数を初期化
        for y in range(7): #床を塗った数を初期化
            for x in range(10):
                if maze[y][x] == 2:
                    maze[y][x] = 0
    if key == "Up" and maze[my-1][mx] == 0:
        my = my - 1
    if key == "Down" and maze[my+1][mx] == 0:
        my = my + 1
    if key == "Left" and maze[my][mx-1] == 0:
        mx = mx - 1
    if key == "Right" and maze[my][mx+1] == 0:
        mx = mx + 1
    if maze[my][mx] == 0:
        maze[my][mx] = 2
        yuka = yuka + 1
        canvas.create_rectangle(mx*80,my*80,mx*80+79,my*80+79,fill="pink",width=0, tag="PAINT") #タグづけして一度に全て削除
    canvas.delete("MYCHR") #キャラを消す
    canvas.create_image(mx*80+40, my*80+40, image=img, tag="MYCHR") #キャラを再描写
    if yuka == 100: #床を全部塗ったらダイアログを出す
        canvas.update()
        tkinter.messagebox.showinfo("クリア","全部塗り終わりました")
    else:
        root.after(300,main_proc)

root = tkinter.Tk()
root.title("迷路移動して塗る")
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)
canvas = tkinter.Canvas(width=1600, height=900, bg="white")
canvas.pack()
maze = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,1],
    [1,0,1,1,0,0,1,1,1,1,1,0,0,0,1,0,0,0,0,1],
    [1,0,0,1,0,0,0,0,0,0,1,0,0,0,1,0,1,0,0,1],
    [1,0,0,1,1,1,1,1,1,0,1,0,0,0,1,1,1,0,0,1],
    [1,1,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,1],
    [1,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,1,1,0,1],
    [1,0,1,1,1,1,0,0,1,0,0,1,1,1,0,0,0,0,0,1],
    [1,0,1,0,0,0,0,0,1,0,0,0,0,0,1,1,1,1,0,1],
    [1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

for y, row in enumerate(maze):
    for x, cell in enumerate(row):
        if cell == 1:
            canvas.create_rectangle(x*80,y*80,x*80+79,y*80+79, fill="gray", width=0)
img = tkinter.PhotoImage(file="fig/pipo-halloweenchara2016_01.png")
canvas.create_image(mx*80+40, my*80+40, image=img, tag="MYCHR")
main_proc()
root.mainloop()