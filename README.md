# Bot for exploring Telegram groups

This project contains a minimal implementation of a Telegram bot that searches for
public groups related to effective altruism. The bot uses the [Telethon](https://docs.telethon.dev)
client library to query the Telegram API.

## Usage

1. Obtain Telegram API credentials from https://my.telegram.org.
2. Set the following environment variables or pass them via CLI arguments:
   - `API_ID`
   - `API_HASH`
3. Run the script:

```bash
python main.py --search-terms "effective altruism, EA" --output groups.csv
```

The results will be stored in a CSV file containing basic information about
matching groups.

## Modules

- `config.py` – configuration loader
- `tg_client.py` – Telegram client factory
- `collector.py` – search helper functions
- `filter.py` – keyword based filter
- `storage.py` – CSV writer
- `main.py` – orchestrates the workflow

This code is meant as an MVP and can be extended with better filtering, storage
options, and scheduling for periodic searches.
