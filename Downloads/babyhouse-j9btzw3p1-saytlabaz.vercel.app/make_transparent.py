from PIL import Image

def remove_white_bg(image_path, output_path):
    img = Image.open(image_path).convert("RGBA")
    data = img.getdata()
    
    new_data = []
    # threshold for considering a pixel "white"
    threshold = 240
    
    for item in data:
        # item is (R, G, B, A)
        # If the pixel is close to pure white, make it transparent
        if item[0] > threshold and item[1] > threshold and item[2] > threshold:
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)
            
    img.putdata(new_data)
    img.save(output_path, "PNG")

remove_white_bg("BabyHouse.png", "BabyHouse.png")
