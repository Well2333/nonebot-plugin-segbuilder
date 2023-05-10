from typing import Union
from io import BytesIO
from pathlib import Path
from anyio import Path as AsyncPath


async def get_image(image: Union[str, bytes, BytesIO, Path]):
    """获取图片类型的消息段，不支持base64输入"""
    if isinstance(image, bytes):
        # nothing to do here
        pass
    elif isinstance(image, BytesIO):
        image = image.getvalue()
    elif isinstance(image, Path) or Path(image).is_file():
        image = await AsyncPath(image).read_bytes()
    else:
        # url
        return image

    # bytes
    return image
