def imgCanny(image,threshold1=100,threshold2=100):
    im = cv2.imread(image)
    imcanny = cv2.Canny(image, threshold1,threshold2)
    imshow("CannyImage",imcanny)
    cv2.waitKey(0)

def imgCannyDial(image,threshold1=100,threshold2=100, iterations=1):
    im = cv2.imread(image)
    imcanny = cv2.Canny(image, threshold1,threshold2)

    kernel = np.ones((5, 5), np.uint8)
    imgdial = cv2.dilate(imcanny,kernel,iterations)

    imshow("DialateImage", imgdial)
    cv2.waitKey(0)

def imgErode(image,threshold1=100,threshold2=100,iterations=1):
    im = cv2.imread(image)
    imcanny = cv2.Canny(image, threshold1, threshold2)

    kernel = np.ones((5, 5), np.uint8)
    imgdial = cv2.dilate(imcanny, kernel, iterations)

    imgErode = cv2.erode(imgdial, kernel, iterations)
    imshow("ErodeImage", imgErode)
    cv2.waitKey(0)