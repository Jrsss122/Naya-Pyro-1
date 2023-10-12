from asyncio import get_event_loop_policy

from kynaylibs import *
from kynaylibs.nan import *
from kynaylibs.nan.load import *
from kynaylibs.nan.utils import *
from kynaylibs.nan.utils.db import *
from pyrogram import idle
from uvloop import install

from naya import *

MSG_ON = """
**Arab Pyro Actived ✅**
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
◉ **Versi** : `{}`
◉ **Phython** : `{}`
◉ **Pyrogram** : `{}`
◉ **Arablibs** : `{}`
**Ketik** `{}alive` **untuk Mengecheck Bot**
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
"""


async def main():
    await app.start()
    LOGGER("Startup").info("Memulai Arab-Pyro Premium..")
    for bot in botlist:
        try:
            await bot.start()
            ex = bot.me
            await ajg(bot)
            await babi(bot)
            LOGGER("✓").info(
                f"Started as {ex.first_name} {ex.last_name or ''} | {ex.id} "
            )
            ids.append(ex.id)
            LOGGER("Info").info("Startup Completed")
        except Exception as e:
            LOGGER("X").info(f"{e}")
    install()
    await loadprem()
    await idle()
    await aiosession.close()


if __name__ == "__main__":
    get_event_loop_policy().get_event_loop().run_until_complete(main())
