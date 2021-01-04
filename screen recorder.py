import pyautogui
import cv2
import numpy as np

resolution=pyautogui.size()
codec=cv2.VideoWriter_fourcc(*"XVID")
filename="Resolution.mp4"
fps=60.0
out=cv2.VideoWriter(filename,codec,fps,resolution)
cv2.namedWindow("Screen Recorder",cv2.WINDOW_NORMAL)
cv2.resizeWindow("Screen Recorder",480,270)

while True:
    img=pyautogui.screenshot()
    frame=np.array(img)
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    cv2.imshow("Screen Recorder",frame)
    k=cv2.waitKey(10) & 0xFF
    if k==27:
        break

out.release()
cv2.destroyAllWindows()    
