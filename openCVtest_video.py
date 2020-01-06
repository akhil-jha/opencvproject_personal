import cv2
import datetime

vid = cv2.VideoCapture(0)

#print(vid.get(cv2.CAP_PROP_XI_ACQ_FRAME_BURST_COUNT)," ",vid.get(cv2.CAP_PROP_FRAME_HEIGHT)," ",vid.get(cv2.CAP_PROP_FRAME_WIDTH))
while True:
    ret, frame = vid.read()
    font = cv2.FONT_HERSHEY_DUPLEX
    #text = 'Width: '+ str(vid.get(cv2.CAP_PROP_FRAME_WIDTH)) + ' Height: '+ str(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
    DateTime = str(datetime.datetime.now())
    frame = cv2.putText(frame, DateTime ,(0,50), font, 1, (0,0,0), 2)
    cv2.imshow("Press space for screenshot or q to quit",frame)
    # if cv2.waitKey(1):
    #     cv2.imwrite("/home/akjha/Desktop/screenshot.jpg",frame)
    #     break
    if cv2.waitKey(24) == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()