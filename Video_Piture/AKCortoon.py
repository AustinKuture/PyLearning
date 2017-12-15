

def make_frame(t):
    surface.set_data(z = Z(t)) # Update the mathematical surface
    canvas.on_draw(None) # Update the image on Vispy's canvas
    return _screenshot((0,0,canvas.size[0],canvas.size[1]))[:,:,:3]

animation = VideoClip(make_frame, duration=1).resize(width=350)
animation.write_gif('sinc_vispy.gif', fps=20, opt='OptimizePlus')





































