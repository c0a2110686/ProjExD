import pygame as pg
import sys
import random

def main():
    clock = pg.time.Clock()  #タイマーを作る

    pg.display.set_caption("逃げろ！こうかとん")  #タイトルバーに「逃げろ...」を表示する
    screen_sfc = pg.display.set_mode((1600, 900))  #1600x900の画面Surfaceを生成する
    screen_rct = screen_sfc.get_rect()             #Rect
    bgimg_sfc = pg.image.load("fig/pg_bg.jpg")     #Surface 画像を挿入
    bgimg_rct = bgimg_sfc.get_rect()               
    screen_sfc.blit(bgimg_sfc, bgimg_rct)          #screenSrfaceにbgimg_sfcをbgimg_rctの位置に貼り付ける

    #練習3
    kkimg_sfc = pg.image.load("fig/3.png")               #Surface
    kkimg_sfc = pg.transform.rotozoom(kkimg_sfc, 0, 2.0) #Surface
    kkimg_rct = kkimg_sfc.get_rect()                     #Rect
    kkimg_rct.center = 900, 400                          #900x400の位置にこうかとんの場所を設定
    
    #練習5 爆弾
    bmimg_sfc = pg.Surface((20, 20)) #Surface(幅 : 20, 高さ : 100)を生成する
    bmimg_sfc.set_colorkey((0, 0, 0)) #円の周りを黒に設定
    pg.draw.circle(bmimg_sfc, (255, 0, 0), (10, 10), 10) #Surfaceであるbmimg_sfcを赤で((255, 0, 0))で位置(横:50, 縦:10)に半径10の円を描写する
    bmimg_rct = bmimg_sfc.get_rect()
    bmimg_rct.centerx = random.randint(0, screen_rct.width)  #Surfaceであるbmimg_sfcを画面用Surfaceであるscreenの位置(ランダム)に描写する
    bmimg_rct.centery = random.randint(0, screen_rct.height)
    vx, vy = +1, +1

    while True:
        screen_sfc.blit(bgimg_sfc, bgimg_rct)
        screen_sfc.blit(kkimg_sfc, kkimg_rct)

        #練習2
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return

        #練習４
        key_states = pg.key.get_pressed() #辞書
        if key_states[pg.K_UP] == True: 
            kkimg_rct.centery -= 1   #y座標を-1
        if key_states[pg.K_DOWN] == True: 
            kkimg_rct.centery += 1   #y座標を+1
        if key_states[pg.K_LEFT] == True: 
            kkimg_rct.centerx -= 1   #x座標を-1
        if key_states[pg.K_RIGHT] == True: 
            kkimg_rct.centerx += 1   #x座標を+1

        #練習6
        bmimg_rct.move_ip(vx, vy)
        screen_sfc.blit(bmimg_sfc, bmimg_rct)

        pg.display.update()
        clock.tick(1000)     #1000秒間Windowsが開いた状態になる



if __name__ == "__main__":
    pg.init()          #モジュールを初期化する
    main()             #これから実装するゲームのメインの部分
    pg.quit()          #モジュールの初期化を解除する
    sys.exit()         #プログラムを終了する