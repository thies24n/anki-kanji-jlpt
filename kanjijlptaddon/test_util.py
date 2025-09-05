import unittest
import kanjijlptaddon.util as util

class TestUtilMethods(unittest.TestCase):

    def setUp(self):
        util.reload_kanji_data()

    def test_jlpt_one_kanji(self):
        # 犬 JLPT 4
        kanji = '犬'
        self.assertEqual(util.kanji_to_jlpt(kanji), 4)

    def test_jlpt_two_kanji(self):
        # 愛 JLPT 3
        # 犬 JLPT 4
        # The lowest JLPT is 3
        kanji = '愛犬'
        self.assertEqual(util.kanji_to_jlpt(kanji), 3)

    def test_jlpt_three_kanji(self):
        # 大 JLPT 5
        # 丈 JLPT 0 (apparently...)
        # 夫 JLPT 3
        # The lowest JLPT is 0
        kanji = '大丈夫'
        self.assertEqual(util.kanji_to_jlpt(kanji), 0)

    def test_jlpt_non_kanji(self):
        # Non-kanji are assigned easiest JLPT/grade
        kanji = 'マルチがありますか。 Yes!'
        self.assertEqual(util.kanji_to_jlpt(kanji), 5)

    def test_jlpt_mixed_kana_kanji(self):
        #　停 JLPT 2
        kanji = 'バス停'
        self.assertEqual(util.kanji_to_jlpt(kanji), 2)

if __name__ == '__main__':
    unittest.main()