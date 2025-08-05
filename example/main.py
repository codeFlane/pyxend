from pyxend import Extension, ModalType

ext = Extension()

@ext.command("show_context", "Show context data")
def show_context(context):
    msg = "\n".join([
        f"📄 File: {context.get('file_path')}",
        f"🔤 Language: {context.get('language')}",
        f"📍 Cursor: {context.get('cursor_pos')}",
        f"📝 Selected: {context.get('selected_text')}",
        f"🧾 All Text Length: {len(context.get('all_text', ''))}",
        f"🪪 Word at Cursor: {context.get('cursor_word')}",
        f"📚 Total Lines: {context.get('lines')}",
        f"📦 File Size: {context.get('file_size')} bytes",
    ])
    ext.show_modal(msg, type=ModalType.INFO)

@ext.command("replace_selection", "Replace selected text")
def replace_selection(context):
    ext.replace_selected_text("✅ This text replaced your selection.")

@ext.command("insert_here", "Insert text after cursor")
def insert_here(context):
    ext.insert_text("🚀 Inserted from pyxend")

@ext.command("open_file", "Open file")
def open_file(context):
    ext.open_file(r'D:\projects\pyxend\README.md')

@ext.command("move_cursor", "Move cursor start file")
def move_cursor(context):
    ext.set_cursor_pos(0, 0)

@ext.command("save_now", "Save current file")
def save_now(context):
    ext.save_file()
    ext.show_modal("File saved!", ModalType.INFO)

@ext.command("overwrite_file", "Overwrite whole file")
def overwrite_file(context):
    ext.replace_text("💣 This file was overwritten by pyxend.")

@ext.command("run_terminal", "Run echo in terminal")
def run_terminal(context):
    ext.run_terminal_command('echo Hello from pyxend!')

ext.run()
