"""Cold-chain logger for Brightwell Packaging"""

class ColdChainLog:
    """Internal service for cold-chain-log."""

    def status(self) -> str:
        return "ok"


if __name__ == "__main__":
    print(ColdChainLog().status())
