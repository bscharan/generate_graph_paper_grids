from PIL import Image, ImageDraw
from math import floor
import os


def create_graph_paper(width, height, sections, subsections, padding):
      
    image = Image.new("RGB", (width, height), "black")
    draw = ImageDraw.Draw(image)

    width = width - 2*padding
    height = height - 2*padding

    major_gap = width/sections
    minor_gap = major_gap/subsections

    # Draw horizontal lines
    pos = 0
    x = 0
    while pos < height:
        for y in range (0, subsections):
            line_width = 1
            pos = floor(padding + x*major_gap + y*minor_gap)
            if y%5 == 0 and y!=0:
                pos = pos - 1
                line_width = 2
            if y == 0:
                pos = pos - 2
                line_width = 3
                if x%5 == 0:
                    line_width = 4
            draw.line([(padding, pos), (width + padding , pos)], fill="white", width=line_width)
        x = x + 1
            
    # Draw vertical lines
    for x in range(0, sections + 1):
        for y in range (0, subsections):
            line_width = 1
            pos = floor(padding + x*major_gap + y*minor_gap)
            if y%5 == 0 and y!=0:
                pos = pos - 1
                line_width = 2
            if y == 0:
                pos = pos - 2
                line_width = 3
                if x%5 == 0:
                    line_width = 4
            # print("Pos: ", pos, " LineWidth: ", line_width)
            draw.line([(pos, padding), (pos, height + padding)], fill="white", width=line_width)
            if x == sections:
                break

    return image


directory = "./output"
if not os.path.exists(directory):
    os.makedirs(directory)


# TODO Add def dotted_line(): to create a dotted line.


def generate_graph(width, height, padding, sections, subsections, tag):
    graph_paper = create_graph_paper(width, height, sections, subsections, padding)
    graph_paper.save(f"./output/graph_paper_{tag}.png")

generate_graph(640, 1000, 10, 10, 10, "sm")
generate_graph(768, 1000, 4, 10, 10, "md")
generate_graph(1024, 1280, 12, 10, 10, "lg")
generate_graph(1280, 1280, 10, 10, 10, "xl")
generate_graph(1536, 1280, 8, 10, 10, "2xl")

