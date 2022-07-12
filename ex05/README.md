# 第5回
## 負けるなこうかとん(ex05/fight_koukaton.py)
### ゲーム概要
- ex05/fight_koukaton.pyを実行すると、1600x900のスクリーンに草原が描写され、
  こうかとんを移動させ飛び回る爆弾から逃げるゲーム
- こうかとんが爆弾と接触するとゲームオーバーで終了する
### 操作方法
- 矢印キーでくかとんを上下左右に移動する
### 追加機能
- 音を追加した。
- 背景を草原ではなく宇宙に変更
- こうかとんは下で動く
- エイリアンから爆弾が放たれる
- こうかとんからも爆弾が出る

### ToDo
- sound エラーはでなかったが再生できない

### メモ
- Sprite.update - spriteクラスで行う処理を制御する命令
- Sprite.kill - 全てのGroupからSpriteを削除
- pygame.transform.flip - 画像の上下、左右を反転させる。
- pygame.transform.scale - 画像のサイズを変更。
- pygame.transform.rotate - 画像を回転。