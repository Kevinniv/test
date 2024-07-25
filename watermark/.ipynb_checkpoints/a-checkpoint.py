from watermark import add_watermark

# 输入图像路径
input_image = 'input.jpg'
# 水印文字
watermark_text = 'Sample Watermark'
# 输出图像路径
output_image = 'output.jpg'

# 添加水印
add_watermark(input_image, watermark_text, output_image)
