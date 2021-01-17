import simple_draw as sd


def bubble(point, step):
    radius = 50
    for _ in range(7):
        radius += step
        sd.circle(center_position=point, radius=radius, width=2)


for x in range(100,700,100):
    point = sd.get_point(x,100)
    bubble(point=point, step=5)