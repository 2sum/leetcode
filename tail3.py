
#!/usr/bin/env python3

"""
Simple tail in Python.

TODO:
    0. file rotate to new fd
    1. file rewrite/truncate with same fd
    2. argparse
"""



import traceback
from typing import Iterator

import os
import io
from time import sleep
from pathlib import Path

class Solution:
    def __init__(self, file_path: str="/Users/malaybiswal/Downloads/a.txt", chunksize: int=io.DEFAULT_BUFFER_SIZE, check_interval: float=0.1):
        self.file_path = file_path
        self.chunksize = chunksize
        self.check_interval = check_interval

        assert Path(file_path).exists(), f"{file_path} not exist"
        assert self.chunksize > 0 and self.check_interval > 0

    def tail(self, n: int = 1, follow: bool=True) -> Iterator[str]:
        assert n >= 0, "Only support postive inputs"

        with open(self.file_path) as reader:
            if not reader.seekable():
                from collections import deque
                yield from deque(reader, n)
            else:
                # 1. seek to end
                cur = reader.seek(0, os.SEEK_END)

                # 2. rewind cur_pos back n lines back
                def rewind_n_lines(cur_pos: int, n: int) -> int:
                    remaining = cur_pos

                    while remaining > 0:
                        cur_pos -= self.chunksize

                        if cur_pos < 0:
                            cur_pos = 0

                        reader.seek(cur_pos)
                        chunk = reader.read(self.chunksize)
                        remaining -= len(chunk)

                        n -= chunk.count(os.linesep)
                        
                        if n <= 0 or 0 == remaining:
                            break

                    reader.seek(cur_pos)
                    while n <= 0:
                        # skip lines reversed more than n
                        reader.readline()
                        n += 1
                    
                    return reader.tell()

                reader.seek(rewind_n_lines(cur, n))

                # 3. read lines
                while True:
                    line = reader.readline()
                    if line is not None:
                        yield line
                    else:
                        if not follow:
                            break

                        # follow and wait for new lines
                        try:
                            sleep(self.check_interval)
                        except KeyboardInterrupt:
                            print("-" * 20)
                            exit(0)

if __name__ == '__main__':
    s = Solution(__file__, chunksize=3)
    for line in s.tail():
        print(line, end="")
