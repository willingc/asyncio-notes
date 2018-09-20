"""dev_detected_never_awaited_coroutine.py"""

import asyncio

async def test():
    print("never scheduled")

async def main():
    test()

# To fix, await the coroutine
#
# async def main():
#    await test()


asyncio.run(main())