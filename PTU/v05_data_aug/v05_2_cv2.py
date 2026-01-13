import cv2 
import matplotlib.pyplot as plt

# 1. 이미지 로드
img = cv2.imread("v05_data_aug/input.jpg")

# 2. 이미지 전처리
# 2-1. 이미지 전처리(수평 반전)
img_flipped = cv2.flip(img, 1)
# 1 = 수평, 0 = 수직, -1 = 수평+수직

# 2-2. 이미지 전처리(흑백)
img_gray_only = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gray = cv2.cvtColor(img_gray_only, cv2.COLOR_GRAY2BGR)

# 2-3. 이미지 전처리(수평+수직)
img_flipped2 = cv2.flip(img, -1)


# 3. 이미지 시각화
fig, ax = plt.subplots(2,2, figsize = (10,5))
# 3-1. 원본 이미지
ax[0,0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
ax[0,0].axis('off') 
ax[0,0].set_title("Oringinal")

# 3-2. 수평 반전 이미지
ax[0,1].imshow(cv2.cvtColor(img_flipped, cv2.COLOR_BGR2RGB))
ax[0,1].axis('off') 
ax[0,1].set_title("Flip")

# 3-3. + 전처리 이미지(흑백)
ax[1,0].imshow(cv2.cvtColor(img_gray, cv2.COLOR_BGR2RGB))
ax[1,0].axis('off') 
ax[1,0].set_title("Gray")

# 3-3. 수평 반전 이미지
ax[1,1].imshow(cv2.cvtColor(img_flipped2, cv2.COLOR_BGR2RGB))
ax[1,1].axis('off') 
ax[1,1].set_title("Flip2")


plt.show()

# 4. 이미지 저장
cv2.imwrite("./img_flipped.jpg", img_flipped)
cv2.imwrite("./img_gray.jpg", img_gray)
cv2.imwrite("./img_flipped2.jpg", img_flipped2)

print("이미지 저장 완료")