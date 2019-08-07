# 人射击子弹分析

# 人: Person
# 属性： 枪
# 行为： 开火，装弹

# 枪：Gun
# 属性：弹夹
# 行为：射击

# 弹夹：BulletBox
# 属性： 子弹列表， 子弹数量
# 行为：

# 子弹：Bullet

from qf_python.人射击子弹.person import Person
from qf_python.人射击子弹.gun import Gun
from qf_python.人射击子弹.box import Box
from qf_python.人射击子弹.bullet import Bullet

def main():
    bullets = [Bullet() for i in range(5)]  # 5发子弹
    box = Box(bullets, 5)  # 5发子弹的弹夹
    gun = Gun(box) # 带有 5发子弹弹夹 的枪
    per = Person(gun)  # 拿枪的人

    # 开枪
    for  i in range(6):
        per.fire()
    per.changeBox(5)

if __name__=="__main__":
    main()