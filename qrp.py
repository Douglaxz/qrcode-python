import qrcode

# Define as opções de personalização do QR code
options = {
    'border': 2,
    'box_size': 10,
    'image_factory': qrcode.image.svg.SvgPathImage,
    'fill_color': '#333',
    'back_color': '#fff',
}

# Cria um QR code com a mensagem "Hello, world!" e as opções de personalização definidas acima
img = qrcode.make("Hello, world!", **options)

# Salva o QR code como um arquivo SVG j
img.save("hello.svg")
