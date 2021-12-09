import arcade



COLUMN = 20
ROW = 20
LEFT = 110
BOTTOM = 110
arcade.open_window(400, 400, 'arc Color')
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()



for row in range(10):
    for col in range(10):
        x = col * COLUMN + LEFT
        y = row * ROW + BOTTOM
        if (row+col) % 2 == 0:
            arcade.draw_rectangle_filled(x, y, 10, 10, arcade.color.RED, 45)
        else:
            arcade.draw_rectangle_filled(x, y, 10, 10, arcade.color.BLUE, 45)
            
            
            
arcade.finish_render()
arcade.run()