import cv2
import face_recognition as fr

# Load images
picture_control = fr.load_image_file('Empleados/Tomas Esquivel.jpg')
test_picture = fr.load_image_file('foto_B.jpg')

# Convert images to RGB
picture_control = cv2.cvtColor(picture_control, cv2.COLOR_BGR2RGB)
test_picture = cv2.cvtColor(test_picture, cv2.COLOR_BGR2RGB)

# Resize images (reduce size by 40% and 25%)
picture_control = cv2.resize(picture_control, (0, 0), fx=0.4, fy=0.4)
test_picture = cv2.resize(test_picture, (0, 0), fx=0.2, fy=0.2)

# Locate control face
control_faces = fr.face_locations(picture_control)
if control_faces:
    place_face_A = control_faces[0]
    face_coded_A = fr.face_encodings(picture_control)[0]

    # Draw rectangle around control face
    cv2.rectangle(picture_control,
                 (place_face_A[3], place_face_A[0]),
                 (place_face_A[1], place_face_A[2]),
                 (0, 255, 0),
                 2)
else:
    print("No se encontró ninguna cara en la imagen de control.")

# Locate test face
test_faces = fr.face_locations(test_picture)
if test_faces:
    place_face_B = test_faces[0]
    face_coded_B = fr.face_encodings(test_picture)[0]

    # Draw rectangle around test face
    cv2.rectangle(test_picture,
                 (place_face_B[3], place_face_B[0]),
                 (place_face_B[1], place_face_B[2]),
                 (0, 255, 0),
                 2)
else:
    print("No se encontró ninguna cara en la imagen de prueba.")

# Make a comparation 
result = fr.compare_faces([face_coded_A], face_coded_B, 0.55 )
print(result)

# Distance measurement
distance = fr.face_distance([face_coded_A], face_coded_B)
print(distance)

# Show results
cv2.putText(test_picture,
            f"{result}{distance.round(2)}",
            (50,50),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (0,255,0),
            2)

# Show images
cv2.imshow('Foto Control', picture_control)
cv2.imshow('Foto Prueba', test_picture)

# Keep program open
cv2.waitKey(0)
cv2.destroyAllWindows()