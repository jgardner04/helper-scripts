# helper-scripts

A collection of utility scripts to streamline local development workflows.  
This repo currently includes `pview`—a clean, formatted terminal viewer for Podman containers.

---

## 📦 pview: Pretty `podman ps` Output

`pview` is a lightweight wrapper that formats `podman ps` output using Python and the [Rich](https://github.com/Textualize/rich) library.

Instead of messy default output, you'll get a colorized, readable table of containers showing:

- Container ID
- Name
- Image
- Status
- Ports
- Created time

### ✨ Sample Output

```
┏━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━┓
┃ ID           ┃ Name            ┃ Image                          ┃ Status    ┃ Ports ┃ Created    ┃
┡━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━┩
│ b1a88bb96a7e │ admiring_liskov │ localhost/mcp/puppeteer:latest │ Up 4 days │ -     │ 4 days ago │
└──────────────┴─────────────────┴────────────────────────────────┴───────────┴───────┴────────────┘
```

---

## ⚙️ Setup

### 1. Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/helper-scripts.git
cd helper-scripts
```

### 2. Set up the virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install rich
```

### 3. Run the tool

```bash
./run_podman_view.sh
```

---

## ⌨️ Optional: Create an alias

To run `pview` from anywhere, add this to your `~/.zshrc` (or `~/.bashrc`):

```bash
alias pview="$HOME/git/helper-scripts/run_podman_view.sh"
```

Then reload your shell:

```bash
source ~/.zshrc
```

Now just type:

```bash
pview
```

---

## 📝 Scripts

- `rich_podman_ps.py`: Collects and formats `podman ps` JSON data using Rich.
- `run_podman_view.sh`: Activates the virtual environment and runs the script.
- `venv/`: Your local Python virtual environment (optional to commit).

---

## 📋 Requirements

- macOS or Linux
- Python 3.7+
- Podman installed and working (`podman ps --format json`)
- Rich (`pip install rich`)

---

## 🪪 License

MIT License

---

> Built by Jonathan Gardner
