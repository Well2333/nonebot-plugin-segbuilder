import nonebot
from nonebot.adapters.mirai2 import Adapter as Mirai_Adapter
from nonebot.adapters.onebot.v11 import Adapter as ONEBOT_V11Adapter
from nonebot.adapters.onebot.v12 import Adapter as ONEBOT_V12Adapter
from nonebot.adapters.qqguild import Adapter as QQGuild_Adapter

nonebot.init()

driver = nonebot.get_driver()
#driver.register_adapter(Mirai_Adapter)
driver.register_adapter(ONEBOT_V11Adapter)
driver.register_adapter(ONEBOT_V12Adapter)
driver.register_adapter(QQGuild_Adapter)

nonebot.load_plugin("func_tests")

if __name__ == "__main__":
    nonebot.run()
