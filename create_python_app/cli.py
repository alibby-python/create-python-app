# app.py
import os
import sys
import time
from pathlib import Path

from create_python_app.core.metadata import save_project_metadata
from create_python_app.core.project import create_project_files, create_project_folders
from create_python_app.core.venv import create_venv
from create_python_app.core.vscode import install_vscode_extensions
from create_python_app.ui.confirms import confirm
from create_python_app.ui.spinner import Spinner
from create_python_app.ui.utils import apply_markup
from create_python_app.wizard.panels import (
    show_project_details,
    show_setup_summary,
    show_welcome,
)
from create_python_app.wizard.prompts import (
    get_editor,
    get_plugins,
    get_project_directory,
    get_project_name,
)


def main():
    """
    Main entry point for the Create-Python-App setup wizard.

    This script guides the user through:
      1. Naming their project.
      2. Choosing a directory for it.
      3. Selecting their preferred editor.
      4. Picking optional plugins/extensions.
      5. Creating a Python virtual environment.
      6. Saving configuration metadata.

    All user-facing prompts use create-python-app's built-in terminal UI components, providing a consistent interactive CLI experience without external prompt dependencies.
    """

    try:
        # --- STEP 1: Display Welcome Panel ---
        print(" ")
        show_welcome()

        # --- STEP 2: Ask for Project Name ---
        """
        Wizard Step:
            project_name

        Description:
            The name of your new Python project; this will also
            form the base of the virtual environment.

        Type:
            string

        Default:
            my-python-app

        Example:
            my-cool-app
        """
        project_name = get_project_name()

        # --- STEP 3: Set Default Project Directory ---
        """
        Wizard Step:
            project_dir

        Description:
            Where the new project should be created.
            Defaults to the root of the current drive plus the
            project name.

        Type:
            string

        Default:
            C:\\my-python-app

        Example:
            C:\\Projects\\my-cool-app
        """
        default_project_path = os.path.join(
            os.path.splitdrive(os.getcwd())[0] + os.sep, project_name
        )
        project_dir = Path(get_project_directory(default_project_path))

        # --- STEP 4: Detect and Select Editor ---
        """
        Wizard Step:
            editor

        Description:
            Choose your preferred editor for this project.
            VSCode is auto-detected if available.

        Type:
            string

        Options:
            VSCode
            PyCharm
            Vim
            Other

        Example:
            VSCode
        """
        default_editor = "VSCode" if os.getenv("VSCODE_GIT_IPC_HANDLE") else "Other"
        editor = get_editor(default_editor=default_editor)

        # --- STEP 5: Select Optional Plugins ---
        """
        Wizard Step:
            plugins

        Description:
            Pick optional editor extensions to install.
            Currently available when VSCode is selected.

        Type:
            array[string]

        Example:
            Pylance
            Jupyter
        """
        print(" ")
        plugins, plugin_data = get_plugins(editor)
        print(" ")

        # --- STEP 6: Show Summary Before Confirmation ---
        """
        Wizard Step:
            confirmation

        Description:
            Displays a summary of the selected options and
            requests confirmation before project generation
            begins.

        Type:
            boolean

        Default:
            true

        Example:
            Yes
        """
        print(" ")
        show_project_details(
            project_name=project_name,
            project_dir=project_dir,
            editor=editor,
            plugins=plugins,
        )

        # Confirm step — returns bool
        is_confirm = confirm(
            "Does this look correct?",
            default=True,
        )

        # Minor delay ensures smooth terminal rendering after prompt interaction
        print(end="")
        time.sleep(0.05)  # 50 ms pause to flush input buffer

        if not is_confirm:
            print(apply_markup("\n{red}❌ Setup cancelled by user.{/red}\n"))
            return

        # --- STEP 7: Create Virtual Environment ---
        """
        Wizard Step:
            create_virtual_environment

        Description:
            Creates a Python virtual environment for the
            new project.

        Type:
            operation

        Result:
            .venv
        """
        with Spinner("Creating virtual environment..."):
            venv_path = create_venv(project_dir)

        # --- STEP 7B: Create Standard Project Structure ---
        """
        Wizard Step:
            create_project_folders

        Description:
            Creates the standard project directory structure,
            including source code, tests, and documentation
            folders.

        Type:
            operation

        Folders:
            src
            tests
            docs
        """
        create_project_folders(project_dir, project_name)

        # --- STEP 7C: Create Base Project Files ---
        """
        Wizard Step:
            create_project_files

        Description:
            Creates the initial project files required for
            development.

        Type:
            operation
        """
        create_project_files(project_dir, project_name)

        # --- STEP 8: Install VSCode Extensions (if applicable) ---
        """
        Wizard Step:
            vscode_plugins

        Description:
            Installs selected VSCode extensions
            automatically.

        Type:
            array[string]

        Example:
            Pylance
            Python Debugger
        """
        if editor == "VSCode" and plugins:
            print(" ")
            install_vscode_extensions(plugins, plugin_data)

        # --- STEP 9: Save Metadata ---
        """
        Wizard Step:
            save_metadata

        Description:
            Saves the selected configuration options
            to a JSON file for future reference.

        Type:
            object

        Fields:
            project_name
            project_path
            editor
            plugins
            venv_path
        """
        save_project_metadata(
            {
                "project_name": project_name,
                "project_path": project_dir,
                "editor": editor,
                "plugins": plugins,
                "venv_path": venv_path,
            },
            project_dir,
        )

        # --- STEP 10: Final Setup Summary ---
        """
        Wizard Step:
            setup_summary

        Description:
            Displays a final summary of the completed
            project configuration.

        Type:
            object

        Fields:
            project_name
            project_path
            editor
            plugins
            venv_path
        """
        show_setup_summary(
            project_name=project_name,
            project_dir=project_dir,
            editor=editor,
            plugins=plugins,
            venv_path=venv_path,
        )

        # --- STEP 11: Next Steps Guidance ---
        """
        Wizard Step:
            next_steps

        Description:
            Displays guidance on activating the virtual
            environment, opening the project, and
            beginning development.

        Type:
            object

        Fields:
            project_path
            venv_path
            editor
        """
        editor_commands = {"VSCode": "code .", "Cursor": "cursor .", "Vim": "vim ."}

        open_command = editor_commands.get(editor)

        print(apply_markup("\n{bold}🚀 Next Steps{/bold}\n"))

        print(
            apply_markup(
                "{blue}{bold}1.{/bold}{/blue} Change into your project directory:"
            )
        )
        print(apply_markup(f"{{cyan}}cd {project_dir}{{/cyan}}"))
        print()

        print(
            apply_markup(
                "{blue}{bold}2.{/bold}{/blue} Activate the virtual environment"
            )
        )
        print(
            apply_markup(f"{{cyan}}{Path(venv_path).name}\\Scripts\\activate{{/cyan}}")
        )
        print()

        if open_command:
            print(
                apply_markup(
                    f"{{blue}}{{bold}}3.{{/bold}}{{/blue}} Open the project in {editor}:"
                )
            )
            print(apply_markup(f"{{cyan}}{open_command}{{/cyan}}"))
        else:
            print("Open the project using your preferred editor.")
        print()

        print(apply_markup("{green}{bold}Happy coding! 🚀{/bold}{/green}\n"))

    except KeyboardInterrupt:
        # Graceful exit if user cancels with Ctrl+C
        print(apply_markup("\n\n{red}❌ Setup cancelled by user.{/red}\n"))
        sys.exit(0)


if __name__ == "__main__":
    # Entry point guard to prevent auto-execution on import
    main()
