# 📄 Changelog

## 0.1.2 *Rename manifest*
 - Update readme
 - Add changelog file
 - Rename `manifest` to `metadata` command
 - Add `cursor_word`, `lines`, `file_size` in context

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
 -  Update readme file

## 0.1.1 *Initial*
Initial version