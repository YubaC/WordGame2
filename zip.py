import os

from PIL import Image

 

# 源目录

project_dir = os.path.dirname(os.path.abspath(__file__))

input = os.path.join(project_dir, 'images')

 

# 输出目录

output = os.path.join(project_dir, 'dest')

def modify():

    # 切换目录

    os.chdir(input)

 

    # 遍历目录下所有的文件

    for image_name in os.listdir(os.getcwd()):

        print(image_name)

        im = Image.open(os.path.join(input, image_name))

        im.thumbnail((512, 512))

        if not os.path.exists(os.path.join(output, image_name + '.thumbnail.' + os.path.splitext(image_name)[-1])):

            im.save(os.path.join(output, image_name + '.thumbnail.' + os.path.splitext(image_name)[-1]))

 

if __name__ == '__main__':

    modify()