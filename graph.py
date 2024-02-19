from PIL import Image, ImageDraw
from math import floor

def create_graph_paper(width, height, sections, subsections, padding):
    # Create a white background image
    
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
                # print(x," ",y)
                line_width = 3
                if x%5 == 0:
                    line_width = 4
            # if x == sections:
            #     pos = pos - 2
            #     line_width = 4
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
                # print(x," ",y)
                line_width = 3
                if x%5 == 0:
                    line_width = 4
            # if x == sections:
            #     pos = pos - 2
            #     line_width = 4
            print("Pos: ", pos, " LineWidth: ", line_width)
            draw.line([(pos, padding), (pos, height + padding)], fill="white", width=line_width)
            if x == sections:
                break

    return image

#sm - 640px -   
#md -768  
#lg-1024  
#xl-1280  
#2xl-1536

sections = 10
subsections = 10

# Define the dimensions of the graph paper, the spacing between lines, and the line style
paper_width = 640  # Width of the image in pixels
paper_height = 1280  # Height of the image in pixels
padding = 0
# line_spacing = paper_width // sections  # Spacing between lines in pixels
# Create the graph paper image
graph_paper = create_graph_paper(paper_width, paper_height, sections, subsections, padding)
# Save the image
graph_paper.save("graph_paper_sm.png")

paper_width = 768
paper_height = 1280
padding = 4
graph_paper = create_graph_paper(paper_width, paper_height, sections, subsections, padding)
graph_paper.save("graph_paper_md.png")

paper_width = 1024
paper_height = 1280  
padding = 12
graph_paper = create_graph_paper(paper_width, paper_height, sections, subsections, padding)
graph_paper.save("graph_paper_lg.png")

paper_width = 1280
paper_height = 1280  
padding = 10
graph_paper = create_graph_paper(paper_width, paper_height, sections, subsections, padding)
graph_paper.save("graph_paper_xl.png")

paper_width = 1536
paper_height = 1280  
padding = 8
graph_paper = create_graph_paper(paper_width, paper_height, sections, subsections, padding)
graph_paper.save("graph_paper_2xl.png")


# Display the image (optional)
#graph_paper.show()
