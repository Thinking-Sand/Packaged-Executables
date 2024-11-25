# create_icon.py
from PIL import Image, ImageDraw

# Create a new image with a transparent background
img = Image.new('RGBA', (256, 256), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# Draw a key shape (improved design)
# Key head
draw.ellipse([80, 80, 140, 140], fill='#FFD700')  # Bright gold color
draw.ellipse([95, 95, 125, 125], fill=(0, 0, 0, 0))  # Inner circle

# Key shaft
draw.rectangle([120, 110, 180, 130], fill='#FFD700')

# Key teeth
draw.rectangle([160, 110, 180, 120], fill='#FFD700')
draw.rectangle([160, 120, 180, 130], fill='#FFD700')
draw.rectangle([160, 130, 180, 140], fill='#FFD700')

# Save as ICO file
img.save('key_icon.ico', format='ICO')
print("✅ Icon file created successfully!")