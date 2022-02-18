from PIL import Image
import os

root_dir = "C:/Users/user/Desktop/celeba_hq_256/"

img_lst = os.listdir(root_dir + "train_image_256/")
# print(img_lst[:5])
# print(len(img_lst))

mask_lst = os.listdir(root_dir + "train_mask_256/")
# print(mask_lst[:5])
# print(len(mask_lst))
# exit()

for idx in range(len(img_lst)):
    print(img_lst[idx])
    img = Image.open(root_dir + "train_mask_256/" + mask_lst[idx])
    img.save(root_dir + "train_image_256_changename/" + img_lst[idx], "PNG")
    # exit()