from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


WIDTH, HEIGHT = 1200, 630
ROOT = Path(__file__).resolve().parent


def font(name: str, size: int):
    return ImageFont.truetype(f"/usr/share/fonts/truetype/dejavu/{name}", size)


image = Image.new("RGB", (WIDTH, HEIGHT), "#faf9f6")
pixels = image.load()
start = (250, 249, 246)
middle = (238, 234, 250)
end = (225, 245, 239)

for y in range(HEIGHT):
    for x in range(WIDTH):
        t = (x / WIDTH) * 0.7 + (y / HEIGHT) * 0.3
        if t < 0.58:
            q = t / 0.58
            color = tuple(round(start[i] + (middle[i] - start[i]) * q) for i in range(3))
        else:
            q = (t - 0.58) / 0.42
            color = tuple(round(middle[i] + (end[i] - middle[i]) * q) for i in range(3))
        pixels[x, y] = color

draw = ImageDraw.Draw(image, "RGBA")
draw.ellipse((860, -160, 1340, 320), outline=(143, 135, 220, 60), width=2)
draw.ellipse((930, -90, 1270, 250), outline=(143, 135, 220, 48), width=2)
draw.ellipse((-150, 420, 290, 860), fill=(188, 235, 220, 115))

draw.rounded_rectangle((85, 74, 161, 150), radius=23, fill="#bcebdc")
draw.line((101, 128, 101, 96), fill="#14213f", width=3)
draw.line((145, 128, 145, 96), fill="#14213f", width=3)
draw.arc((101, 91, 132, 136), 250, 95, fill="#14213f", width=3)
draw.arc((114, 91, 145, 136), 85, 290, fill="#14213f", width=3)
draw.line((123, 102, 123, 136), fill="#14213f", width=3)

navy = "#14213f"
muted = "#617089"
lavender = "#8f87dc"
draw.text((185, 75), "OTA Learning Studio", fill=navy, font=font("DejaVuSerif-Bold.ttf", 42))
draw.text((185, 126), "GUIDED LEARNING. LASTING PROGRESS.", fill=muted, font=font("DejaVuSans-Bold.ttf", 14))
draw.text((84, 240), "Learn with clarity.", fill=navy, font=font("DejaVuSerif.ttf", 67))
draw.text((84, 322), "Grow with confidence.", fill=lavender, font=font("DejaVuSerif.ttf", 67))
draw.text((88, 417), "International online tutoring for GCSE, IGCSE, IB,", fill="#53627a", font=font("DejaVuSans.ttf", 23))
draw.text((88, 451), "A-Level, SAT and international-school learners.", fill="#53627a", font=font("DejaVuSans.ttf", 23))

draw.rounded_rectangle((88, 510, 284, 558), radius=24, fill=navy)
draw.text((186, 534), "BOOK A FREE CALL", anchor="mm", fill="white", font=font("DejaVuSans-Bold.ttf", 15))
draw.rounded_rectangle((302, 510, 697, 558), radius=24, fill=(255, 255, 255, 205), outline=(213, 209, 236, 255), width=1)
draw.text((500, 534), "MATHS • SCIENCE • ENGLISH • CODING", anchor="mm", fill=navy, font=font("DejaVuSans-Bold.ttf", 14))

image.save(ROOT / "assets" / "ota-social-preview.png", optimize=True)
