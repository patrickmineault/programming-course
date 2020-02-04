import csv
import random

background_color = 32
text_color = 255

def setup():
    global columns
    file = open("data/aggregate_montreal_climate.csv", 'r')
    reader = csv.reader(file, quoting=csv.QUOTE_NONNUMERIC)
    header = reader.next()
    columns = {}
    for colname in header:
        columns[colname] = []
    print(header)
    for row in reader:
        for i in range(len(row)):
            columns[header[i]].append(row[i])
    file.close()
    size(800, 800)
    background(background_color)
    
def draw():
    global columns
    
    idx = frameCount % len(columns['year'])
    if idx == 0:
        background
        return
    
    noStroke()
    fill(background_color, background_color, background_color, 5)
    rect(0, 0, width, height)
    strokeWeight(0)
    
    
    #print(columns['year'][idx])
    pushMatrix()
    translate(0, height)
    scale(1, -1)
    translate(width * .05, width * .05)
    scale(.9, .9)
    
    colname = 'cold_days'
    the_col = columns[colname]
    bottom_range = min(the_col)
    top_range = max(the_col)
    left_range = min(columns['year'])
    right_range = max(columns['year'])
    
    current_year = columns['year'][idx]
    frac_t = (current_year - left_range) / (right_range - left_range)
    stroke(frac_t * 255, 
           192, 
           (1 - frac_t) * 255) 
    
    scale(width / (right_range - left_range), height / (top_range - bottom_range))
    translate(-left_range, -bottom_range)
    
    for i in range(3):
        line(columns['year'][idx-1],
            the_col[idx-1],
            columns['year'][idx],
            the_col[idx])
    popMatrix()
    
    noStroke()
    fill(background_color)
    rect(0, 0, width, 50)
    fill(text_color)
    textSize(30)
    textAlign(CENTER)
    fill(background_color)
    rect(0, height - 50, width, 50)
    fill(text_color)
    text(int(columns['year'][idx]), width / 2, height - 20)
    textAlign(CENTER)
    text(colname, width/2, 30)
