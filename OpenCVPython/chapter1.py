import cv2
print("Package Imported")

# In order to read images, we have the function 'imread'

# img = cv2.imread("Resources/lena.png")
# cv2.imshow("Output: ",img)
# cv2.waitKey(0)



def showvideo():
    cap = cv2.VideoCapture("Resources/testVideo.mp4")
    # Because the video is a sequence of images, you must add a while loop
    while True:
        success, img = cap.read()
        # success will be a boolean, img will be the image

        cv2.imshow("Video:", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

def webcam():
    cap = cv2.VideoCapture(0)
    cap.set(3,640)
    # width and then size
    cap.set(4,480)
    # height and then size
    cap.set(10,100)
    #we can change the brightness
    while True:
        success, img = cap.read()
        cv2.imshow("Video:", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break