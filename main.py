import cv2
cap = cv2.VideoCapture(0)
pathf = "haarcascade_frontalface_default.xml"
pathn = "haarcascade_mcs_nose.xml"
pathm = "haarcascade_mcs_mouth.xml"

while(True):
    ret, frame = cap.read()
    face_cascade = cv2.CascadeClassifier(pathf)
    nose_cascade = cv2.CascadeClassifier(pathn)
    mouth_cascade = cv2.CascadeClassifier(pathm)
    #eye_cascade = cv2.CascadeClassifier(pathe)

    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    nose = nose_cascade.detectMultiScale(
        gray, scaleFactor=1.5, minNeighbors=5, minSize=(30, 30))
    mouth = mouth_cascade.detectMultiScale(
        gray, scaleFactor=1.5, minNeighbors=5, minSize=(30, 30))

    for(nx, ny, nw, nh) in nose:
        cv2.rectangle(frame, (nx, ny), (nx+nw, ny+nh), (255, 0, 0), 1)
    for(mx, my, mw, mh) in mouth:
        my = int(my - 0.15*mh)
        cv2.rectangle(frame, (mx, my), (mx+mw, my+mh), (2, 0, 0), 1)

    if(len(nose) != 0 and len(mouth) != 0):
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
    elif(len(nose) != 0):
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
    else:
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow("test", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
