from io import BytesIO
from pathlib import Path
from typing import Any, Dict, Optional, Union
import contextlib

from nonebot.adapters import Bot, Event
from nonebot.adapters import MessageSegment as MS
from nonebot.log import logger
from nonebot.matcher import current_bot, current_event


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
            return f"[Unsupport Message: {name}]"
        except Exception as e:
            logger.exception(e)
            return f"[Build failed: {name}]"

    @classmethod
    def register_impl(cls, adapter: str, segment_type: Optional[str] = None):
        def decorator(func):
            segtype = segment_type or func.__name__
            cls._impl_map.setdefault(segtype, {})
            cls._impl_map[segtype][adapter] = func
            return func

        return decorator

    @staticmethod
    def __get_bot() -> Bot:
        try:
            return current_bot.get()
        except Exception as e:
            raise RuntimeError("Unable to get Bot object") from e

    @staticmethod
    def __get_event() -> Union[Event, None]:
        with contextlib.suppress(Exception):
            return current_event.get()

    @classmethod
    async def at(
        cls,
        *,
        user_id: Union[str, int] = 0,
        bot: Optional[Bot] = None,
        event: Optional[Event] = None,
    ) -> Union[MS, str]:
        bot = bot or cls.__get_bot()
        event = event or cls.__get_event()
        return await cls.on_call("at", bot, event=event, user_id=user_id)

    @classmethod
    async def image(
        cls, *, image: Union[str, bytes, BytesIO, Path], bot: Optional[Bot] = None
    ) -> Union[MS, str]:
        bot = bot or cls.__get_bot()
        return await cls.on_call("image", bot, image=image)

    @classmethod
    async def reply(
        cls,
        *,
        message_id: Optional[Union[str, int]] = 0,
        bot: Optional[Bot] = None,
        event: Optional[Event] = None,
    ) -> Union[MS, str]:
        bot = bot or cls.__get_bot()
        event = event or cls.__get_event()
        return await cls.on_call("reply", bot, event=event, message_id=message_id)
