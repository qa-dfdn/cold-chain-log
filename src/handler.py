"""Request handler for cold-chain-log."""

def handle(event: dict) -> dict:
    kind = event.get("kind", "scan")
    return {"ok": True, "kind": kind, "service": "cold-chain-log"}
