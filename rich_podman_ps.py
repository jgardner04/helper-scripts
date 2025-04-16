import json
import subprocess
from datetime import datetime
from rich.console import Console
from rich.table import Table

# Get JSON output from podman
result = subprocess.run(['podman', 'ps', '--format', 'json'], capture_output=True, text=True)
containers = json.loads(result.stdout)

# Initialize the Rich table
table = Table(title="Podman Containers")
table.add_column("ID", style="cyan")
table.add_column("Name", style="magenta")
table.add_column("Image")
table.add_column("Status", style="green")
table.add_column("Ports", style="yellow")
table.add_column("Created", style="dim")

for c in containers:
    container_id = c.get('Id', '')[:12]
    name = c.get('Names', [''])[0]
    image = c.get('Image', '')
    status = c.get('Status', '')
    ports = ', '.join(c.get('Ports') or []) or '-'
    created = c.get('CreatedAt', '')
    
    # Format the created timestamp if present
    try:
        created_dt = datetime.strptime(created, "%Y-%m-%dT%H:%M:%S.%f%z")
        created_str = created_dt.strftime("%b %d %H:%M")
    except Exception:
        created_str = created

    table.add_row(container_id, name, image, status, ports, created_str)

# Print the table
console = Console()
console.print(table)
