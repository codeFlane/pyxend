from pyxend import Extension, ModalType

ext = Extension()

# create commands like this:
@ext.command('get_selected_text')
def get_selected_text(context):
    ext.show_modal(context['selected_text'])

@ext.command('get_cursor_pos')
def get_cursor_pos(context):
    ext.show_modal(str(context['cursor_pos']))

@ext.command('get_language')
def get_language(context):
    ext.show_modal(context['language'])

@ext.command('get_file_path')
def get_file_path(context):
    ext.show_modal(context['file_path'])

@ext.command('get_all_text')
def get_all_text(context):
    ext.show_modal(context['all_text'])

@ext.command('show_info_modal')
def show_info_modal(context):
    ext.show_modal('info modal', ModalType.INFO)

@ext.command('show_warn_modal')
def show_warn_modal(context):
    ext.show_modal('warning modal', ModalType.WARNING)

@ext.command('show_error_modal')
def show_error_modal(context):
    ext.show_modal('error modal', ModalType.ERROR)

@ext.command('replace_selected_text')
def replace_selected_text(context):
    ext.replace_selected_text('replace selected')

@ext.command('insert_text')
def insert_text(context):
    ext.insert_text('insert')

@ext.command('open_file')
def open_file(context):
    ext.open_file(r'D:\projects\setup.py')

@ext.command('set_cursor_pos')
def set_cursor_pos(context):
    ext.set_cursor_pos(0, 0)

@ext.command('save_file')
def save_file(context):
    ext.save_file()

@ext.command('replace_all_text')
def replace_all_text(context):
    ext.replace_text('replaced all')

@ext.command('run_terminal_command')
def run_terminal_command(context):
    ext.run_terminal_command('echo hello', 'pyxend test')

ext.run()