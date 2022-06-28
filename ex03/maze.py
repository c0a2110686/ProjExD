import tkinter as tk
import maze_maker as mm
import random

def key_down(event):
  global key
  key = event.keysym
  #print(f"{key}キーが押されました")

def key_up(event):
 global key
 key = ""

def main_proc():
  global cx, cy, mx, my

  d = {  # キー：押されているキーkey/値: 移動幅リスト[x,y]
    "Up":[0, -1],
    "Down": [0, +1],
    "Left": [-1, 0],
    "Right": [+1, 0],
      }
  
  try:
    if maze_bg[ my+d[key][1]][mx+d[key][0]] == 0: # もし移動先が床ならば
      my, mx =  my+d[key][1], mx+d[key][0]
  except:
    pass


  cx, cy = mx*100+50, my*100+50
  canvas.coords("tori", cx, cy)
  root.after(100, main_proc)

def add_enemy():  #teki1をランダムに出力
    global cx, cy, dx, dy, teki
    teki1 = tk.PhotoImage(file="fig/43012274426004b86abe4d47172c8ee8.png")
    dx = random.randint(0, 13)
    dy = random.randint(0, 13)
    cx, cy = 100*dx, 100*dy
    canvas.create_image(cx, cy, image=teki, tag="teki1")
    canvas.coords("teki1", cx, cy)
    root.after(200, add_enemy)

if __name__ == "__main__":
  global key
  root = tk.Tk()
  root.title("pakupakumeiro")
  
  canvas = tk.Canvas(root, width=1500, height=900, bg="black")
  canvas.pack()

  maze_bg = mm.make_maze(15, 9) # 1:壁 0:床 を表す二次元リスト
  #print(maze_bg)
  mm.show_maze(canvas, maze_bg)# 

  pakuman = tk.PhotoImage(file="fig/b312acaa0397b6d20574f475e35f5ffc.png")
  pakuman = pakuman.zoom(5)
  pakuman = pakuman.subsample(32)
  mx, my = 1, 1
  cx, cy = mx*100+50, my*100+50
  #cx, cy = 300, 400
  canvas.create_image(cx, cy, image=pakuman, tag="tori")

  dx = random.randint(0, 13)
  dy = random.randint(0, 13)
  teki = tk.PhotoImage(file="fig/43012274426004b86abe4d47172c8ee8.png")
  teki = teki.zoom(5)
  teki = teki.subsample(32)
  cx, cy = 100*dx, 100*dy
  canvas.create_image(cx, cy, image = teki, tag="teki1")

  key = ""

  root.bind("<KeyPress>", key_down)
  root.bind("<KeyRelease>", key_up)

  root.after(0, main_proc)
  root.after(0, add_enemy)

  #main_proc()

  
  root.mainloop()