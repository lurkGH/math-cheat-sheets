from pdf2image import convert_from_path

images = convert_from_path('physics.pdf', dpi=300)

images[0].save('physics.png', 'PNG')