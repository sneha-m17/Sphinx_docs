# SAS2PY Documentation

This project contains the documentation for the SAS2PY project, built using [Sphinx](https://www.sphinx-doc.org/) with the [Furo theme](https://pradyunsg.me/furo/) and several Sphinx extensions.

## Features
- Responsive, modern documentation theme (Furo)
- Enhanced design components (sphinx-design)
- Toggle buttons for content (sphinx-togglebutton)
- Markdown support (MyST parser)

## Requirements
- Python 3.9 or higher

## Installation

1. **Clone the repository** (if you haven't already):
   ```sh
   git clone <your-repo-url>
   cd <your-repo-directory>
   ```

2. **(Optional) Create and activate a virtual environment:**
   ```sh
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

## Building the Documentation

From the root of the project (where `Makefile` or `make.bat` is located):

- **On Linux/macOS:**
  ```sh
  make html
  ```
- **On Windows (cmd):**
  ```cmd
  make.bat html
  ```
- **On Windows (PowerShell):**
  ```powershell
  .\make.bat html
  ```

The built HTML documentation will be in the `docs/_build/html/` directory.

## Live Preview (Optional)
For live-reloading during documentation writing, you can install [sphinx-autobuild](https://github.com/executablebooks/sphinx-autobuild):

```sh
pip install sphinx-autobuild
sphinx-autobuild docs/source docs/_build/html
```

Then open [http://localhost:8000](http://localhost:8000) in your browser.

## Adding Content
- Edit or add `.rst` or `.md` files in `docs/source/`.
- Update `index.rst` to include new pages.

## Customization
- Static files (CSS, images, JS) are in `docs/source/_static/`.
- Theme and extension configuration: `docs/source/conf.py`.

## Useful Links
- [Sphinx Documentation](https://www.sphinx-doc.org/)
- [Furo Theme](https://pradyunsg.me/furo/)
- [sphinx-design](https://sphinx-design.readthedocs.io/)
- [MyST Parser](https://myst-parser.readthedocs.io/) 