from aiohttp import client
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from app import logger, loop, settings


class TGBot:
    def __init__(self): ...
    def start(self):
        scheduler = AsyncIOScheduler(timezone="Europe/Moscow", event_loop=loop)
        scheduler.add_job(self.notify, "cron", hour=18)
        scheduler.start()

    async def _send_message(self, text: str):
        async with client.ClientSession() as session:
            url = f"https://api.telegram.org/bot{settings.tg_bot.token}/sendMessage"
            payload = {"chat_id": settings.tg_bot.admin_id, "text": text}
            await session.post(url, data=payload)

    async def notify(self):
        await self._send_message("Setup your spendings today!!")
