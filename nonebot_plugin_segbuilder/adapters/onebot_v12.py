import time
from io import BytesIO
from pathlib import Path
from typing import Optional, Union

from nonebot.adapters.onebot.v12 import Adapter, Bot, MessageEvent, MessageSegment
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
        MessageSegment.mention_all()
        if user_id == "all"
        else MessageSegment.mention(str(user_id))
    )


@SegmentBuilder.register_impl(ADAPTER_NAME)
async def reply(bot: Bot, event: MessageEvent, message_id: Union[str, int] = 0):
    return MessageSegment.reply(
        message_id=str(message_id or event.message_id), user_id=event.get_user_id()
    )


@SegmentBuilder.register_impl(ADAPTER_NAME)
async def image(bot: Bot, image: Union[str, bytes, BytesIO, Path]):
    image = await get_image(image)
    if isinstance(image, bytes):
        fileid = await bot.upload_file(
            type="data", name=f"{time.time()}.jpg", data=image
        )
    else:
        fileid = await bot.upload_file(type="url", name=f"{time.time()}.jpg", url=image)
    return MessageSegment.image(file_id=fileid["file_id"])


logger.success(f"The adapter {ADAPTER_NAME} is loaded successfully")
