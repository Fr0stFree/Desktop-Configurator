import PySimpleGUI as GUI

from . import settings


class GraphicalUserInterface:
    GUI.theme('LightGrey1')
    GUI.set_options(font='Franklin 10')

    def __init__(self):
        self.load_data_btn = GUI.Button('Загрузить', key='-LOAD_DATA-', size=settings.BUTTON_SIZE)
        self.file_path_title = GUI.Text('Файл')
        self.file_path = GUI.Multiline(key='-FILE_NAME_OUTPUT-', disabled=True, size=(30,3),
                                       reroute_stdout=True, autoscroll=True, no_scrollbar=True,
                                       expand_x=True)
        self.min_row_title = GUI.Text('Начальная строка')
        self.min_row_input = GUI.InputText(key='-MIN_ROW-', size=settings.BUTTON_SIZE,
                                           default_text=None, enable_events=True)
        self.max_row_title = GUI.Text('Конечная строка')
        self.max_row_input = GUI.InputText(key='-MAX_ROW-', size=settings.BUTTON_SIZE,
                                           default_text=None, enable_events=True)
        self.error_counter_title = GUI.Text('Число ошибок')
        self.error_counter = GUI.Multiline(key='-ERROR_COUNTER-', size=(9,1),
                                           disabled=True, reroute_stdout=True, autoscroll=False,
                                           no_scrollbar=True, expand_x=True, do_not_clear=False)
        self.event_box = GUI.Multiline(key='-OUTPUT-', disabled=True, size=settings.EVENT_BOX_SIZE,
                                       reroute_stdout=True, autoscroll=True, no_scrollbar=True,
                                       expand_x=True, expand_y=True)
        self.process_data_btn = GUI.Button(button_text='Обработать', key='-PROCESS_DATA-',
                                           size=settings.BUTTON_SIZE, disabled=True)
        self.stop_process_btn = GUI.Button(button_text='Стоп', key='-STOP_PROCESS-',
                                           size=settings.BUTTON_SIZE, disabled=True)
        self.save_data_btn = GUI.Button(button_text='Сохранить', key='-SAVE_DATA-',
                                        size=settings.BUTTON_SIZE, disabled=True)
        self.progress_bar = GUI.ProgressBar(max_value=100, key='-PROGRESS_BAR-',
                                            size=settings.PROGRESS_BAR_SIZE, expand_x=True)

        menu = GUI.Menu([
            ['Разное', 'Об авторе'],
            ['Инструкция', 'Клик']
        ])
        layout = [
            [menu],
            [self.file_path_title, self.file_path, self.load_data_btn],
            [self.min_row_title, self.min_row_input, self.max_row_title, self.max_row_input, self.error_counter_title, self.error_counter, GUI.Push()],
            [self.event_box],
            [self.progress_bar],
            [self.process_data_btn, self.stop_process_btn, GUI.Push(), self.save_data_btn],
        ]
        self.window = GUI.Window(title=settings.WINDOW_TITLE, layout=layout,
                                 size=settings.WINDOW_SIZE)
