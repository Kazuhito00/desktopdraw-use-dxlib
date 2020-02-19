#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from ctypes import cdll, create_string_buffer

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

    # DXライブラリ初期化
    if dxlib.dx_DxLib_Init() == -1:
        sys.exit()

    # メインループ
    dxlib.dx_SetDrawScreen(-2)  # DX_SCREEN_BACK:-2
    while dxlib.dx_ProcessMessage() == 0:
        dxlib.dx_ClearDrawScreen()

        draw_string = 'DESKTOP DRAW TEST'
        encode_string = draw_string.encode('utf-8')
        draw_string = create_string_buffer(encode_string)
        dxlib.dx_DrawString(300, 300, draw_string, dxlib.dx_GetColor(
            0, 255, 0))
        dxlib.dx_ScreenFlip()

    dxlib.dx_DxLib_End()