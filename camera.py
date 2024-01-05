import os
import cv2
import jpg_to_bmp

def capture():
     capture = cv2.VideoCapture(0)
     
     if capture.isOpened() == False:
          print("camera open failed")
          exit()
     
     capNum = int(0) # 캡쳐된 사진 카운트
     
     while True:
          ret, frame = capture.read()
          
          if not ret:
               print("Can't read camera")
               break
          
          cv2.imshow("camera", frame)
          
          key = cv2.waitKey(1) & 0xFF
          
          if key == ord('c'):
               # 현재 스크립트 파일이 위치한 디렉토리 경로
               script_dir = os.path.dirname(os.path.abspath(__file__))

               # 저장할 디렉토리 생성 (만약 없으면)
               save_dir = os.path.join(script_dir, 'captured_img')
               os.makedirs(save_dir, exist_ok=True)

               # 파일 경로를 상대경로로 지정
               file_path = os.path.join(save_dir, 'captured_%03d.jpg' % capNum)
               
               img_captured = cv2.imwrite(file_path, frame)
               capNum += 1
               
               jpg_to_bmp.jpg_to_bmp_func(capNum)
               
               break
                        
          #if key == ord('q'):
          #     break;
          
     capture.release()