import base64
from io import BytesIO
from pathlib import Path
from typing import Optional, Union

from nonebot.adapters.mirai2 import Adapter, Bot, MessageSegment
from nonebot.adapters.mirai2.event import FriendMessage, GroupMessage, MessageEvent
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
    if isinstance(event, FriendMessage):
        return "全体成员" if user_id == "all" else f"@{user_id}"
    return (
        MessageSegment.at_all() if user_id == "all" else MessageSegment.at(int(user_id))
    )


@SegmentBuilder.register_impl(ADAPTER_NAME)
async def reply(bot: Bot, event: MessageEvent, message_id: Union[str, int] = 0):
    # group_id: int = event.sender.group.id if isinstance(event, GroupMessage) else 0
    # target_id: int = group_id or event.self_id
    # quote = MessageSegment.quote(
    #    id=event.source.id,  # type:ignore
    #    sender_id=event.sender.id,
    #    target_id=target_id,
    #    group_id=group_id,
    #    origin=event.message_chain,
    # )
    # return quote
    return ""


@SegmentBuilder.register_impl(ADAPTER_NAME)
async def image(bot: Bot, image: Union[str, bytes, BytesIO, Path]):
    image = await get_image(image)
    if isinstance(image, bytes):
        return MessageSegment.image(base64=base64.b64encode(image).decode("utf-8"))
    else:
        return MessageSegment.image(url=image)


logger.success(f"The adapter {ADAPTER_NAME} is loaded successfully")
