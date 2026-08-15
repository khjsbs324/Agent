import os
import qrcode

TEXT = "https://example.com"
OUTPUT_DIR = r"C:\Agent\Day8\output"
OUTPUT_FILENAME = "basic-qr.png"


def create_qr():
    img = qrcode.make(TEXT)

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output_path = os.path.join(OUTPUT_DIR, OUTPUT_FILENAME)
    img.save(output_path)
    print(f"저장 완료: {output_path}")


if __name__ == "__main__":
    create_qr()
