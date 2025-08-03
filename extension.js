const vscode = require("vscode");
const cp = require("child_process");
const path = require("path");
const fs = require("fs");

function activate(context) {
  const runPythonCommand = (commandName) => {
    const editor = vscode.window.activeTextEditor;

    if (!editor) {
      vscode.window.showErrorMessage("[pyxend] No active editor.");
      return;
    }

    const selection = editor.selection;
    const document = editor.document;
    const selectedText = document.getText(selection) || "";
    const fullText = document.getText() || "";
    const language = document.languageId || "";
    const filePath = document.uri.fsPath || "";
    const cursorPos = selection ? { line: selection.start.line, character: selection.start.character } : null;

    const contextPayload = {
      selected_text: selectedText,
      all_text: fullText,
      language,
      file_path: filePath,
      cursor_pos: cursorPos
    };

    const scriptPath = path.join(__dirname, "main.py");
    const args = [scriptPath, commandName, JSON.stringify(contextPayload)];

    const py = cp.spawnSync("python", args, { encoding: "utf-8" });

    if (py.stderr) {
      vscode.window.showErrorMessage("[pyxend] Python stderr: " + py.stderr.trim());
      return;
    }

    let actions;
    try {
      actions = JSON.parse(py.stdout);
    } catch (e) {
      vscode.window.showErrorMessage("[pyxend] Invalid JSON from Python");
      return;
    }

    if (!Array.isArray(actions)) {
      vscode.window.showErrorMessage("[pyxend] " + (actions.error || "Unknown error"));
      return;
    }

    actions.forEach((action) => {
      const editor = vscode.window.activeTextEditor;
      const document = editor?.document;

      switch (action.action) {
        case "show_modal":
          const type = action.type || "info";
          const msg = action.message;
          if (type === "error") vscode.window.showErrorMessage(msg);
          else if (type === "warning") vscode.window.showWarningMessage(msg);
          else vscode.window.showInformationMessage(msg);
          break;

        case "replace_selected_text":
          if (!editor || !selection) {
            vscode.window.showErrorMessage("[pyxend] Cannot replace text: no selection or editor.");
            return;
          }
          editor.edit(editBuilder => {
            editBuilder.replace(selection, action.text || "");
          });
          break;

        case "insert_text":
          if (!editor) {
            vscode.window.showErrorMessage("[pyxend] Cannot insert text: no editor.");
            return;
          }
          const pos = editor.selection.active;
          editor.edit(editBuilder => {
            editBuilder.insert(pos, action.text || "");
          });
          break;

        case "open_file":
          if (!action.path) {
            vscode.window.showErrorMessage("[pyxend] Cannot open file: no path provided.");
            return;
          }
          if (!fs.existsSync(action.path)) {
            vscode.window.showErrorMessage("[pyxend] File does not exist: " + action.path);
            return;
          }
          vscode.workspace.openTextDocument(action.path).then(doc => {
            vscode.window.showTextDocument(doc);
          });
          break;

        case "set_cursor_pos":
          if (!editor) {
            vscode.window.showErrorMessage("[pyxend] Cannot set cursor: no editor.");
            return;
          }
          if (typeof action.line !== 'number' || typeof action.character !== 'number') {
            vscode.window.showErrorMessage("[pyxend] Invalid cursor position.");
            return;
          }
          const position = new vscode.Position(action.line, action.character);
          editor.selection = new vscode.Selection(position, position);
          editor.revealRange(new vscode.Range(position, position));
          break;

        case "save_file":
          if (!document) {
            vscode.window.showErrorMessage("[pyxend] Cannot save: no document.");
            return;
          }
          document.save();
          break;

        case "run_terminal_command":
          if (!action.command) {
            vscode.window.showErrorMessage("[pyxend] No terminal command provided.");
            return;
          }
          const terminal = vscode.window.createTerminal(action.terminal_name || "pyxend terminal");
          terminal.show();
          terminal.sendText(action.command);
          break;

        case "overwrite_file":
          if (!editor || !document) {
            vscode.window.showErrorMessage("[pyxend] Cannot overwrite file: editor or document missing.");
            return;
          }
          const entireRange = new vscode.Range(
            document.positionAt(0),
            document.positionAt(document.getText().length)
          );
          editor.edit(editBuilder => {
            editBuilder.replace(entireRange, action.text || "");
          });
          break;

        default:
          vscode.window.showWarningMessage("[pyxend] Unknown action: " + action.action);
      }
    });
  };

  context.subscriptions.push(
    
    vscode.commands.registerCommand("pyxendtest.get_selected_text", () => {
      runPythonCommand('get_selected_text');
    }),
    
    vscode.commands.registerCommand("pyxendtest.get_cursor_pos", () => {
      runPythonCommand('get_cursor_pos');
    }),
    
    vscode.commands.registerCommand("pyxendtest.get_language", () => {
      runPythonCommand('get_language');
    }),
    
    vscode.commands.registerCommand("pyxendtest.get_file_path", () => {
      runPythonCommand('get_file_path');
    }),
    
    vscode.commands.registerCommand("pyxendtest.get_all_text", () => {
      runPythonCommand('get_all_text');
    }),
    
    vscode.commands.registerCommand("pyxendtest.show_info_modal", () => {
      runPythonCommand('show_info_modal');
    }),
    
    vscode.commands.registerCommand("pyxendtest.show_warn_modal", () => {
      runPythonCommand('show_warn_modal');
    }),
    
    vscode.commands.registerCommand("pyxendtest.show_error_modal", () => {
      runPythonCommand('show_error_modal');
    }),
    
    vscode.commands.registerCommand("pyxendtest.replace_selected_text", () => {
      runPythonCommand('replace_selected_text');
    }),
    
    vscode.commands.registerCommand("pyxendtest.insert_text", () => {
      runPythonCommand('insert_text');
    }),
    
    vscode.commands.registerCommand("pyxendtest.open_file", () => {
      runPythonCommand('open_file');
    }),
    
    vscode.commands.registerCommand("pyxendtest.set_cursor_pos", () => {
      runPythonCommand('set_cursor_pos');
    }),
    
    vscode.commands.registerCommand("pyxendtest.save_file", () => {
      runPythonCommand('save_file');
    }),
    
    vscode.commands.registerCommand("pyxendtest.replace_all_text", () => {
      runPythonCommand('replace_all_text');
    }),
    
    vscode.commands.registerCommand("pyxendtest.run_terminal_command", () => {
      runPythonCommand('run_terminal_command');
    }),
    
  );
}

function deactivate() {}

module.exports = { activate, deactivate };