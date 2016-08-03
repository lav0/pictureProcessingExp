from PIL import Image

input_file_name  = "pillow\image.jpg"
output_file_name = "pillow\output.jpg"
output_file_no_ext = "pillow\output"


def extensive_rotations():
    im = Image.open(input_file_name)
    print type(im)

    step = 5
    r = int(90 / step)
    print type(r)
    for c in range(100):
        for i in range(r):
            im = im.rotate(step)

        im = im.rotate(-90)

        im.save(output_file_no_ext + str(c) + ".jpg")


def resizing():
    im = Image.open(input_file_name)
    tenfold_less_size = tuple([x / 3 for x in im.size])
    im.thumbnail(tenfold_less_size)
    im.save(output_file_name)


def crop_box():
    im = Image.open(input_file_name)
    box = (100, 100, 400, 400)
    region = im.crop(box)
    region = region.transpose(Image.ROTATE_180)
    im.paste(region, box)
    im.save(output_file_name)


def split_and_merge():
    im = Image.open(input_file_name)
    r, g, b = im.split()
    Image.merge("RGB", (g, b, r)).save(output_file_name)


def point_in_interval(left_side, right_side, lam):
    # lam is in [0, 1] interval
    return (1 - lam) * left_side + lam * right_side

im = Image.open(input_file_name)
square_range = 100
left_top = (100, 100)
width_height = im.size
right_bottom = tuple(a - b for a, b in zip(width_height, left_top))
rgb = im.getpixel((100, 100))
print type(rgb), rgb
left_right_range = range(left_top[0], right_bottom[0])
top_bottom_range = range(left_top[1], right_bottom[1])
for i in left_right_range:
    for j in top_bottom_range:
        pixel = im.getpixel((i, j))
        index, max_value = max(enumerate(pixel), key=lambda p:p[1])
        pix_list = list(pixel)
        pix_list[index] = min(255, int(1.2 * max_value))
        what = im.putpixel((i, j), tuple(pix_list))
im.save(output_file_name)

print "finished"