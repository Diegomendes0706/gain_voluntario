import cv2
import numpy as np

cap = cv2.VideoCapture(0)
prevCircle = None


def dist(x1, y1, x2, y2):
    return np.linalg.norm(np.array((x1, y1)) - np.array((x2, y2)), ord=2)


while True:
    ret, frame = cap.read()
    if not ret: break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1.2, 100,
                               param1=100, param2=30, minRadius=10, maxRadius=100)

    if circles is not None:
        circles = np.uint16(np.around(circles))
        chosen = None
        for i in circles[0, :]:
            if chosen is None:
                chosen = i
            elif prevCircle is not None:
                if dist(chosen[0], chosen[1], prevCircle[0], prevCircle[1]) > dist(i[0], i[1], prevCircle[0],
                                                                                   prevCircle[1]):
                    chosen = i

        cv2.circle(frame, (chosen[0], chosen[1]), 1, (0, 100, 100), 3)
        cv2.circle(frame, (chosen[0], chosen[1]), chosen[2], (255, 0, 255), 3)
        prevCircle = chosen

    cv2.imshow('Detecção de Círculos', frame)

    # Sair com 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
