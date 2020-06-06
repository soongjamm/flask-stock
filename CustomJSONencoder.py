# 플라스크 기본 인코더가 있는데, 그 안에 어떤 값을 변경 시킬 것
# 그것을 위해 상속을 받아서 변경 -> 덮어쓰기

from flask.json import JSONEncoder  # 기본 인코더
import numpy as np


class CustomJSONEncoder(JSONEncoder):  # 상속
    def __init__(self, **kwargs):
        kwargs["ensure_ascii"] = False
        super().__init__(**kwargs)

    def default(self, obj):
        try:
            if isinstance(obj, np.integer):
                return int(obj)
            if isinstance(obj, np.float):
                return int(obj)

            return str(obj).encode('utf-8')

        except TypeError:
            pass

        return super().default(obj)
        print()
