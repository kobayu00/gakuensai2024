***作業する方法についてはこの文素の最後の項を参考に！！***

# gakuensai2024の目的

学園祭の個人企画！！

# 開発の進め方(理想)

- とりあえずホッケーのゲームを作る
- mediapipeで身体の座標取る
- 身体で操作できるようにする
- 対戦できるようにする
- プロジェクターに移してできるか試す
- ちゃんとゲームっぽくする
- 可愛くする
- 音とかつける

# Git, Git hubの使い方について
https://www.youtube.com/watch?v=Dz95iUNt-fg&list=TLPQMzEwODIwMjTqT2_CF9aA1A&index=2

↑
これ見ながらやりました。

よくわかんないのでこれ見てください。


# game_develop.ipynd

ここで開発進めていきましょう、各自ファイル作ってもらってもおけです。

# 共同で開発を進めるためにしてほしいこと
## 最初にやること
  - [GitHub][https://github.co.jp/]のアカウントを作る
  - [VSCode][https://code.visualstudio.com/download]をダウンロードする


1. <>code ってところからzipファイルをダウンロード
1. 解凍してこのリポジトリを自分のPCの好きな場所に入れる
1. 入れた場所でターミナルを開く

~~~
cd <さっき入れたフォルダの名前>)
~~~

1. リモートのリポジトリと、ローカルのリポジトリを表示
~~~
git branch -a
~~~

1. リモートのブランチをローカルのブランチに反映する
~~~
git pull
~~~

1. 新しいブランチを作ってブランチを切り替える
~~~
git checkout -b feature/add_profile_page
~~~

1. 
