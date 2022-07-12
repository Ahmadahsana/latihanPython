```python 

# mendefinisikan direktori
path / direktori => path = r'gambar/iamge.jpg'

# membaca gambar
Syntax: cv2.imread(path, flag)
contoh : img = cv2.imread("gombalan.png", cv2.IMREAD_COLOR) #warna asli
contoh : img = cv2.imread(path, 0) # 0 menandakan grayscale

# menampilkan gambar
Syntax: cv2.imshow(window_name, image)

window_name = 'image'
cv2.imshow(window_name, img)

# merename file gambar
filename = 'hai cuk'
cv2.imwrite(filename, img)

# split warna 
B, G, R = cv2.split(image)

cv2.imshow("blue", B)
cv2.waitKey(0)
 
cv2.imshow("Green", G)
cv2.waitKey(0)
 
cv2.imshow("red", R)
cv2.waitKey(0)




```
