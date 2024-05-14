from paddleocr import PaddleOCR, draw_ocr
import os

# Paddleocr目前支持的多语言语种可以通过修改lang参数进行切换
# 例如`ch`, `en`, `fr`, `german`, `korean`, `japan`
ocr = PaddleOCR(use_angle_cls=True, lang="ch")  # need to run only once to download and load model into memory

img_dir = './wang'
#遍历img_dir下的jpg文件，将识别结果保存到output.txt中
text = []
output_filename='./wang/output.txt'
#output_file=open(output_filename,'w')

files = os.listdir('./wang')

# 按照字母顺序对文件进行排序
sorted_files = sorted(files, key=lambda x: x.split('.')[0])

for img in sorted_files:
    if img.endswith('.jpg'):
        img_path = os.path.join(img_dir, img)
        print(img_path)
        result = ocr.ocr(img_path, cls=True)
        for idx in range(len(result)):
            res = result[idx]
            for line in res:
                #print(type(line[1]))
                print(line[1][0])
                #save the content of line[1] to text
                text.append(line[1][0])

        # Create a new file with the same name as the image but with .txt extension
        output_file = os.path.splitext(img)[0] + '.txt'
        output_file_path = os.path.join(img_dir, output_file)

        # Write the text content to the new file
        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(text))

        print('Output file is saved as {}'.format(output_file_path))

        # Clear the text list for the next image
        text = []



