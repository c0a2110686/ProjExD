# 第2回
## 超高機能電卓(ex02/calc.py)
###　追加機能
 - 四則演算 : +以外の四則演算をする
 - クリア : click_buttonに入力されている数学、数学の1文字をdelateする
 - オールクリア : click_buttonに入力されている数字、数式の文字列全体をdelateする
 - 数値としてふさわしくないボタンは押しても表示されない
 - ボタンの背景と文字の色を換えた : tk.Buttonのbgは背景。fgは文字の色

 ### メモ
  - tk() : ウィンドウ
  　　　　　title(タイトル):ウィンドウのタイトルを設定
           geometyr(サイズ):ウィンドウのサイズ"幅x高さ"を設定
           resizable(横方向、縦方向):サイズ変更可能True or 不可能False
           mainloop():ウィンドウを表示
  - label() : 文字列ラベル
              font:(フォントタイプ、フォントサイズ)
  - button() : ボタン
               be:背景
               fg:文字の色
               command:クリックした際の反応
  - canvas() : キャンパス
  　　　　　　　create_image(x座標,y座標,image=PhotoImageクラスのインスタンス)
               create_line(座標列,fill=色,width=線の太さ)
               create_rectangle(座標,fill=塗色,outline=枠線の色,width=枠線の太さ)
  - entry() : テキスト入力欄
  - text() : 複数行のテキスト入力欄
  - checkbutton() : チェックボタン（複数選択可）
  - ブランチを作るコマンド : git branch ブランチ名
  - ブランチを切り替えるコマンド : git switch ブランチ名
  - mainブランチに戻るコマンド : git switch main
  - 