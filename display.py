datas = [
    [2, 3, 2.7, 3.2, 4.1],
    [10, 14, 12, 15, 20],
    [4, 5, 6, 7, 8]
]

from Tkinter import *

CANVAS_WIDTH, CANVAS_HEIGHT = 900, 500

master = Tk()

canvas = Canvas(master, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, cursor='crosshair')
canvas.pack()

LEFT, RIGHT = 100, CANVAS_WIDTH - 100
BOTTOM, TOP = CANVAS_HEIGHT - 100, 100

def draw_y_axes(min, max):
    dy = float(BOTTOM - TOP) / 4
    dval = float(max - min) / 4
    for i in range(5):
        canvas.create_text(LEFT - 10, BOTTOM - (i * dy), text=round(min + (i * dval), 2), anchor=E)
        canvas.create_line(LEFT, BOTTOM - (i * dy), RIGHT, BOTTOM - (i * dy), dash=(4,4))

def draw_point(graph_x, graph_y, set_n):
    r = 5
    (x, y) = graph_to_canvas((graph_x, graph_y))
    canvas.create_oval(x - r, y - r, x + r, y + r, fill=color(set_n))

def color(n):
    colors = ['blue', 'red', 'green', 'cyan', 'magenta']
    return colors[n % len(colors)]

shared = {}

def graph_to_canvas(graph_coord):
    return (LEFT + (graph_coord[0] * shared['di']), BOTTOM - ((graph_coord[1] - shared['min_val']) * shared['scale']))

def plot_datas(datas):
    max_len = max([len(data) for data in datas])
    shared['di'] = float(RIGHT - LEFT) / (max_len - 1)
    shared['max_val'] = max([val for data in datas for val in data])
    shared['min_val'] = min([val for data in datas for val in data])
    shared['scale'] = float(BOTTOM - TOP) / (shared['max_val'] - shared['min_val'])

    draw_y_axes(shared['min_val'], shared['max_val'])

    for n, data in enumerate(datas):
        for i, val in enumerate(data):
            draw_point(i, val, n)

plot_datas(datas)

mainloop()
