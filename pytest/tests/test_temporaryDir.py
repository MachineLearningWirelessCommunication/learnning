import pytest


class TestTempDir:
    """tmpdir 的作用是: 在本地生成临时文件夹，并返回文件对象"""

    def test_tempDir(self, tmpdir):
        print(tmpdir)


if __name__ == '__main__':
    pytest.main(['-sv', 'test_tempDir.py'])
