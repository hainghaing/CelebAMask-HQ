from PIL import Image
import os

root_dir = "C:/Users/user/Desktop/celeba_hq_256/"

lst = os.listdir(root_dir + "train_mask_512/")

for item in lst:
    img = Image.open(root_dir + "train_mask_512/" + item)
    print(img.size)
    img_resized = img.resize((256, 256))
    print(img_resized.size)
    # img_resized.show()
    img_resized.save(root_dir + "train_mask_256/" + item, "PNG")
    # exit()