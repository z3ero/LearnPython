'''
    async和await是针对coroutine的新语法，要使用新的语法，只需要做两步简单的替换，
    (1) 把@asyncio.coroutine替换为async；
    (2) 把yield from替换为await。
'''
# 使用新方法 重写 代码 5
import asyncio

async def wget(host):
    print('wget %s ...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = await connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    await writer.drain()
    while True:
        line = await reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # ignore the body, close the socket
    writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

