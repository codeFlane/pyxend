from pyxend import Extension, ModalType, InsertTextPreset, ReplaceTextPreset

ext = Extension()

@ext.command("show_context", "Show context data")
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

@ext.command("replace_selection", "Replace selected text")
def replace_selection(context):
    ext.replace_text("✅ This text replaced your selection.", preset=ReplaceTextPreset.SELECTED)

@ext.command("insert_here", "Insert text after cursor")
def insert_here(context):
    ext.insert_text("🚀 Inserted from pyxend", preset=InsertTextPreset.CURSOR)

@ext.command("insert_start", "Insert at start")
def insert_start(context):
    ext.insert_text("🔝 Top of file\n", preset=InsertTextPreset.START)

@ext.command("insert_end", "Insert at end")
def insert_end(context):
    ext.insert_text("\n🔚 Bottom of file", preset=InsertTextPreset.END)

@ext.command("replace_all", "Replace entire file")
def replace_all(context):
    ext.replace_text("💣 This file was overwritten by pyxend.", preset=ReplaceTextPreset.ALL)

@ext.command("replace_custom", "Replace custom range")
def replace_custom(context):
    ext.replace_text("🧪 Replaced in range", preset=ReplaceTextPreset.CUSTOM,
                     start_line=0, start_character=0,
                     end_line=0, end_character=5)

@ext.command("open_file", "Open file")
def open_file(context):
    ext.open_file(r"D:\projects\pyxend\README.md")

@ext.command("move_cursor", "Move cursor start file")
def move_cursor(context):
    ext.set_cursor_pos(0, 0)

@ext.command("save_now", "Save current file")
def save_now(context):
    ext.save_file()
    ext.show_modal("File saved!", ModalType.INFO)

@ext.command("run_terminal", "Run echo in terminal")
def run_terminal(context):
    ext.run_terminal_command("echo Hello from pyxend!")

@ext.command("delete_text", "Delete selected text")
def delete_text(context):
    ext.delete_selected_text()

@ext.command("delete_file", "Delete current file")
def delete_file(context):
    ext.delete_file()

ext.run()