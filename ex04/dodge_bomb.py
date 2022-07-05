import pygame as pg
import sys
import random

def main():
    clock = pg.time.Clock()  #タイマーを作る(表示時間の設定)

    pg.display.set_caption("逃げろ！こうかとん")     #タイトルバーに「逃げろ...」を表示する
    screen_sfc = pg.display.set_mode((1600, 900))  #1600x900の画面Surfaceを生成する
    screen_rct = screen_sfc.get_rect()             #画像用Rect
    bgimg_sfc = pg.image.load("fig/pg_bg.jpg")     #Surface 背景画像を挿入
    bgimg_rct = bgimg_sfc.get_rect()               #背景用rect
    screen_sfc.blit(bgimg_sfc, bgimg_rct)          #screenSrfaceにbgimg_sfcをbgimg_rctの位置に貼り付ける

    #練習3
    kkimg_sfc = pg.image.load("fig/3.png")               #Surface
    kkimg_sfc = pg.transform.rotozoom(kkimg_sfc, 0, 2.0) #Surface
    kkimg_rct = kkimg_sfc.get_rect()                     #Rect
    kkimg_rct.center = 900, 400                          #900x400の位置にこうかとんの場所を設定
    
    #練習5 爆弾
    bmimg_sfc = pg.Surface((20, 20))                         #Surface(幅 : 20, 高さ : 100)を生成する
    bmimg_sfc.set_colorkey((0, 0, 0))                        #円の周りを黒に設定
    pg.draw.circle(bmimg_sfc, (255, 0, 0), (10, 10), 10)     #Surfaceであるbmimg_sfcを赤で((255, 0, 0))で位置(横:50, 縦:10)に半径10の円を描写する
    bmimg_rct = bmimg_sfc.get_rect()
    bmimg_rct.centerx = random.randint(0, screen_rct.width)  #Surface 爆弾のx座標をランダムに設定
    bmimg_rct.centery = random.randint(0, screen_rct.height) #Surface 爆弾のy座標をランダムに設定
    vx, vy = +1, +1

    while True:
        screen_sfc.blit(bgimg_sfc, bgimg_rct) #screenに背景画像を合成
        screen_sfc.blit(kkimg_sfc, kkimg_rct)

        #練習2
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return

        #練習４
        key_states = pg.key.get_pressed() # 「↑,→,↓,←」キーを押されたときの反応を規定した辞書を作成
        if key_states[pg.K_UP] == True: 
            kkimg_rct.centery -= 1   #y座標を-1
        if key_states[pg.K_DOWN] == True: 
            kkimg_rct.centery += 1   #y座標を+1
        if key_states[pg.K_LEFT] == True: 
            kkimg_rct.centerx -= 1   #x座標を-1
        if key_states[pg.K_RIGHT] == True: 
            kkimg_rct.centerx += 1   #x座標を+1

        if check_bound(kkimg_rct, screen_rct) != (1, 1): #領域外だったら
            if key_states[pg.K_UP] == True: 
                kkimg_rct.centery += 1   #y座標を-1
            if key_states[pg.K_DOWN] == True: 
               kkimg_rct.centery -= 1   #y座標を+1
            if key_states[pg.K_LEFT] == True: 
                kkimg_rct.centerx += 1   #x座標を-1
            if key_states[pg.K_RIGHT] == True: 
                kkimg_rct.centerx -= 1   #x座標を+1
            screen_sfc.blit(kkimg_sfc, kkimg_rct)

        #練習6
        bmimg_rct.move_ip(vx, vy) #爆弾用のRectを移動する
        #練習5
        screen_sfc.blit(bmimg_sfc, bmimg_rct)
        #練習7
        yoko, tate = check_bound(bmimg_rct, screen_rct)
        vx *= yoko
        vy *= tate

        


        pg.display.update()
        clock.tick(1000)     #1秒間1000画像Windowsが開いた状態になる

def check_bound(rct, scr_rct): #RectとScreenRect
    x, y = +1, +1 #領域内
    if rct.left < scr_rct.left or scr_rct.right < rct.right:
        x = -1
    if rct.top < scr_rct.top or scr_rct.bottom < rct.bottom:
        y = -1
    return x, y



if __name__ == "__main__":
    pg.init()          #モジュールを初期化する
    main()             #これから実装するゲームのメインの部分
    pg.quit()          #モジュールの初期化を解除する
    sys.exit()         #プログラムを終了する