from pynput import mouse
from pynput import keyboard

def on_click(x, y, button, pressed):
    if pressed:
        detfile=open('./records/1.txt','a',)
        print('{0} at {1}'.format('Pressed',(x, y)))
        x=str(x)
        y=str(y)
    
        coord=x+" "+y+"\n"
        detfile.write(coord)
        detfile.close()
        
with mouse.Listener(on_click=on_click) as listener:
        listener.join()
