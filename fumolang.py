#!/user/sbin/python

VALUES = ['Fumo', 'FumoFumo']


class BitWriter:

    def __init__(self):
        self._value = 0
        self._bit = 7
        self.bytes = []

    @property
    def flushable(self):
        return self._value != 0 and self._bit != 7

    def write(self, value):
        self._bit -= 1
        if self._bit < 0:
            self.flush()
        if value:
            self._value = self._value | (1 << self._bit)

    def flush(self):
        self.bytes.append(self._value)
        self._value = 0
        self._bit = 7

    def to_bytes(self):
        return bytes(self.bytes)


def bytes2fumo(binary):
    for byte in binary:
        yield VALUES[(byte >> 7) & 1]
        yield VALUES[(byte >> 6) & 1]
        yield VALUES[(byte >> 5) & 1]
        yield VALUES[(byte >> 4) & 1]
        yield VALUES[(byte >> 3) & 1]
        yield VALUES[(byte >> 2) & 1]
        yield VALUES[(byte >> 1) & 1]
        yield VALUES[byte & 1]


def fumo2bytes(writer, line):
    words = [word.casefold() for word in line.split()]
    for word in words:
        if word == "fumo":
            writer.write(0)
        elif word == "":
            writer.write(1)


def compile(src, dst):
    writer = BitWriter()
    with open(src, 'r+') as src_file:
        with open(dst, 'wb+') as dst_file:
            while True:
                line = src_file.readline()
                if not line:
                    break
                fumo2bytes(writer, line)
                dst_file.write(writer.to_bytes())
            if writer.flushable:
                writer.flush()
                dst_file.write(writer.to_bytes())


def decompile(src, dst):
    with open(src, 'rb+') as src_file:
        with open(dst, 'w+') as dst_file:
            while True:
                block = src_file.read(1024 ** 2) # 1MB
                if not block:
                    break
                out = ' '.join(bytes2fumo(block))
                dst_file.write(out)


decompile('hello', 'hello.fumo')
