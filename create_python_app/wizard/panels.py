from create_python_app.ui.panels import panel
from create_python_app.ui.utils import apply_markup


def show_welcome() -> None:
    """
    Display the Create Python App welcome panel.

    Presents the initial setup wizard screen
    shown when the application starts.
    """
    panel(
        title="🐞 Setup Wizard",
        content="{magenta}Welcome to create-python-app!{/}",
        width=70,
        title_bg="magenta",
        title_fg="white",
        border_style="magenta",
        padding=1,
    )


def show_project_details(
    project_name,
    project_dir,
    editor,
    plugins,
) -> None:
    """
    Display the selected project configuration.

    Args:
        project_name:
            Name of the project.
    
        project_dir:
            Target project directory.
        
        editor:
            Selected editor.
    
        plugins:
            List of selected plugins.
    """    
    panel(
        title="📦 Project Details",
        content=(
            f"{{bold}}Project:{{/bold}} "
            f"{{cyan}}{project_name}{{/cyan}}\n"
            f"{{bold}}Location:{{/bold}} "
            f"{{green}}{project_dir}{{/green}}\n"
            f"{{bold}}Editor:{{/bold}} "
            f"{{magenta}}{editor}{{/magenta}}\n"
            f"{{bold}}Plugins:{{/bold}} "
            f"{', '.join(plugins) if plugins else 'none'}"
        ),
        border_style="cyan",
        title_bg="cyan",
        title_fg="white",
        width=70,
    )


def show_setup_summary(
    project_name,
    project_dir,
    editor,
    plugins,
    venv_path,
) -> None:
    """
    Display the final setup summary.

    Shows the completed project configuration,
    including the virtual environment location.

    Args:
        project_name:
            Name of the project.

        project_dir:
            Project location.

        editor:
            Selected editor.

        plugins:
            Installed or selected plugins.

        venv_path:
            Path to the created virtual environment.
    """
    print(
        apply_markup(
            "\n{green}{bold}✅ Setup complete!{/bold}{/green}"
        )
    )

    print(
        apply_markup(
            "\nYour Python project is ready to go.\n"
        )
    )

    panel(
        title="📦 Setup Summary",
        content=(
            f"{{bold}}Project:{{/bold}} "
            f"{{cyan}}{project_name}{{/cyan}}\n"
            f"{{bold}}Location:{{/bold}} "
            f"{{green}}{project_dir}{{/green}}\n"
            f"{{bold}}Editor:{{/bold}} "
            f"{{magenta}}{editor}{{/magenta}}\n"
            f"{{bold}}Plugins:{{/bold}} "
            f"{', '.join(plugins) if plugins else 'none'}\n"
            f"{{bold}}Virtual env:{{/bold}} "
            f"{{blue}}{venv_path}{{/blue}}"
        ),
        title_bg="cyan",
        title_fg="white",
        border_style="cyan",
        width=70,
    )