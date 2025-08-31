from typing import Dict, Iterable, List
from telethon import functions
from telethon.tl.types import Channel, Chat


async def search_groups(client, keyword: str, limit: int = 50) -> List[Dict]:
    """Search public chats/channels matching the keyword."""
    result = await client(functions.contacts.SearchRequest(q=keyword, limit=limit))
    groups = []
    for chat in result.chats:
        if isinstance(chat, (Channel, Chat)):
            groups.append(
                {
                    "id": chat.id,
                    "title": getattr(chat, "title", ""),
                    "username": getattr(chat, "username", ""),
                    "participants": getattr(chat, "participants_count", None),
                    "description": getattr(chat, "about", ""),
                }
            )
    return groups


async def collect_groups(client, keywords: Iterable[str], limit: int = 50) -> List[Dict]:
    """Collect unique groups for all keywords."""
    collected: Dict[int, Dict] = {}
    for kw in keywords:
        results = await search_groups(client, kw, limit)
        for group in results:
            collected[group["id"]] = group
    return list(collected.values())
