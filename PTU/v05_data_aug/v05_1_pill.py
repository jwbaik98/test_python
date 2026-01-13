from PIL import Image, ImageEnhance, ImageOps
import matplotlib.pyplot as plt

from PIL import Image, ImageEnhance, ImageOps
import matplotlib.pyplot as plt

# 1. 이미지 로드
img = Image.open("captured_images/result_20260113_154450.jpg")

# 2. 이미지 전처리
img_rotated = img.rotate(90)

# 2-1. 이미지 전처리(밝기 조절)
enhancer = ImageEnhance.Brightness(img)
img_bright = enhancer.enhance(2.5)

# 2-2. 이미지 전처리(좌우 반전)
# img_flip = ImageOps.flip(img)
img_flip = ImageOps.mirror(img)

# 3. 결과 시각화
fig, ax = plt.subplots(2, 3, figsize=(20, 10))

# 원본 이미지
ax[0,0].imshow(img)
ax[0,0].axis('off')
ax[0,0].set_title("Original")

# 회전 이미지
ax[0,1].imshow(img_rotated)
ax[0,1].axis('off')
ax[0,1].set_title("Rotated 90")

# + 밝기 이미지
ax[1,0].imshow(img_bright)
ax[1,0].axis('off')
ax[1,0].set_title("Bright")

# + 좌우 반전 이미지
ax[1,1].imshow(img_flip)
ax[1,1].axis('off')
ax[1,1].set_title("Flip")

plt.show()

img_rotated.save("./img_rotated.jpg")
img_bright.save("./img_bright.jpg")
img_flip.save("./img_flip.jpg")
                
print("이미지 저장이 잘 됐습니다.")