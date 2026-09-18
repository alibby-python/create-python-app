from create_python_app.core.project import (
    create_project_folders,
)


def test_create_project_folders_creates_gitkeep_files(
    tmp_path,
):
    create_project_folders(
        tmp_path,
        "test-project",
    )

    assert (tmp_path / "src" / ".gitkeep").exists()
    assert (tmp_path / "tests" / ".gitkeep").exists()
    assert (tmp_path / "docs" / ".gitkeep").exists()


def test_create_project_folders_creates_directories(
    tmp_path,
):
    create_project_folders(
        tmp_path,
        "test-project",
    )

    assert (tmp_path / "src").exists()
    assert (tmp_path / "tests").exists()
    assert (tmp_path / "docs").exists()


def test_create_project_folders_creates_starter_files(
    tmp_path,
):
    create_project_folders(
        tmp_path,
        "test-project",
    )

    assert (tmp_path / "src" / "__init__.py").exists()
    assert (tmp_path / "src" / "app.py").exists()
    assert (tmp_path / "tests" / "test_sample.py").exists()
    assert (tmp_path / "docs" / "README.md").exists()


def test_create_project_folders_writes_docs_readme(
    tmp_path,
):
    create_project_folders(
        tmp_path,
        "my-app",
    )

    contents = (tmp_path / "docs" / "README.md").read_text()

    assert "Documentation for my-app" in contents


def test_create_project_files_creates_root_files(
    tmp_path,
):
    create_project_files(
        tmp_path,
        "test-project",
    )

    assert (tmp_path / "README.md").exists()
    assert (tmp_path / "requirements.txt").exists()


from create_python_app.core.project import (
    create_project_files,
)


def test_create_project_files_writes_readme(
    tmp_path,
):
    create_project_files(
        tmp_path,
        "test-project",
    )

    contents = (tmp_path / "README.md").read_text()

    assert "# test-project" in contents
    assert "Getting Started" in contents


def test_create_project_files_writes_requirements(
    tmp_path,
):
    create_project_files(
        tmp_path,
        "test-project",
    )

    contents = (tmp_path / "requirements.txt").read_text()

    assert "# Add your project dependencies here" in contents
