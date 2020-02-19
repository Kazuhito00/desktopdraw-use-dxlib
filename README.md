# desktopdraw_use_dxlib
desktopdraw_use_dxlibはDXライブラリ(C# DLL版)を用いて、Pythonでデスクトップ上に描画するソフトです。

[ＤＸライブラリ](https://dxlib.xsrv.jp/)を利用しています。

描画用のAPIの詳細は[ＤＸライブラリ](https://dxlib.xsrv.jp/)を参照ください。


# Enviroment

* Windows10

# Requirement

* OpenCV 3.4.2
* Pillow 6.1.0
* Tensorflow 1.14.0(objectdetection_example.py 実行時のみ)
 
# Usage
 
サンプルの実行方法は以下です。
 
```bash
python desktopdraw_use_dxlib.py
```
 
```bash
python objectdetection_example.py
```

# Note
objectdetection_example.pyで利用している物体検出モデルは以下から取得しています。
* http://download.tensorflow.org/models/object_detection/ssdlite_mobilenet_v2_coco_2018_05_09.tar.gz
* https://raw.githubusercontent.com/amikelive/coco-labels/master/coco-labels-paper.txt

# Author
高橋かずひと
 
# License 
desktopdraw_use_dxlib is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).

# DXライブラリ License 
ＤＸライブラリの著作権は山田 巧様が保持しています。

詳しくは以下ライセンステキストをご参照ください。

LICENSE(DxLib)