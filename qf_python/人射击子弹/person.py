from qf_python.人射击子弹.bullet import Bullet
class Person(object):
    def __init__(self, gun):
        self.gun = gun

    def fire(self):
        self.gun.shoot()

    # 装弹
    def changeBox(self, count):
        for i in range(count):
            self.gun.box.bullets.append(Bullet())
        self.gun.box.count += count
        print("增加了 %d 发子弹，现有 %d 发子弹！"%(count, self.gun.box.count))



