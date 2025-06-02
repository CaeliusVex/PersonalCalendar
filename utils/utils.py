import os

def get_task(code):
    file_path = "static/task/"+str(code)
    if not os.path.exists(file_path):
        return f"File {code} not found.", 404
    with open(file_path, 'r') as file:
        content = file.read()
    return content



import datetime
from PIL import Image, ImageDraw, ImageFont
import math

cell_width = 400
cell_height = int(cell_width/8*7)
title_f = int(cell_width/10)
day_f = int(title_f/6*5)
text_f = int(day_f/4*3)
line_height = text_f

def create_calendar_with_task():
    today = datetime.date.today()
    num_days = 30
    days = list(range(1, num_days + 1))
    cols = 5
    img_width = cell_width * cols
    rows = math.ceil(num_days / cols)
    img_height = cell_height * rows 
    img = Image.new('RGB', (img_width, img_height), 'white')
    draw = ImageDraw.Draw(img)
    day_font = ImageFont.truetype("DejaVuSans.ttf", day_f) 
    task_font = ImageFont.truetype("DejaVuSans.ttf", text_f)  
    for i, day in enumerate(days):
        col = i % cols
        row = i // cols
        x = col * cell_width
        y = row * cell_height
        fill_color = 'lightblue' if day == today.day else 'white'
        draw.rectangle([x, y, x + cell_width, y + cell_height], fill=fill_color, outline='black')
        draw.text((x + int(line_height/4), y + int(line_height/4)), str(day), fill='black', font=day_font)
        task = get_task(i+1)
        max_width = cell_width - 20
        y_offset = day_f+int(line_height/2)
        for part in task.split('\n'):
            part = part.strip()
            if not part:
                continue
            words = part.split()
            current_line = []
            for word in words:
                test_line = ' '.join(current_line + [word])
                test_width = draw.textlength(test_line, font=task_font)
                if test_width <= max_width:
                    current_line.append(word)
                else:
                    if current_line:
                        if y + y_offset <= y + cell_height - 10:
                            draw.text((x + 10, y + y_offset), ' '.join(current_line), fill='black', font=task_font)
                            y_offset += line_height
                    current_line = [word]
            if current_line and y + y_offset <= y + cell_height - 10:
                draw.text((x + 10, y + y_offset), ' '.join(current_line), fill='black', font=task_font)
                y_offset += line_height
    img.save("static/calendar.png")

# print(get_task(1))
def edit_task(loc, task):
    file_path = "static/task/" + str(loc)
    if not os.path.exists(file_path):
        return f"File {loc} not found."
    
    with open(file_path, 'w') as file:
        file.write(task)
        
    create_calendar_with_task()

    return "success"