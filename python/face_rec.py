

def face_verify():

    import cv2
    import pickle
    import face_recognition

    cap=cv2.VideoCapture(0)

    #Load the saved encodings
    file=open("Py/User.p","rb")
    enc=pickle.load(file)
    file.close()
    print("Encoding Loaded")

    num_frame=0
    matchList=[]

    while num_frame<10:
        _,frame=cap.read()
        # frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        cv2.imshow("Input",frame)
        frame_rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

        face_loc=face_recognition.face_locations(frame_rgb)
        enc_frame=face_recognition.face_encodings(frame_rgb,face_loc)

        #Threshold for face match

        for e,f in zip(enc_frame,face_loc):
            match=face_recognition.compare_faces([enc],e)
            # print(match)
            dist=face_recognition.face_distance([enc],e)
            dist=1-dist
            cv2.rectangle(frame,(f[3],f[0]),(f[1],f[2]),(255,0,0),2)
            cv2.putText(frame,f"{match} {round(dist[0],2)}",(f[3],f[0]),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
            print(match,dist)
            matchList.append(match[0])
        cv2.imshow("Output",frame)
        
        if cv2.waitKey(1)==ord('q'):
            break
        num_frame+=1
    return matchList
    
def find_percentage(lst):
    true_count = lst.count(True)
    total_count = len(lst)
    return (true_count / total_count) * 100


lst=face_verify()
print(lst)
print(find_percentage(lst))
