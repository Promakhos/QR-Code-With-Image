import qrcode
from PIL import Image

def create_qr_with_image(data, image_path, output_path):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    qr_img = qr.make_image(fill_color="black", back_color="white")
    
    img = Image.open(image_path)
    
    scale_factor = 0.2
    
    
    img = img.resize((int(img.width * scale_factor), int(img.height * scale_factor)), Image.ANTIALIAS)
    
    img_width, img_height = img.size
    qr_width, qr_height = qr_img.size
    x = (qr_width - img_width) // 2
    y = (qr_height - img_height) // 2
    
    qr_img.paste(img, (x, y))
    
    qr_img.save(output_path)

data_to_encode = "https://www.youtube.com/"
image_path = "Imageyt.jpg"
output_path = "qr.png"

create_qr_with_image(data_to_encode, image_path, output_path)
