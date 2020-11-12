import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.scatter import Scatter, ScatterPlane
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle, Ellipse, Line
from kivy.graphics.transformation import Matrix
from kivy.lang import Builder


class Painter(Widget):
    """
    Canvas для рисования систем
    """
    def __init__(self, **kwargs):
        super(Painter, self).__init__(**kwargs)

    def draw(self, size_x, size_y):
        self.canvas.clear()
        self.canvas.add(Color(0, 0, 0, 1))
        self.canvas.add(Rectangle(pos=(0, 0), size=(int(size_x), int(size_y))))
        self.canvas.add(Color(1, 0, 0, 1))
        self.canvas.add(Line(rectangle=(0, 0, int(size_x), int(size_y))))
        self.size = (int(size_x), int(size_y))
        with open(os.path.dirname(__file__) + "/records/input.txt", 'r') as f:
            for line in f:
                x, y = line.strip("\n").split(" ")
                point = Ellipse(pos=(int(x) - 5, int(size_y) - int(y) - 5), size=(10, 10))
                self.canvas.add(point)


class HeatmapApp(App):
    """
    Главное приложение
    """
    def __init__(self):
        super(HeatmapApp, self).__init__()
        self.settings_layout = None
        self.scatter = None
        self.draw_layout = None
        self.painter = None

    def build(self):
        self.root = BoxLayout(orientation="horizontal")
        self.settings_layout = Builder.load_file('./templates/settings.kv')

        self.draw_layout = RelativeLayout()
        self.draw_layout.canvas.before.add(Color(255, 255, 255, 1))
        self.draw_layout.canvas.before.add(Rectangle(size=(4000, 4000)))
        self.scatter = ScatterPlane()
        self.painter = Painter()
        self.scatter.add_widget(self.painter)
        self.draw_layout.add_widget(self.scatter)
        self.root.add_widget(self.draw_layout)
        self.root.add_widget(self.settings_layout)

        self.settings_layout.ids.start_mode_1.bind(
            on_press=lambda a: self.start(self.painter)
        )
        self.draw_layout.bind(
            on_touch_down=lambda obj, touch: self.scale(touch)
        )
        self.settings_layout.ids.screenshot.bind(
            on_press=lambda a: self.save()
        )



        return self.root

    def start(self, painter):
        """
        Запуск отрисовки
        """
        x = self.settings_layout.ids.x.text
        y = self.settings_layout.ids.y.text
        painter.draw(x, y)

    def scale(self, touch):
        """
        Масштабирование колесом мыши
        """
        if touch.is_mouse_scrolling:
            if self.draw_layout.size[0] > touch.pos[0]:
                if touch.button == 'scrolldown':
                    self.scale_up(touch.pos)
                elif touch.button == 'scrollup':
                    self.scale_down(touch.pos)

    def scale_up(self, anchor=None):
        """
        Увеличение
        """
        if not anchor:
            anchor = self.draw_layout.center
        self.scatter.apply_transform(Matrix().scale(1.1, 1.1, 1.1), anchor=anchor)

    def scale_down(self, anchor=None):
        """
        Уменьшение
        """
        if not anchor:
            anchor = self.draw_layout.center
        self.scatter.apply_transform(Matrix().scale(0.9, 0.9, 0.9), anchor=anchor)

    def save(self):
        self.painter.export_to_png('imgs/clickmap.png')

if __name__ == "__main__":
    HeatmapApp().run()
