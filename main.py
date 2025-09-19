from PIL import Image

def main():
    # TODO: Change to command-line argument
    input_file = input("Type image name: ").strip()

    # https://stackoverflow.com/a/74186686/11009466
    charset = " `.-':_,^=;><+!rc*/z?sLTv)J7(|Fi{C}fI31tlu[neoZ5Yxjya]2ESwqkP6h9d4VpOGbUAKXHm8RD#$Bg0MNWQ%&@"
    
    def remap(num):
        # TODO: fix contrast to be from min(pixels) to max(pixels) instead of 0-255
        index = round(num / 255 * (len(charset) - 1))
        return charset[index]
    
    with Image.open(input_file).convert("L") as img: # convert("L") makes it grayscale
        
        # Resize so that the height of images aren't distorted by the height of a character
        width, height = img.size
        im_resized = img.resize((width, int(height*0.47085201793))) # Number is the ratio of height to width of a consolas font character

        width, height = im_resized.size
        pixels = list(im_resized.getdata())

        # divides the pixels list into a nested list, each element is a new list that contains each row of pixels
        pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]

        with open("output.txt", "w") as f:
            for i in pixels:
                for j in i:
                    f.write(remap(j))
                f.write("\n")

if __name__ == "__main__":
    main()