import pygame as pg
import sys

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
    

    while True:
        screen_sfc.blit(bgimg_sfc, bgimg_rct)
        screen_sfc.blit(kkimg_sfc, kkimg_rct)

        #練習2
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        pg.display.update()
        clock.tick(1000)     #1000秒間Windowsが開いた状態になる



if __name__ == "__main__":
    pg.init()          #モジュールを初期化する
    main()             #これから実装するゲームのメインの部分
    pg.quit()          #モジュールの初期化を解除する
    sys.exit()         #プログラムを終了する