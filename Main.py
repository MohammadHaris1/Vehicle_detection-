import cv2 #image acquistion                                                                                                                                                                                                                                                                                                                                                          
import imutils #resize theframe
cascade_src = 'cars.xml'
car_cascade = cv2.CascadeClassifier(cascade_src)
cam = cv2.VideoCapture(0)

while True:
    detected = 0
    _,img=cam.read() #reading frame from camera
    img=imutils.resize (img, width=300) #resize to 300
    gray = cv2.cvtColor (img, cv2.COLOR_BGR2GRAY) #color to Grayscale
    cars = car_cascade.detectMultiScale(gray, 1.1, 1) #coordinates of vehic for (x,y,w,h) in cars:
    for(x,y,w,h) in cars:
        cv2.rectangle (img, (x, y), (x+w, y+h), (0,0,255),2)    
    cv2.imshow("Frame", img)
    b= str(len(cars))                                                                                                                                                                                                                                                                       
    a= int(b)
    detected=a
    n = detected    
    print ("---------------------------------------------")
    print ("North: %d "% (n))
    if n>=2:
        print ("North More Traffic")
    else:
        print ("no traffic")
    if cv2.waitKey (33) == 27:
        break
cam.release()
cv2.destroyAllWindows()
    
