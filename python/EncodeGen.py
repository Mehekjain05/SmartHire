import cv2
import os
import pickle
import face_recognition

def Encode(img):
    print("Encoding...")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # cv2.imshow("RGB",img)
    encode=face_recognition.face_encodings(img)[0]
    print("Encoding Complete")
    return encode
def SaveEnc(enc):
    file=open("Py/User.p","wb")
    pickle.dump(enc,file)
    file.close()
    print("Encoding Saved")

img=cv2.imread("Py\Vedant.jpg")
# print(type(img))
# cv2.imshow("Input",img)
enc=Encode(img)
SaveEnc(enc)




cv2.waitKey(0)

cv2.destroyAllWindows()