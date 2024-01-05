import cv2
import jpg_to_bmp

capture = cv2.VideoCapture(0)

if capture.isOpened() == False:
      print("camera open failed")
      exit()

capNum = int(0)
while True:
     ret, frame = capture.read()
     
     if not ret:
          print("Can't read camera")
          break;
     
     cv2.imshow("camera", frame)
     
     key = cv2.waitKey(1) & 0xFF
     if key == ord('c'):
          img_captured = cv2.imwrite(r'C:\Users\mok07\Desktop\Study\Project\vscode\Receipt_Camera\captured_img\captured_%03d.jpg' % capNum, frame)
          capNum += 1;
          
          jpg_to_bmp.jpg_to_bmp_func(capNum)
          
     if key == ord('q'):
          break;

capture.release()
