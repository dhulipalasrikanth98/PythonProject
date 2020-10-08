import face_recognition
i = face_recognition.load_image_file('C:\Users\dhuli\OneDrive\Pictures\Camera Roll\WIN_20200511_12_21_12_Pro.jpg')
face_locaiton =face_recognition.face_locaiton(i)
print(face_locaiton)