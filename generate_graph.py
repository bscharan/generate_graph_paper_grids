import argparse, sys, os

from PIL import Image, ImageDraw
from math import floor

width=0
height=0
sections=0
sunsections=0
padding=0
tag=0
# runDefaultFlag = False

def parse_Arguments():
    global width, height, sections, subsections, padding, tag

    parser=argparse.ArgumentParser(description='Generate graph paper.')
    # parser.add_argument('-d',"--default", action="store", help='run with default config, other parameters are ignored')
    parser.add_argument("--width",action="store", default=1024, type=int, help="Width of the page in pixels, DefaultVaule: 1024")
    parser.add_argument("--height",action="store", default=1024, type=int, help="height of the page in pixels, DefaultVaule: 1024")
    parser.add_argument("--sections",action="store", default=10, type=int, help="number of section, the width should be divided, DefaultVaule: 10")
    parser.add_argument("--subsections",action="store", default=10, type=int, help="number of subsections each section should be divided, DefaultVaule: 10")
    parser.add_argument("--padding",action="store", default=12, type=int, help="outer margins width in pixels for the graph, , DefaultVaule: 12")
    parser.add_argument("--tag",action="store", default="default", help="suffix for output file name, DefaultVaule: default")
    args=parser.parse_args()

    
    if args.width:
        width = args.width
    
    if args.height:
        height = args.height
    
    if args.sections:
        sections = args.sections
    
    if args.subsections:
        subsections = args.subsections

    if args.padding:
        padding = args.padding
    
    if args.tag:
        tag = args.tag
    

def create_graph_paper(width, height, sections, subsections, padding):
      
    image = Image.new("RGB", (width, height), "black")
    draw = ImageDraw.Draw(image)

    width = width - 2*padding
    height = height - 2*padding

    major_gap = width/sections
    minor_gap = major_gap/subsections

    # Draw horizontal lines
    top_padding = 10
    pos = 0
    x = 0
    while pos < height:
        for y in range (0, subsections):
            line_width = 1
            pos = floor(top_padding + x*major_gap + y*minor_gap)
            if y%5 == 0 and y!=0:
                pos = pos - 1
                line_width = 2
            if y == 0:
                pos = pos - 2
                line_width = 3
                if x%5 == 0:
                    line_width = 4
            draw.line([(padding, pos), (width + padding , pos)], fill="#36454f", width=line_width)
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
            draw.line([(pos, top_padding), (pos, height + top_padding)], fill="#36454f", width=line_width)
            if x == sections:
                break

    return image




# TODO Add def dotted_line(): to create a dotted line.


def generate_graph(width, height, padding, sections, subsections, tag):
    graph_paper = create_graph_paper(width, height, sections, subsections, padding)
    graph_paper.save(f"./output/{tag}_graph_paper.png")

def runDefault():
    
    generate_graph(640, 1000, 10, 10, 10, "sm")
    generate_graph(768, 1000, 9, 10, 10, "md")
    generate_graph(1024, 1280, 12, 10, 10, "lg")
    generate_graph(1280, 1280, 10, 10, 10, "xl")
    generate_graph(1536, 1280, 8, 10, 10, "2xl")

def main():
    directory = "./output"
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    if not len(sys.argv) > 1:
        print("""
        running with default config,
        generating graphs for sm,md,lg,xl,2xl sizes
        run following command to view all options
            >> python generate_graph.py -h  """)
        runDefault()
    else: 
        parse_Arguments()
        print(f"""
        creating graph with Width  = {width}, height = {height}, padding = {padding},
        sections = {sections}, subsections = {subsections}, output_file = ./output/{tag}_graph_paper.png""")
        generate_graph(width, height, padding, sections, subsections, tag)


main()

