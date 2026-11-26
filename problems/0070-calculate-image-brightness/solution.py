
def calculate_brightness(img):
    # Write your code here
    if not img :
        return -1
    count = 0
    total = 0
    for row in img:
        if len(row) != len(img[0]) :
            return -1
        for pixel in row:
            if not 0 <= pixel <= 255 :
                return -1
            total += pixel
            count += 1
    ans = total / count
    return ans
    