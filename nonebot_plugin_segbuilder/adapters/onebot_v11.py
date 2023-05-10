from io import BytesIO
from pathlib import Path
from typing import Optional, Union

from nonebot.adapters.onebot.v11 import Adapter, Bot, MessageEvent, MessageSegment
from nonebot.log import logger

from ..base import SegmentBuilder

ADAPTER_NAME = Adapter.get_name()


@SegmentBuilder.register_impl(ADAPTER_NAME)
async def at(
    bot: Bot, event: Optional[MessageEvent] = None, user_id: Union[str, int] = 0
):
    if event:
        user_id = event.get_user_id()
    if not user_id:
        raise ValueError("user_id can not be empty")
    return MessageSegment.at(user_id)


@SegmentBuilder.register_impl(ADAPTER_NAME)
async def reply(bot: Bot, event: MessageEvent, message_id: Union[str, int] = 0):
    return MessageSegment.reply(int(message_id or event.message_id))


@SegmentBuilder.register_impl(ADAPTER_NAME)
async def image(bot: Bot, image: Union[str, bytes, BytesIO, Path]):
    return MessageSegment.image(image)


logger.success(f"The adapter {ADAPTER_NAME} is loaded successfully")
