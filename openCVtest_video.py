import cv2

vid = cv2.VideoCapture(0)

while True:
    ret, frame = vid.read()
    cv2.imshow("Press space for screenshot or q to quit",frame)
    if cv2.waitKey(24) == 32:
        cv2.imwrite("screenshot.jpg",frame)
        break
    if cv2.waitKey(24) == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()