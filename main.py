# Placeholder content for: main.py
# Auto-start bot saat FastAPI aktif
import asyncio
from start_main import run_bot
@app.on_event("startup")
async def startup_event():
    asyncio.create_task(run_bot())
