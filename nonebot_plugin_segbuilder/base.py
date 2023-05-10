from io import BytesIO
from pathlib import Path
from typing import Any, Dict, Optional, Union

from nonebot.adapters import Bot, Event
from nonebot.adapters import MessageSegment as MS
from nonebot.log import logger


class SegmentBuilder:
    _impl_map: Dict[str, Dict[str, Any]] = {}

    @classmethod
    async def on_call(cls, name: str, bot: Bot, *args, **kwargs) -> Union[MS, str]:
        platform = bot.adapter.get_name()
        try:
            return await cls._impl_map[name][platform](bot, *args, **kwargs)
        except KeyError:
            logger.warning(
                f"Adapter {platform} or MessageSegment {name} is not supported yet"
            )
            return f"[Adapter {platform} or MessageSegment {name} is not supported yet]"

    @classmethod
    def register_impl(cls, adapter: str, segment_type: Optional[str] = None):
        def decorator(func):
            segtype = segment_type or func.__name__
            cls._impl_map.setdefault(segtype, {})
            cls._impl_map[segtype][adapter] = func
            return func

        return decorator

    @classmethod
    async def at(
        cls,
        bot: Bot,
        event: Optional[Event] = None,
        user_id: Union[str, int] = 0,
    ):
        return await cls.on_call("at", bot, event=event, user_id=user_id)

    @classmethod
    async def image(cls, bot: Bot, image: Union[str, bytes, BytesIO, Path]):
        return await cls.on_call("image", bot, image=image)

    @classmethod
    async def reply(cls, bot: Bot, event: Event, message_id: Union[str, int] = 0):
        return await cls.on_call("reply", bot, event=event, message_id=message_id)
