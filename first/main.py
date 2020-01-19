from PIL import Image


def main():
    try:
        # Relative Path
        img = Image.open("mario.jpg")

        # Angle given
        img = img.rotate(180)

        # Saved in the same relative location
        img.save("images/rotated_picture.jpg")
    except IOError:
        pass
    print("done")

if __name__ == "__main__":
    main()
img2 = Image.open("rotated_picture.jpg")
img2.show()