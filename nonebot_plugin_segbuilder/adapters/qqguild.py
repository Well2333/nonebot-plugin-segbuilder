from io import BytesIO
from pathlib import Path
from typing import Optional, Union

from httpx import AsyncClient
from nonebot.adapters.qqguild import Adapter, Bot, MessageEvent, MessageSegment
from nonebot.log import logger

from ..base import SegmentBuilder
from ..utils import get_image

ADAPTER_NAME = Adapter.get_name()


@SegmentBuilder.register_impl(ADAPTER_NAME)
async def at(
    bot: Bot, event: Optional[MessageEvent] = None, user_id: Union[str, int] = 0
):
    if event:
        user_id = event.get_user_id()
    if not user_id:
        raise ValueError("user_id can not be empty")
    return (
        MessageSegment.mention_everyone()
        if user_id == "all"
        else MessageSegment.mention_user(int(user_id))
    )


@SegmentBuilder.register_impl(ADAPTER_NAME)
async def reply(bot: Bot, event: MessageEvent, message_id: Union[str, int] = 0):
    return MessageSegment.reference(reference=str(message_id or event.id))


@SegmentBuilder.register_impl(ADAPTER_NAME)
async def image(bot: Bot, image: Union[str, bytes, BytesIO, Path]):
    image = await get_image(image)
    if isinstance(image, str):
        async with AsyncClient() as client:
            resp = await client.get(image)
        image = resp.content
    return MessageSegment.file_image(image)


logger.success(f"The adapter {ADAPTER_NAME} is loaded successfully")
