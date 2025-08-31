from telethon import TelegramClient
from config import Config


def create_client(config: Config) -> TelegramClient:
    """Create a Telegram client using the provided configuration."""
    return TelegramClient("bot_session", config.api_id, config.api_hash)
