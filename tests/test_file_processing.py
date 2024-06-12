import unittest
import tempfile
import os
from gui import read_and_process_file  # 替换为实际的模块名

class TestReadAndProcessFile(unittest.TestCase):

    def test_read_plain_english_file(self):
        content = "Hello world\nThis is a test."
        with tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8') as f:
            f.write(content)
            file_path = f.name

        result = read_and_process_file(file_path)
        expected = "hello world this is a test"
        self.assertEqual(result, expected)
        os.remove(file_path)

    def test_read_non_ascii_file(self):
        content = "Hello world\n这是一个测试。"
        with tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8') as f:
            f.write(content)
            file_path = f.name

        result = read_and_process_file(file_path)
        expected = "hello world"
        self.assertEqual(result, expected)
        os.remove(file_path)

    def test_read_mixed_encoding_file(self):
        content = "Hello world\n¡Hola mundo!"
        with tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='latin-1') as f:
            f.write(content)
            file_path = f.name

        result = read_and_process_file(file_path)
        expected = "hello world hola mundo"
        self.assertEqual(result, expected)
        os.remove(file_path)

if __name__ == '__main__':
    unittest.main()
