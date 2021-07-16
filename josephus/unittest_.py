import unittest
from Person import Person
from josephus import JosephusRing
from Reader import ExcelReader, CsvReader, ZipReader

ZIPPATH = 'ADcarry.zip'
ZIP_TARGET_FILE = 'ADcarry/ADcarry.csv'
CSVPATH = 'ADcarry2/ADcarry.csv'
EXCELPATH = 'ADcarry2/ADcarry.xlsx'


class TestPerson(unittest.TestCase):
    def test_init(self):
        self.assertRaises(AssertionError, Person, 'a', 123)
        self.assertIsInstance(Person('阿狸', '123456'), Person)


class TestJsephusRing(unittest.TestCase):
    def setUp(self) -> None:
        obj = CsvReader(CSVPATH)
        self.list_ = obj.read()

    def test_init(self):
        self.assertRaises(AssertionError, JosephusRing, {}, 3, '薇恩')
        self.assertIsInstance(JosephusRing(self.list_, 3, '薇恩'), JosephusRing)

    def test_next(self):        # 迭代器怎么测？？？？
        pass


class TestExcelReader(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = ExcelReader(EXCELPATH)
        self.list_ = self.obj.read()

    def test_init(self):
        self.assertIsInstance(self.obj, ExcelReader)

    def test_read(self):        # read方法测试内容：输出是否为list，还有？
        self.assertIsInstance(self.list_, list)


class TestCsvReader(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = CsvReader(CSVPATH)
        self.list_ = self.obj.read()

    def test_init(self):
        self.assertIsInstance(self.obj, CsvReader)

    def test_read(self):
        pass


class TestZipReader(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = ZipReader(ZIPPATH, ZIP_TARGET_FILE)
        self.list_ = self.obj.read()

    def test_init(self):
        self.assertIsInstance(self.obj, ZipReader)

    def test_read(self):
        pass
