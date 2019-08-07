class Gun(object):
    def __init__(self, box):
        self.box = box

    def shoot(self):
        if self.box.count == 0:
            print("无子弹")
        else:
            self.box.count -= 1
            self.box.bullets.pop()
            print("砰！子弹剩余 %d 发"%self.box.count)

