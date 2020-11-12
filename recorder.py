import datetime
from pynput import mouse
from pynput import keyboard

def on_click(x, y, button, pressed):
    if pressed:
        today = datetime.date.today()
        detfile = open('/home/th/WORKDIR/heatmap/records/{}_{}_{}.txt'.format(today.day, today.month, today.year), 'a',)
        print('{0} at {1}'.format('Pressed', (x, y)))
        x = str(x)
        y = str(y)
    
        coord = x+" "+y+"\n"
        detfile.write(coord)
        detfile.close()

with mouse.Listener(on_click=on_click) as listener:
        listener.join()
