from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelHeader
from kivy.uix.boxlayout import BoxLayout

class MenuTabbedPanel(TabbedPanel):
    def __init__(self, **kwargs):
        super(MenuTabbedPanel, self).__init__(**kwargs)

        tab1 = TabbedPanelHeader(text='Pestaña 1')
        tab1.content = YourContentForTab1()

        tab2 = TabbedPanelHeader(text='Pestaña 2')
        tab2.content = YourContentForTab2()

        self.add_widget(tab1)
        self.add_widget(tab2)

class YourContentForTab1(BoxLayout):
    # Aquí podrías colocar la implementación del contenido para la pestaña 1
    pass  # Usamos 'pass' para indicar que no hay implementación por ahora

class YourContentForTab2(BoxLayout):
    # Aquí podrías colocar la implementación del contenido para la pestaña 2
    pass  # Usamos 'pass' para indicar que no hay implementación por ahora

class MenuApp(App):
    def build(self):
        return MenuTabbedPanel()

if __name__ == '__main__':
    MenuApp().run()
