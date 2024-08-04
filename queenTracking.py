import cv2

image = cv2.imread("./images/queen.png")
print(image)
# mean_value = cv2.mean(image)
# print(mean_value)

lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
lab_value = cv2.mean(lab_image)
print(lab_value)

image = cv2.imread("./images/carrom_board.jpg")
cv2.imshow('output',image)
cv2.waitKey(-1)

blurred = cv2.GaussianBlur(image,(3,3),None)

lab_image = cv2.cvtColor(blurred, cv2.COLOR_BGR2LAB)

binary = cv2.inRange(lab_image,(0,165,145),(255,175,155))
cv2.imshow('output',binary)
cv2.waitKey(-1)

contours, hierarchy = cv2.findContours(binary,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))

the__biggest_contour_by_area = max(contours, key=cv2.contourArea)
biggest_area = cv2.contourArea(the__biggest_contour_by_area)

print(biggest_area)
if biggest_area < 25:
    print('queen not found')
    cv2.putText(image,'No Queen Found',(30,30),cv2.FONT_HERSHEY_COMPLEX, 1,(0,255,0))
else:
    cv2.drawContours(image, [the__biggest_contour_by_area], 0, (0,255,0), 1)
    print('Queen Found')
    cv2.putText(image,'Queen Found',(30,30),cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0))
    cv2.imshow('output', image)
    cv2.waitKey(-1)



