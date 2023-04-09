import cv2


img= cv2.imread('PRO-104-Project-Image-main\solar-system.jpg')

cv2.putText(img,
            "Sun",
            (50,80),
            cv2.FONT_HERSHEY_COMPLEX,
            .5,
            (255,255,255))
cv2.putText(img,
            "Mercury",
            (100,180),
            cv2.FONT_HERSHEY_COMPLEX,
            .5,
            (255,255,255))
cv2.putText(img,
            "Venus",
            (190,180),
            cv2.FONT_HERSHEY_COMPLEX,
            .5,
            (255,255,255))
cv2.putText(img,
            "Earth",
            (280,180),
            cv2.FONT_HERSHEY_COMPLEX,
            .5,
            (255,255,255))
cv2.putText(img,
            "Mars",
            (380,180),
            cv2.FONT_HERSHEY_COMPLEX,
            .5,
            (255,255,255))
cv2.putText(img,
            "Jupiter",
            (580,60),
            cv2.FONT_HERSHEY_COMPLEX,
            .5,
            (255,255,255))
cv2.putText(img,
            "Saturn",
            (800,90),
            cv2.FONT_HERSHEY_COMPLEX,
            .5,
            (255,255,255))
cv2.putText(img,
            "Uranus",
            (970,140),
            cv2.FONT_HERSHEY_COMPLEX,
            .5,
            (255,255,255))
cv2.putText(img,
            "Neptune",
            (1100,150),
            cv2.FONT_HERSHEY_COMPLEX,
            .5,
            (255,255,255))
cv2.imshow("Planet", img)
cv2.waitKey(0)