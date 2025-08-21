from pyxend import Extension, ModalType, InsertTextPreset, ReplaceTextPreset, Event

ext = Extension()

@ext.command("show_context", "Show context")
def show_context(context):
    msg = (f"File: {context['file_path']}"
        f"Language: {context['language']}"
        f"Cursor: {context['cursor_pos']}"
        f"Selected: {context['selected_text']}"
        f"Word at Cursor: {context['cursor_word']}"
        f"Total Lines: {context['lines']}"
        f"File Size: {context['file_size']} bytes"
        f"Saved: {context['is_saved']}"
        f"Opened files: {context['opened_files']}"
        f"Workspace folder: {context['workspace']}")
    ext.show_modal(msg, type=ModalType.INFO)

@ext.command('show_info_modal', 'Show info modal')
def show_info_moadl(context):
    ext.show_modal('Info modal')

@ext.command('show_warn_modal', 'Show warn modal')
def show_warn_moadl(context):
    ext.show_modal('Warn modal', type=ModalType.WARNING)

@ext.command('show_error_modal', 'Show error modal')
def show_error_moadl(context):
    ext.show_modal('Error modal', type=ModalType.ERROR)

@ext.command("replace_selection", "Replace selected text")
def replace_selection(context):
    ext.replace_text("Replace selected text", preset=ReplaceTextPreset.SELECTED)

@ext.command("insert_here", "Insert text after cursor")
def insert_here(context):
    ext.insert_text("Insert after cursor", preset=InsertTextPreset.CURSOR)

@ext.command("insert_start", "Insert at start")
def insert_start(context):
    ext.insert_text("Insert at start file", preset=InsertTextPreset.START)

@ext.command("insert_end", "Insert at end")
def insert_end(context):
    ext.insert_text("Insert at end file", preset=InsertTextPreset.END)

@ext.command("replace_all", "Replace all text")
def replace_all(context):
    ext.replace_text("Replace all text", preset=ReplaceTextPreset.ALL)

@ext.command("replace_custom", "Replace at custom pos")
def replace_custom(context):
    ext.replace_text("Replaced at custom position", preset=ReplaceTextPreset.CUSTOM, start_line=0, start_character=0, end_line=0, end_character=5)

@ext.command("open_file", "Open file")
def open_file(context):
    ext.open_file(r"D:\projects\pyxend\README.md")

@ext.command("move_cursor", "Set cursor pos")
def move_cursor(context):
    ext.set_cursor_pos(0, 0)

@ext.command("save_now", "Save file")
def save_now(context):
    ext.save_file()

@ext.command("run_terminal", "Run terminal")
def run_terminal(context):
    ext.run_terminal_command("echo Hello")

@ext.command("delete_text", "Delete selected text")
def delete_text(context):
    ext.delete_selected_text()

@ext.command("delete_file", "Delete file")
def delete_file(context):
    ext.delete_file()

@ext.command('select_range', 'Select range')
def select_range(context):
    ext.select_range(0, 1, 0, 5)

@ext.command('reload_editor', 'Reload editor')
def reload_editor(context):
    ext.reload_editor()

@ext.command('status_message', 'Show status message')
def status_message(context):
    ext.status_message('Hello from Pyxend!')

@ext.event(Event.STARTUP)
def startup(context):
    ext.show_modal('extension startup')

@ext.event(Event.CHANGE)
def change(context):
    ext.show_modal('file changed')

@ext.event(Event.SHUTDOWN)
def shutdown(context):
    ext.show_modal('extension shutdown')

ext.run()