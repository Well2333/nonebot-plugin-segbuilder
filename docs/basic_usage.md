# 基础使用

首先，你需要在需要使用的插件中导入此插件，防止因为你未导入别人在之后导入造成的错误。

```python
from nonebot import require

require("nonebot_plugin_segbuilder")
```

然后，你就可以通过 `SegmentBuilder` 对象来构建 `MessageSegment` 了，例如如下是一个基于 OneBot V11 适配器的简易插件

```python
from pathlib import Path

from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot, MessageSegment

t = on_command("setu")


@t.handle()
async def _(
    bot: Bot,
):
    img = Path("imgae.png")
    image = MessageSegment.image(img)
    await t.send(image)
```

在引入 `SegmentBuilder` 后，可以使用其 `image` 方法根据不同的适配器生成不同的代码，例如

```python
from pathlib import Path
from typing import Union

from nonebot import on_command, require
from nonebot.adapters.mirai2 import Bot as Mirai_Bot
from nonebot.adapters.onebot.v11 import Bot as V11_Bot
from nonebot.adapters.onebot.v12 import Bot as V12_Bot
from nonebot.adapters.qqguild import Bot as QG_Bot

require("nonebot_plugin_segbuilder")


from nonebot_plugin_segbuilder import SegmentBuilder

t = on_command("setu")


@t.handle()
async def _(bot: Union[Mirai_Bot, V11_Bot, V12_Bot, QG_Bot]):
    img = Path("image.png")
    image = await SegmentBuilder.image(image = img)
    await t.send(image)
```

这样，我们在几乎没有改动事件处理的逻辑的情况下便将其拓展至四个适配器了。

其具体用法可详见 [源代码](../nonebot_plugin_segbuilder/base.py) 中的说明。
