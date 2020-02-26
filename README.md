# desktopdraw-use-dxlib
desktopdraw-use-dxlibはDXライブラリ(C# DLL版)をPythonから使用することで、
デスクトップ上に図形やテキストを重畳表示するプログラムです。

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
![2020-02-19 (1)](https://user-images.githubusercontent.com/37477845/74846324-9f77e280-5373-11ea-9e5f-a13ab67c86fd.png)
 
```bash
python objectdetection_example.py
```
![maqbp-1uu9w](https://user-images.githubusercontent.com/37477845/74846159-60e22800-5373-11ea-8920-3906fdf72f52.gif)

# Note
objectdetection_example.pyで利用している物体検出モデルは以下から取得しています。
* http://download.tensorflow.org/models/object_detection/ssdlite_mobilenet_v2_coco_2018_05_09.tar.gz
* https://raw.githubusercontent.com/amikelive/coco-labels/master/coco-labels-paper.txt

# Author
高橋かずひと
 
# License 
desktopdraw-use-dxlib is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).

# DXライブラリ License 
ＤＸライブラリの著作権は山田 巧様が保持しています。

詳しくは以下ライセンステキストをご参照ください。

LICENSE(DxLib)
