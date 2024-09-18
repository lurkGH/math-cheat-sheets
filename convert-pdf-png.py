from pdf2image import convert_from_path

images = convert_from_path("physics.pdf")

for i, image in enumerate(images):
    image.save(f"images/physics_{i + 1}.png", "PNG")