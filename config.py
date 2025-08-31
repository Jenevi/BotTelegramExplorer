from dataclasses import dataclass
from typing import List
import os

try:
    from dotenv import load_dotenv  # type: ignore
    load_dotenv()
except Exception:
    # python-dotenv is optional; environment variables may be set externally
    pass


@dataclass
class Config:
    """Application configuration loaded from environment or CLI."""

    api_id: int
    api_hash: str
    search_terms: List[str]
    output_path: str = "groups.csv"


def from_env() -> Config:
    """Create configuration instance from environment variables.

    Expected variables:
    - API_ID: Telegram API ID
    - API_HASH: Telegram API hash
    - SEARCH_TERMS: comma separated list of keywords
    - OUTPUT_PATH: path to CSV file for saving results
    """

    api_id = int(os.getenv("API_ID", "0"))
    api_hash = os.getenv("API_HASH", "")
    terms = os.getenv("SEARCH_TERMS", "")
    search_terms = [t.strip() for t in terms.split(",") if t.strip()]
    output_path = os.getenv("OUTPUT_PATH", "groups.csv")
    return Config(api_id=api_id, api_hash=api_hash, search_terms=search_terms, output_path=output_path)
