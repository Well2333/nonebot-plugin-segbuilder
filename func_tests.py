import contextlib
from typing import Union, Any
from pathlib import Path

from nonebot import on_command, require
from nonebot.adapters.mirai2 import Bot as M_Bot
from nonebot.adapters.mirai2.event import MessageEvent as M_MessageEvent
from nonebot.adapters.onebot.v11 import Bot as V11_Bot
from nonebot.adapters.onebot.v11 import MessageEvent as V11_MessageEvent
from nonebot.adapters.onebot.v12 import Bot as V12_Bot
from nonebot.adapters.onebot.v12 import MessageEvent as V12_MessageEvent
from nonebot.adapters.qqguild import Bot as QG_Bot
from nonebot.adapters.qqguild.event import MessageEvent as QG_MessageEvent
from nonebot.params import Depends

require("nonebot_plugin_segbuilder")


from nonebot_plugin_segbuilder import SegmentBuilder

t = on_command("start")


@t.handle()
async def _(
    bot: Union[M_Bot, V11_Bot, V12_Bot, QG_Bot],
    event: Union[
        M_MessageEvent,
        V11_MessageEvent,
        V12_MessageEvent,
        QG_MessageEvent,
    ],
):
    # sourcery skip: use-fstring-for-concatenation
    # at
    at = await SegmentBuilder.at(bot, event)
    await t.send(at)
    # at_all
    at_all = await SegmentBuilder.at(bot, user_id="all")
    await t.send(at_all)

    # reply
    reply = await SegmentBuilder.reply(bot, event)
    msg = await t.send(reply + "123")
    # reply to msgid
    with contextlib.suppress(Exception):
        msgid = msg["message_id"]
        reply_ = await SegmentBuilder.reply(bot, event, message_id=msgid)
        await t.send(reply_ + "456")

    # image
    img = Path("docs/images/nbp_logo.png")
    # pathlike or bytes
    image = await SegmentBuilder.image(bot, img)
    await t.send(image)
    # url
    image = await SegmentBuilder.image(
        bot,
        "https://i.pixiv.re/img-original/img/2022/02/05/00/00/03/96003801_p0.jpg",
    )
    await t.send(image)
