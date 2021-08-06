```bash
+--darknet
ㅣ    +--backup
ㅣ    ㅣ    +--yolov3_training_last.weights # 학습된 가중치가 저장되는 파일
ㅣ    +--cfg
ㅣ    ㅣ    +--yolov3_training.cfg # yolo 설정에 필요한 파일
ㅣ    +--data
ㅣ    ㅣ    +--obj
ㅣ    ㅣ    ㅣ    +--images.zip # 유통기한 데이터셋
ㅣ    ㅣ    +--obj.data # 정보 종합 파일
ㅣ    ㅣ    +--obj.names # class 이름이 저장된 파일
ㅣ    ㅣ    +--train.txt # 학습시킬 이미지들 경로 저장된 파일
ㅣ    +--find_ed.py # darknet 실행하는 코드
+--image-process.py # 사진에 유통기한 부분을 그려주는 코드
+--make-integer.py # result.txt에 담긴 x, y, w, h 정보를 추출하는 코드
+--result.txt # darknet/find_ed.py의 실행결과가 저장되는 파일
```
