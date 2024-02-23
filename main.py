import os
import cv2
import jpg_to_bmp
import resize_img
import printer

def start():
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
          
          cv2.imshow("camera", frame) # 카메라 영상 출력
          
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
               
               # jpg이미지를 bmp이미지로 변환
               jpg_to_bmp.jpg_to_bmp_func(capNum)
               
               # 이미지 해상도 변경
               resize_img.resize_image(240, 180)
               
               printer.print_image()
               
               break
                        
          #if key == ord('q'):
          #     break;
          
     capture.release()
     
start()