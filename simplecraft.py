from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

world_size = int(input('How big you want your world (bigger=slower): '))

app = Ursina()
Sky()
player = FirstPersonController()

window.title = 'Simplecraft.PY [V1.0] - by hayoto // @froggy.lul'
window.borderless = False


boxes = []
for n in range(8):
    for k in range(world_size):
        box = Button(
            parent=scene,
            model='cube',
            origin_y = 0.5,
            texture = 'white_cube',
            color = color.green,
            highlight_color = color.yellow,
            position = (k, 0, n)
        )
        boxes.append(box)

    def input(key):
        for box in boxes:
            if box.hovered:
                if key=='right mouse down':
                    newBox = Button(
                        parent=scene,
                        model='cube',
                        origin_y = 0.5,
                        texture = 'white_cube',
                        color = color.brown,
                        highlight_color = color.yellow,
                        position = box.position + mouse.normal
                    )
                    boxes.append(newBox)
                if key=='left mouse down':
                    boxes.remove(box)
                    destroy(box)

app.run()