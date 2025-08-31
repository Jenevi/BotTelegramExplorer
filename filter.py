from typing import Dict, Iterable, List


def filter_groups(groups: Iterable[Dict], keywords: Iterable[str]) -> List[Dict]:
    """Return groups where title or description contains any keyword."""
    keyword_list = [k.lower() for k in keywords]
    filtered: List[Dict] = []
    for group in groups:
        text = f"{group.get('title', '')} {group.get('description', '')}".lower()
        for kw in keyword_list:
            if kw in text:
                group["matched_keyword"] = kw
                filtered.append(group)
                break
    return filtered
