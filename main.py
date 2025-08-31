import argparse
import asyncio
from config import Config, from_env
from tg_client import create_client
from collector import collect_groups
from filter import filter_groups
from storage import save_csv


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Search Telegram groups related to effective altruism")
    parser.add_argument("--search-terms", type=str, help="Comma separated keywords", default="")
    parser.add_argument("--output", type=str, default=None, help="Path to output CSV")
    parser.add_argument("--api-id", type=int, default=None, help="Telegram API ID")
    parser.add_argument("--api-hash", type=str, default=None, help="Telegram API hash")
    parser.add_argument("--limit", type=int, default=50, help="Limit per keyword")
    return parser.parse_args()


async def run() -> None:
    args = parse_args()
    config: Config = from_env()

    if args.api_id is not None:
        config.api_id = args.api_id
    if args.api_hash is not None:
        config.api_hash = args.api_hash
    if args.search_terms:
        config.search_terms = [s.strip() for s in args.search_terms.split(",") if s.strip()]
    if args.output is not None:
        config.output_path = args.output

    if not config.api_id or not config.api_hash:
        raise RuntimeError("API_ID and API_HASH must be provided via env or CLI")

    async with create_client(config) as client:
        groups = await collect_groups(client, config.search_terms, limit=args.limit)

    relevant = filter_groups(groups, config.search_terms)
    save_csv(relevant, config.output_path)
    print(f"Saved {len(relevant)} groups to {config.output_path}")


if __name__ == "__main__":
    asyncio.run(run())
