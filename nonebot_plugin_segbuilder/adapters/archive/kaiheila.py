# 由于开黑啦逆天的消息支持程度，基本不可能在消息构建层面与其他适配器兼容
# 因此本模块处于弃用状态，如果有需要，请使用saa
# https://github.com/felinae98/nonebot-plugin-send-anything-anywhere

import time
from io import BytesIO
from pathlib import Path
from typing import Optional, Union

from httpx import AsyncClient
from nonebot.adapters.kaiheila import Adapter, Bot, MessageSegment
from nonebot.adapters.kaiheila.event import MessageEvent
from nonebot.log import logger

from ...base import SegmentBuilder
from ...utils import get_image

ADAPTER_NAME = Adapter.get_name()


@SegmentBuilder.register_impl(ADAPTER_NAME)
async def at(
    bot: Bot, event: Optional[MessageEvent] = None, user_id: Union[str, int] = 0
):
    if event:
        user_id = event.get_user_id()
    if not user_id:
        raise ValueError("user_id can not be empty")
    return MessageSegment.at(str(user_id))


@SegmentBuilder.register_impl(ADAPTER_NAME)
async def reply(bot: Bot, event: MessageEvent, message_id: Union[str, int] = 0):
    # return MessageSegment.quote(str(message_id or event.SegmentBuilderg_id))
    return ""


@SegmentBuilder.register_impl(ADAPTER_NAME)
async def image(bot: Bot, image: Union[str, bytes, BytesIO, Path]):
    image = await get_image(image)
    if isinstance(image, str):
        async with AsyncClient() as client:
            resp = await client.get(image)
        image = resp.content
    file_key = await bot.upload_file(image, f"{time.time()}.jpg")
    return MessageSegment.image(file_key)


logger.success(f"The adapter {ADAPTER_NAME} is loaded successfully")

raise NotImplementedError
