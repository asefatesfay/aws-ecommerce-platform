"""
pathlib — Object-oriented filesystem paths (Python 3.4+).
os.path — Legacy path utilities (included for comparison).

pathlib covered:
  Path construction       — absolute, relative, home, cwd, joining
  Path attributes         — .name, .stem, .suffix, .suffixes, .parent, .parts, .drive
  Navigation              — /  operator, .parent, .parents, .relative_to()
  Type checks             — .exists(), .is_file(), .is_dir(), .is_symlink()
  File content I/O        — .read_text(), .write_text(), .read_bytes(), .write_bytes()
  Directory operations    — .mkdir(), .rmdir(), .iterdir(), .glob(), .rglob()
  File operations         — .touch(), .unlink(), .rename(), .replace(), .stat()
  Metadata                — .stat().st_size, .st_mtime, .owner() (Unix)
  Introspection           — .resolve(), .expanduser(), .is_absolute()
  Iteration patterns      — glob with patterns, recursive rglob, filtering
  Practical use cases     — project structure discovery, log rotation, config files
"""

import os
import stat
import time
import tempfile
from pathlib import Path, PurePath, PurePosixPath, PureWindowsPath


# ---------------------------------------------------------------------------
# 1. Construction and attributes
# ---------------------------------------------------------------------------

def demo_construction():
    print("=" * 60)
    print("Path construction and attributes")
    print("=" * 60)

    # Various ways to construct a Path
    p1 = Path("/usr/local/bin/python3")
    p2 = Path("src/app/main.py")
    p3 = Path.home()           # user's home directory
    p4 = Path.cwd()            # current working directory

    print(f"Absolute path:     {p1}")
    print(f"Relative path:     {p2}")
    print(f"Home directory:    {p3}")
    print(f"Current dir:       {p4}")

    # Path attributes
    p = Path("/projects/myapp/src/main.py")
    print(f"\nPath: {p}")
    print(f"  .name:      {p.name}")        # main.py
    print(f"  .stem:      {p.stem}")        # main
    print(f"  .suffix:    {p.suffix}")      # .py
    print(f"  .parent:    {p.parent}")      # /projects/myapp/src
    print(f"  .parts:     {p.parts}")       # ('/', 'projects', 'myapp', 'src', 'main.py')

    # Multiple suffixes
    archive = Path("data.tar.gz")
    print(f"\n  archive.name:     {archive.name}")
    print(f"  archive.suffix:   {archive.suffix}")    # .gz
    print(f"  archive.suffixes: {archive.suffixes}")  # ['.tar', '.gz']
    print(f"  archive.stem:     {archive.stem}")      # data.tar

    # Parents chain
    p = Path("/a/b/c/d/file.txt")
    print(f"\nParent chain of '{p}':")
    for parent in p.parents:
        print(f"  {parent}")

    print()


# ---------------------------------------------------------------------------
# 2. Path joining — the / operator
# ---------------------------------------------------------------------------

def demo_joining():
    print("=" * 60)
    print("Path joining with / operator")
    print("=" * 60)

    # / is overloaded on Path — works like os.path.join
    base    = Path("/var/log")
    app_log = base / "myapp" / "debug.log"
    print(f"base / 'myapp' / 'debug.log' = {app_log}")

    # Joining with a relative Path
    root    = Path("/projects")
    sub     = Path("backend/src")
    full    = root / sub
    print(f"root / sub = {full}")

    # with_name — replace the filename
    p = Path("/data/configs/production.yaml")
    staging = p.with_name("staging.yaml")
    print(f"\nwith_name: {p.name} -> {staging}")

    # with_stem — replace stem, keep suffix (3.9+)
    versioned = p.with_stem("production_v2")
    print(f"with_stem: {p}")
    print(f"         -> {versioned}")

    # with_suffix — replace extension
    py_file = Path("script.py")
    print(f"\nwith_suffix('.pyc'): {py_file.with_suffix('.pyc')}")
    print(f"with_suffix(''):     {py_file.with_suffix('')}")     # remove extension

    # relative_to — make a path relative to a parent
    full_path   = Path("/var/log/myapp/error.log")
    log_dir     = Path("/var/log")
    relative    = full_path.relative_to(log_dir)
    print(f"\nrelative_to: {full_path.relative_to(log_dir)}")

    print()


# ---------------------------------------------------------------------------
# 3. File I/O operations
# ---------------------------------------------------------------------------

def demo_file_io():
    print("=" * 60)
    print("File read/write operations")
    print("=" * 60)

    with tempfile.TemporaryDirectory() as tmpdir:
        base = Path(tmpdir)

        # --- write_text / read_text ---
        txt_path = base / "notes.txt"
        txt_path.write_text("Line 1\nLine 2\nLine 3\n", encoding="utf-8")
        print(f"Wrote to: {txt_path.name}")

        content = txt_path.read_text(encoding="utf-8")
        print("Content:", content.strip())

        # --- read_lines alternative (generator-friendly) ---
        lines = txt_path.read_text(encoding="utf-8").splitlines()
        print("Lines:", lines)

        # --- write_bytes / read_bytes ---
        bin_path = base / "data.bin"
        bin_path.write_bytes(b"\x00\x01\x02\x03\xff\xfe\xfd")
        raw = bin_path.read_bytes()
        print(f"\nBinary: {raw.hex()}")

        # --- append via open() ---
        log_path = base / "app.log"
        log_path.write_text("START\n", encoding="utf-8")
        with log_path.open("a", encoding="utf-8") as f:
            f.write("INFO: user logged in\n")
            f.write("INFO: order placed\n")
        print(f"\nLog file content:")
        print(log_path.read_text(encoding="utf-8"))

        # --- touch / unlink ---
        tmp_file = base / "temp_marker.lock"
        tmp_file.touch()
        print(f"Lock file exists: {tmp_file.exists()}")
        tmp_file.unlink()
        print(f"After unlink:     {tmp_file.exists()}")

        # --- rename / replace ---
        old = base / "old_name.txt"
        old.write_text("data", encoding="utf-8")
        new = base / "new_name.txt"
        old.rename(new)
        print(f"\nRenamed {old.name} -> {new.name}: {new.exists()}")

    print()


# ---------------------------------------------------------------------------
# 4. Directory operations — mkdir, iterdir, rmdir
# ---------------------------------------------------------------------------

def demo_directories():
    print("=" * 60)
    print("Directory operations")
    print("=" * 60)

    with tempfile.TemporaryDirectory() as tmpdir:
        root = Path(tmpdir)

        # Create nested directories
        deep = root / "a" / "b" / "c"
        deep.mkdir(parents=True, exist_ok=True)
        print(f"Created nested: {deep.relative_to(root)}")

        # Create sibling dirs
        for name in ["src", "tests", "docs", "config"]:
            (root / name).mkdir(exist_ok=True)

        # Create some files
        (root / "src" / "main.py").write_text("# main", encoding="utf-8")
        (root / "src" / "utils.py").write_text("# utils", encoding="utf-8")
        (root / "tests" / "test_main.py").write_text("# tests", encoding="utf-8")
        (root / "config" / "settings.json").write_text('{"debug":false}', encoding="utf-8")
        (root / "README.md").write_text("# Project", encoding="utf-8")

        # iterdir — immediate children
        print("\nRoot contents:")
        for item in sorted(root.iterdir()):
            marker = "/" if item.is_dir() else ""
            print(f"  {item.name}{marker}")

        # Type filtering
        print("\nOnly files in root:")
        for item in root.iterdir():
            if item.is_file():
                print(f"  {item.name}")

        print("\nOnly directories:")
        for item in sorted(root.iterdir()):
            if item.is_dir():
                print(f"  {item.name}/")

        # rmdir — only works on empty directories
        (root / "a" / "b" / "c").rmdir()
        (root / "a" / "b").rmdir()
        (root / "a").rmdir()
        print("\nRemoved nested empty dirs: a/, a/b/, a/b/c/")

    print()


# ---------------------------------------------------------------------------
# 5. glob and rglob — pattern matching
# ---------------------------------------------------------------------------

def demo_glob():
    print("=" * 60)
    print("glob and rglob")
    print("=" * 60)

    with tempfile.TemporaryDirectory() as tmpdir:
        root = Path(tmpdir)

        # Build a fake project tree
        files = [
            "main.py", "utils.py", "config.py",
            "tests/test_main.py", "tests/test_utils.py",
            "docs/index.md", "docs/api.md",
            "data/users.csv", "data/orders.json",
            ".env", ".gitignore",
        ]
        for fpath in files:
            p = root / fpath
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text("", encoding="utf-8")

        # glob — match within this directory (non-recursive)
        print("*.py in root:")
        for p in sorted(root.glob("*.py")):
            print(f"  {p.name}")

        # glob — specific subdirectory
        print("\ntests/test_*.py:")
        for p in sorted(root.glob("tests/test_*.py")):
            print(f"  {p.relative_to(root)}")

        # rglob — recursive, equivalent to glob("**/<pattern>")
        print("\nAll .py files (rglob):")
        for p in sorted(root.rglob("*.py")):
            print(f"  {p.relative_to(root)}")

        print("\nAll .md files (rglob):")
        for p in sorted(root.rglob("*.md")):
            print(f"  {p.relative_to(root)}")

        # rglob("*") — all files and dirs recursively
        all_files = [p for p in root.rglob("*") if p.is_file()]
        print(f"\nTotal files: {len(all_files)}")

        # Find all test files
        test_files = sorted(root.rglob("test_*.py"))
        print("\nTest files:")
        for f in test_files:
            print(f"  {f.relative_to(root)}")

    print()


# ---------------------------------------------------------------------------
# 6. stat — file metadata
# ---------------------------------------------------------------------------

def demo_stat():
    print("=" * 60)
    print("stat — file metadata")
    print("=" * 60)

    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt",
                                     delete=False, encoding="utf-8") as f:
        path = Path(f.name)
        f.write("Hello from pathlib stat demo!\n" * 100)

    try:
        s = path.stat()
        print(f"File: {path.name}")
        print(f"  Size:     {s.st_size:,} bytes")
        print(f"  Modified: {time.ctime(s.st_mtime)}")
        print(f"  Created:  {time.ctime(s.st_ctime)}")
        print(f"  Mode:     {oct(stat.S_IMODE(s.st_mode))}")

        # Check permissions
        is_readable  = os.access(path, os.R_OK)
        is_writable  = os.access(path, os.W_OK)
        is_executable= os.access(path, os.X_OK)
        print(f"  Readable:   {is_readable}")
        print(f"  Writable:   {is_writable}")
        print(f"  Executable: {is_executable}")

    finally:
        path.unlink(missing_ok=True)

    print()


# ---------------------------------------------------------------------------
# 7. PurePath — path manipulation without filesystem access
# ---------------------------------------------------------------------------

def demo_purepath():
    print("=" * 60)
    print("PurePath — logic without filesystem access")
    print("=" * 60)

    # PurePosixPath and PureWindowsPath work on any OS
    posix = PurePosixPath("/home/user/docs/report.pdf")
    win   = PureWindowsPath("C:/Users/Alice/Documents/report.docx")

    print(f"POSIX:   {posix}")
    print(f"  root:   {posix.root}")
    print(f"  parts:  {posix.parts}")

    print(f"\nWindows: {win}")
    print(f"  drive:  {win.drive}")
    print(f"  root:   {win.root}")
    print(f"  stem:   {win.stem}")

    # Common: check file suffixes without touching the filesystem
    def is_image(path: str) -> bool:
        return PurePath(path).suffix.lower() in {".jpg", ".jpeg", ".png", ".gif", ".webp"}

    test_paths = ["photo.jpg", "doc.pdf", "banner.PNG", "data.csv", "icon.WEBP"]
    for tp in test_paths:
        print(f"  {tp:15} is_image={is_image(tp)}")

    # Build cross-platform paths using PurePosixPath for URL segments
    base_url = PurePosixPath("/api/v2")
    endpoint = base_url / "users" / "profile"
    print(f"\nAPI endpoint: {endpoint}")

    print()


# ---------------------------------------------------------------------------
# 8. Practical: walk project and gather stats
# ---------------------------------------------------------------------------

def demo_project_stats():
    print("=" * 60)
    print("Practical: project statistics with rglob")
    print("=" * 60)

    with tempfile.TemporaryDirectory() as tmpdir:
        root = Path(tmpdir)

        # Build a realistic project structure
        project_files = {
            "src/app.py":               "x" * 4200,
            "src/models/user.py":       "x" * 2800,
            "src/models/product.py":    "x" * 1500,
            "src/routes/api.py":        "x" * 3100,
            "tests/test_app.py":        "x" * 1800,
            "tests/test_models.py":     "x" * 2200,
            "docs/architecture.md":     "x" * 5000,
            "docs/api_reference.md":    "x" * 8500,
            "config/production.yaml":   "x" * 400,
            "config/development.yaml":  "x" * 350,
            "README.md":                "x" * 1200,
            "pyproject.toml":           "x" * 600,
            "requirements.txt":         "x" * 250,
        }

        for rel_path, content in project_files.items():
            p = root / rel_path
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(content, encoding="utf-8")

        # Gather stats
        by_ext: dict[str, list[Path]] = {}
        for p in root.rglob("*"):
            if p.is_file():
                ext = p.suffix.lower() or "(none)"
                by_ext.setdefault(ext, []).append(p)

        print("Files by extension:")
        for ext, paths in sorted(by_ext.items()):
            total_bytes = sum(p.stat().st_size for p in paths)
            print(f"  {ext:10} {len(paths):3} files  {total_bytes:8,} bytes")

        # Largest files
        all_files = [(p, p.stat().st_size) for p in root.rglob("*") if p.is_file()]
        all_files.sort(key=lambda x: x[1], reverse=True)
        print("\nTop 5 largest files:")
        for p, size in all_files[:5]:
            print(f"  {str(p.relative_to(root)):40} {size:6,} bytes")

    print()


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    demo_construction()
    demo_joining()
    demo_file_io()
    demo_directories()
    demo_glob()
    demo_stat()
    demo_purepath()
    demo_project_stats()
