import tkinter as tk
import maze_maker as mm

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def main_proc():
    global cx, cy, mx, my
    delta = { #キー:押されているキーkey/値: 移動幅リスト[x,y]
        #""     : [0, 0],
        "Up"   : [0, -1],
        "Down" : [0, +1],
        "Left" : [-1, 0],
        "Right": [+1, 0],
    }
    try:
        if maze_bg[mx+delta[key][1]][mx+delta[key][0]] == 0: #もし移動先が床なら
            my, mx = my+delta[key][1], mx+delta[key][0]
    except:
        pass

    #if key == "Up"    and maze_bg[my-1][mx] == 0 : my -= 1
    #if key == "Down"  and maze_bg[my+1][mx] == 0 : my += 1
    #if key == "Left"  and maze_bg[my][mx-1] == 0 : mx -= 1
    #if key == "Right" and maze_bg[my][mx+1] == 0 : mx -= 1
    cx, cy = mx*100+50, my*100+50
    #cx, cy = cx+delta[key][0], cy+delta[key][1]
    canvas.coords("tori", cx, cy)
    root.after(100, main_proc)
    


if __name__ == "__main__":
    #global key
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(root, width=1500, height=900, bg="black")
    canvas.pack()

    maze_bg = mm.make_maze(15, 9) #1:壁１/0:床を表す二次元リスト
    mm.show_maze(canvas, maze_bg) #canvasにmaze_bgを描く
    #print(maze_bg)

    tori = tk.PhotoImage(file="fig/5.png")
    mx, my = 1, 1
    cx, cy = mx*100+50, my*100+50
    canvas.create_image(cx, cy, image=tori, tag="tori")

    key = ""
    
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    main_proc()

    root.mainloop()
   
