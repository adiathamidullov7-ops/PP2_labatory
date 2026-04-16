from pathlib import Path
from clock import MickeyClock


def main():
    image_path = Path(__file__).with_name("mickey_converted.png")
    app = MickeyClock(str(image_path), width=900, height=900)
    app.run()


if __name__ == "__main__":
    main()