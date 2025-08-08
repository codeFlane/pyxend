# 📄 Changelog

## 0.2.0 *New actions*
 - Added `opened_files`, `is_saved` and `workspace` in context.
 - `replace_selected_text` and `overwrite_file` JS actions are now **deprecated**. Use `replace_text` with presets instead.
 - Added `delete_selected_text`, `delete_file`, `select_range`, `close_terminal`, `open_terminal`, `run_terminal`, `switch_to_file`, `reload_editor` actions in JS (python support only 2 new actions, others support soon)
 - Added `delete_selected_text` and `delete_file` actions in Extension class
 - Added docstrings for Extension class and ModalType enums
 - Added InsertTextPreset and ReplaceTextPreset enums
 - Reworked replace_text to support replace whole file, selection, or custom position
 - Reworked insert_text to support insert at start, end, after cursor or custom position
 - Updated readme
   - Added "How it works", "Important Notes about Command Execution" and "How to Integrate a New Custom Action" sections
   - Added note that gif made when project was called pyvscode
   - Replaced `"ful"` to `"full"` in changelog section (typo fix)
   - Renamed headers in changelog section - "Latest (0.1.2)" -> "0.1.2 (Latest)"

## 0.1.2 *Rename manifest*
 - Updated readme
 - Added changelog file
 - Renamed `manifest` to `metadata` command
 - Added `cursor_word`, `lines`, `file_size` in context

## 0.1.1 *Bugfix*
 -  Added missing `templates/` directory to package (resolved setup failure).
 -  Replaced `"selcted_text"` with correct `"selected_text"` in extension template.
 -  Corrected `replace_text` call in `__init__.py` (now properly replaces entire file content).
 -  Removed redundant text after `pyxend build` command output.
 -  Added error modals for:

    - Python stderr output in extension
    - Unknown actions
    - Invalid JSON from Python
    - Incorrect cursor position
    - Missing command context
 - Added file existence check in `open_file` (shows error if path is invalid or file not found).
 - Updated readme file

## 0.1.1 *Initial*
Initial version