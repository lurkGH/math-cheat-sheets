from pdf2image import convert_from_path

filePath = "physics.pdf"

images = convert_from_path(filePath)

for i, image in enumerate(images):
    image.save(f"physics_{i + 1}.png", "PNG")