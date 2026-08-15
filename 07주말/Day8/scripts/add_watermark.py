import os
from PIL import Image, ImageDraw, ImageFont

INPUT_PATH = r"C:\Agent\Day8\output\sample.jpg"
OUTPUT_DIR = r"C:\Agent\Day8\output"
OUTPUT_FILENAME = "watermarked.jpg"

WATERMARK_TEXT = "AI DESIGN CLASS"
TEXT_COLOR = (255, 255, 255)  # 흰색
OPACITY = 0.6  # 투명도 60%
MARGIN = 32  # 가장자리 여백(px)

FONT_PATH = r"C:\Windows\Fonts\malgunbd.ttf"
FONT_SIZE_RATIO = 0.035  # 이미지 짧은 변 기준 폰트 크기 비율


def add_watermark():
    base = Image.open(INPUT_PATH).convert("RGBA")
    overlay = Image.new("RGBA", base.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    font_size = max(16, int(min(base.size) * FONT_SIZE_RATIO))
    font = ImageFont.truetype(FONT_PATH, font_size)

    bbox = draw.textbbox((0, 0), WATERMARK_TEXT, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]

    x = base.width - MARGIN - text_w - bbox[0]
    y = base.height - MARGIN - text_h - bbox[1]

    alpha = int(255 * OPACITY)
    draw.text((x, y), WATERMARK_TEXT, font=font, fill=(*TEXT_COLOR, alpha))

    watermarked = Image.alpha_composite(base, overlay).convert("RGB")

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output_path = os.path.join(OUTPUT_DIR, OUTPUT_FILENAME)
    watermarked.save(output_path, "JPEG", quality=95)
    print(f"저장 완료: {output_path}")


if __name__ == "__main__":
    add_watermark()
