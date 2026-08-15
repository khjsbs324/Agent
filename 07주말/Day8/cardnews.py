from PIL import Image, ImageDraw, ImageFont
import os
import textwrap

# ===== 카드뉴스 설정 =====
WIDTH, HEIGHT = 1080, 1080
BG_COLOR = (255, 255, 255)
TITLE_COLOR = (20, 20, 20)
BODY_COLOR = (60, 60, 60)

FONT_DIR = r"C:\Windows\Fonts"
TITLE_FONT_PATH = os.path.join(FONT_DIR, "malgunbd.ttf")
BODY_FONT_PATH = os.path.join(FONT_DIR, "malgun.ttf")

TITLE_FONT_SIZE = 72
BODY_FONT_SIZE = 40

OUTPUT_DIR = r"C:\Agent\Day8"
OUTPUT_FILENAME = "카드뉴스2.png"

MARGIN = 200  # 좌우 정렬 시 사용할 여백(px)

# ===== 카드뉴스 내용 (여기에 한글 텍스트를 채워주세요) =====
TITLE = "AI AGENT 강의"
BODY = "오늘은 파이썬 언어 이론과 라이브러리에 대해 학습하겠습니다."

# 정렬 방식: "left", "center", "right" 중 선택
TITLE_ALIGN = "left"
BODY_ALIGN = "left"


def line_x(w, align):
    if align == "left":
        return MARGIN
    if align == "right":
        return WIDTH - MARGIN - w
    return (WIDTH - w) / 2  # center


def draw_card():
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)

    title_font = ImageFont.truetype(TITLE_FONT_PATH, TITLE_FONT_SIZE)
    body_font = ImageFont.truetype(BODY_FONT_PATH, BODY_FONT_SIZE)

    # 제목 그리기 (TITLE_ALIGN 정렬, 줄바꿈)
    title_lines = textwrap.wrap(TITLE, width=14)
    y = 300
    for line in title_lines:
        bbox = draw.textbbox((0, 0), line, font=title_font)
        w = bbox[2] - bbox[0]
        draw.text((line_x(w, TITLE_ALIGN), y), line, font=title_font, fill=TITLE_COLOR)
        y += (bbox[3] - bbox[1]) + 20

    # 본문 그리기 (BODY_ALIGN 정렬, 줄바꿈)
    body_lines = textwrap.wrap(BODY, width=24)
    y += 60
    for line in body_lines:
        bbox = draw.textbbox((0, 0), line, font=body_font)
        w = bbox[2] - bbox[0]
        draw.text((line_x(w, BODY_ALIGN), y), line, font=body_font, fill=BODY_COLOR)
        y += (bbox[3] - bbox[1]) + 15

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output_path = os.path.join(OUTPUT_DIR, OUTPUT_FILENAME)
    img.save(output_path)
    print(f"저장 완료: {output_path}")


if __name__ == "__main__":
    draw_card()
