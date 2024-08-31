import cv2
import mediapipe as mp
import pygame
import numpy as np

# 定数の設定
WIDTH, HEIGHT = 800, 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
PUCK_RADIUS = 10
FPS = 60

# MediaPipeのセットアップ
mp_hands = mp.solutions.hands

# Handsモジュールの初期化
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# ビデオキャプチャの初期化
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("無効なフレームを取得しました。")
        break

    # 画像の反転とRGB変換
    image = cv2.flip(image, 1)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # 手のランドマークの検出
    results = hands.process(image_rgb)

    # 手のランドマークの座標を取得
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            for id, landmark in enumerate(hand_landmarks.landmark):
                height, width, _ = image.shape
                cx, cy = int(landmark.x * width), int(landmark.y * height)
                hx = np.interp(cx, [0, 3000], [width, 0]) #x座標を正規化
                hy = np.interp(cy, [0, 3000], [0, height]) #y座標を正規化
               
                print(f'ランドマークID {id}: cx={cx}, cy={cy}, hx={hx}, hy={hy}')
    
    # 'q'キーが押された場合はループを終了
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# リソースの解放
cap.release()
cv2.destroyAllWindows()
