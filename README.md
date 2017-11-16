# Haircolor-Recognition
二次元イラストに映る人物の髪色を分類します。自分がChainerに慣れるためConvolutional Neural Networkを使っていますが、CNNを使うまでもないかもしれません。また、データのアノテーション用に書いたものなのでCNNの構造としては簡素なものである事にご注意ください。

各プログラムの説明をすると  
` $ python scrayping.py `  
でsafebooruから画像を集めて

` $ python extract.py `  
で集めた画像からlbpcascade_animeface.xmlとopencvで顔を抽出

` $ python preparing_traindata.py `  
でデータの整形と、データとラベリングそれぞれをnpyファイルへ 

` $ python chainerCNN.py`  
で実際に分類、またテストデータに対する精度も計算します。chainerCNN.pyではGPUでの計算を仮定しています。

コメントアウトが少なくわかりにくい所もあると思うかもしれませんが、遠慮無く聞いてください。
