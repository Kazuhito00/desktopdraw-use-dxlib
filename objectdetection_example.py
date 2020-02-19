#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from ctypes import cdll, create_string_buffer
from PIL import ImageGrab
import numpy as np
import cv2 as cv
import tensorflow as tf


def session_run(sess, inp):
    out = sess.run([
        sess.graph.get_tensor_by_name('num_detections:0'),
        sess.graph.get_tensor_by_name('detection_scores:0'),
        sess.graph.get_tensor_by_name('detection_boxes:0'),
        sess.graph.get_tensor_by_name('detection_classes:0')
    ],
                   feed_dict={
                       'image_tensor:0':
                       inp.reshape(1, inp.shape[0], inp.shape[1], 3)
                   })
    return out


if __name__ == '__main__':

    # DXライブラリのDLLをロード
    dxlib = cdll.DxLib_x64

    # ウィンドウタイトル設定
    dxlib.dx_SetMainWindowText(" ")
    # ウィンドウのスタイルを枠無しに指定
    dxlib.dx_SetWindowStyleMode(2)
    # ウィンドウを透明に指定
    dxlib.dx_SetUseBackBufferTransColorFlag(1)
    # ウィンドウモード(TRUE：1)に指定
    dxlib.dx_ChangeWindowMode(1)
    # ウィンドウサイズ変更
    dxlib.dx_SetWindowSizeChangeEnableFlag(0, 0)
    dxlib.dx_SetGraphMode(1920, 1080, 32)
    dxlib.dx_SetWindowSize(1920, 1080)
    # 非アクティブ状態でも動作継続するよう指定
    dxlib.dx_SetAlwaysRunFlag(1)
    # 最前面(DX_WIN_ZTYPE_TOPMOST:3)表示するよう指定
    dxlib.dx_SetWindowZOrder(3)

    # フォント指定
    dxlib.dx_SetFontSize(30)
    dxlib.dx_ChangeFontType(2)

    # 検出モデルロード ########################################################
    with tf.Graph().as_default() as net1_graph:
        filepath = os.path.join(os.getcwd(), "models",
                                "ssdlite_mobilenet_v2_coco_2018_05_09",
                                "frozen_inference_graph.pb")
        graph_data = tf.gfile.FastGFile(filepath, 'rb').read()
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(graph_data)
        tf.import_graph_def(graph_def, name='')

    sess1 = tf.Session(graph=net1_graph)
    sess1.graph.as_default()

    # ラベルロード ############################################################
    labels = ['blank']
    with open("models/coco-labels-paper.txt", "r") as f:
        for line in f:
            labels.append(line.rstrip())

    # DXライブラリ初期化
    if dxlib.dx_DxLib_Init() == -1:
        sys.exit()

    # メインループ
    dxlib.dx_SetDrawScreen(-2)  # DX_SCREEN_BACK:-2
    while dxlib.dx_ProcessMessage() == 0:
        dxlib.dx_ClearDrawScreen()

        # デスクトップキャプチャ
        frame = np.asarray(ImageGrab.grab())
        frame = cv.cvtColor(frame, cv.COLOR_RGB2BGR)

        # 検出実施 ############################################################
        inp = cv.resize(frame, (300, 300))
        inp = inp[:, :, [2, 1, 0]]  # BGR2RGB

        out = session_run(sess1, inp)

        rows = frame.shape[0]
        cols = frame.shape[1]

        # 検出結果可視化 ######################################################
        num_detections = int(out[0][0])
        for i in range(num_detections):
            class_id = int(out[3][0][i])
            score = float(out[1][0][i])
            bbox = [float(v) for v in out[2][0][i]]

            if score < 0.6:
                continue

            x = int(bbox[1] * cols)
            y = int(bbox[0] * rows)
            right = int(bbox[3] * cols)
            bottom = int(bbox[2] * rows)

            dxlib.dx_DrawLineBox(x, y, right, bottom,
                                 dxlib.dx_GetColor(255, 0, 0))

            draw_string = labels[class_id] + '(ID:' + str(
                class_id) + ' Score:' + str('{:.3g}'.format(score)) + ')'
            encode_string = draw_string.encode('utf-8')
            draw_string = create_string_buffer(encode_string)
            dxlib.dx_DrawString(x, y - 37, draw_string,
                                dxlib.dx_GetColor(255, 0, 0))
        dxlib.dx_ScreenFlip()

    dxlib.dx_DxLib_End()