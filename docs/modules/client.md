# TelegramClient

The [TelegramClient][telethon.client.telegramclient.TelegramClient] aggregates several mixin
classes to provide all the common functionality in a nice, Pythonic interface.
Each mixin has its own methods, which you all can use.

**In short, to create a client you must run:**

```python
from telethon import TelegramClient

client = TelegramClient(name, api_id, api_hash)

async def main():
    # Now you can use all client methods listed below, like for example...
    await client.send_message('me', 'Hello to myself!')

with client:
    client.loop.run_until_complete(main())
```

You **don't** need to import these `AuthMethods`, `MessageMethods`, etc.
Together they are the [TelegramClient][telethon.client.telegramclient.TelegramClient] and
you can access all of their methods.

See :ref:`client-ref` for a short summary.

::: telethon.client.telegramclient
    rendering:
        show_if_no_docstring: True

::: telethon.client.telegrambaseclient

::: telethon.client.account

::: telethon.client.auth

::: telethon.client.bots

::: telethon.client.buttons

::: telethon.client.chats

::: telethon.client.dialogs

::: telethon.client.downloads

::: telethon.client.messageparse

::: telethon.client.messages

::: telethon.client.updates

::: telethon.client.uploads

::: telethon.client.users
