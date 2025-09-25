import json
from pathlib import Path
from datetime import datetime

# Ścieżki do plików
BASE = Path(__file__).parent
ALERTS_FILE = BASE / "alerts.json"
ACTIONS_FILE = BASE / "actions.log"

# Mapowanie typu alertu na decyzję
ACTIONS_MAP = {
    "http_400": "Zgłoś do zespołu API",
    "cpu_high": "Uruchom restart serwisu",
    "disk_full": "Wyślij alert do zespołu infrastruktury",
}

# Wczytanie alertów z JSON
def load_alerts(path=ALERTS_FILE):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Nie można wczytać {path}: {e}")
        return []

# Funkcja decyzyjna
def decide(alert):
    return ACTIONS_MAP.get(alert.get("type"), "Nieznany typ alertu - eskaluj do L2")

# Zapis decyzji do pliku
def write_actions(results, path=ACTIONS_FILE):
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"# Run: {datetime.utcnow().isoformat()}Z\n")
        for r in results:
            f.write(f"Alert {r['id']}: {r['action']}\n")

# Główna funkcja
def main():
    alerts = load_alerts()
    if not alerts:
        print("Brak alertów do przetworzenia.")
        return
    results = []
    for a in alerts:
        action = decide(a)
        results.append({"id": a.get("id"), "action": action})
    write_actions(results)
    print(f"✅ Zapisano {len(results)} decyzji do {ACTIONS_FILE}")

if __name__ == "__main__":
    main()