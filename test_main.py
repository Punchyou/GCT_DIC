#Unit testing for GCT
#testing main fil
import unittest
import HARM_consonanceChordRecognizer_func
import HARM_findPitchClassesfromChord_func as fpc
import HARM_takeOnlyUniqueValuesfromPitchClasses_func as huv
import HARM_findSubsets_func as hfs
import HARM_findConsonantSequencesOfSubsets_func as hcss
import HARM_findMaximalConsonantSubsets_func as hmcs
import HARM_findExtentions_func as fx
import HARM_shortestFormOfSubsets_func as sf
consWeights = [1,0,0,1,1,1,0,1,1,1,0,0]

class Test_GCTs(unittest.TestCase):
    #first test the main functin that gives the final chord form: HARM_consonanceChordRecognizer
    '''def test_HARM_consonanceChordRecogniser(self):
        self.assertEqual([[0, [0, 4, 7], []]], HARM_consonanceChordRecognizer_func.HARM_consonanceChordRecognizer([60, 64, 67, 72], consWeights), msg="False GCT for [60, 64, 67, 72]")
        self.assertEqual([[5, [0, 4, 7], []]], HARM_consonanceChordRecognizer_func.HARM_consonanceChordRecognizer([65, 60, 57, 65], consWeights), msg='False GCT for [65, 60, 57, 65]')
        #needs moderation after learning
        #self.assertEqual([[4, [0, 3], [9]], [1, [0, 3], [6]]], HARM_consonanceChordRecognizer_func.HARM_consonanceChordRecognizer([52, 61, 67, 79], consWeights), msg = 'False GCT for [64, 61, 67, 67]')
        self.assertEqual([[2, [0, 3, 7], []]], HARM_consonanceChordRecognizer_func.HARM_consonanceChordRecognizer([62, 62, 57, 65], consWeights), msg = 'False GCT for [62, 62, 57, 65]')
        self.assertEqual([[9, [0, 4, 7], []]], HARM_consonanceChordRecognizer_func.HARM_consonanceChordRecognizer([57, 61, 57, 64], consWeights), msg = 'False GCT for [57, 61, 57, 64]')
        self.assertEqual([[2, [0, 3, 7], []]], HARM_consonanceChordRecognizer_func.HARM_consonanceChordRecognizer([65, 74, 57, 74], consWeights), msg = 'False GCT for [65, 74, 57, 74]')
        self.assertEqual([[4, [0,4,7], []]], HARM_consonanceChordRecognizer_func.HARM_consonanceChordRecognizer([64, 59, 68, 64], consWeights), msg = 'False GCT for [64, 59, 68, 64]')
        #needs moderations after learning
        self.assertEqual([[10, [0], [2]], [0, [0], [10]]], HARM_consonanceChordRecognizer_func.HARM_consonanceChordRecognizer([60, 72, 82], consWeights), msg = 'False GCT for [60, 72, 82]')
        self.assertEqual([[7, [0, 5], [10]], [0, [0, 5], [7]]], HARM_consonanceChordRecognizer_func.HARM_consonanceChordRecognizer([60, 65, 67], consWeights), msg = 'False GCT for [60, 65, 67]')
        self.assertEqual([[10, [0, 5], [14]], [0, [0, 3], [10]]], HARM_consonanceChordRecognizer_func.HARM_consonanceChordRecognizer([60, 63, 70], consWeights), msg= 'False GCT for [60, 63, 70]')
        
        #FALSE for two two-note-chords
        self.assertEqual([[0, [0, 7], []]], HARM_consonanceChordRecognizer_func.HARM_consonanceChordRecognizer([60, 67], consWeights), msg='False GCT for [60, 67]')
        self.assertEqual([5, [0,7], []], HARM_consonanceChordRecognizer_func.HARM_consonanceChordRecognizer([60, 65], consWeights), msg= 'False GCT for [60, 65]')
        self.assertEqual([[10, [0, 5], [14]], [0, [0, 3], [10]]], HARM_consonanceChordRecognizer_func.HARM_consonanceChordRecognizer([60, 63, 70], consWeights), msg='False GCT for [60, 63, 70]')
        self.assertEqual([[0, [0], []]], HARM_consonanceChordRecognizer_func.HARM_consonanceChordRecognizer([60,72], consWeights), msg='False GCT for [60,72]')
        self.assertEqual([[10, [0], [2]], [0, [0], [10]]], HARM_consonanceChordRecognizer_func.HARM_consonanceChordRecognizer([60, 70, 60], consWeights), msg='False GCT for [60, 70, 60]')'''

    #test the function that finds the possible subsets of a set of pitches in a chord: HARM_findSubsets
    def test_HARM_findPitchClassesfromChord(self):
        self.assertEqual([0, 4, 7, 0], fpc.HARM_findPitchClassesfromChord([60, 64, 67, 72]), msg='False pitch classes for [60, 64, 67, 72]')
        self.assertEqual([5, 0, 9, 5], fpc.HARM_findPitchClassesfromChord([65, 60, 57, 65]), msg='False pitch classes for [65, 60, 57, 65]')
        self.assertEqual([9, 1, 9, 4], fpc.HARM_findPitchClassesfromChord([57, 61, 57, 64]), msg='False pitch classes for [57, 61, 57, 64]')

    #test the function that finds the only the unique values of a list of pitches
    def test_HARM_takeOnlyUniqueValuesfromPitchClasses(self):
        self.assertEqual([0], huv.HARM_takeOnlyUniqueValuesfromPitchClasses([0, 0, 0]), msg="HARM_takeOnlyUniqueValuesfromPitches doesn't return unique values with same values given  given")
        self.assertEqual([5, 6], huv.HARM_takeOnlyUniqueValuesfromPitchClasses([5, 5, 5, 5, 6]), msg="HARM_takeOnlyUniqueValuesfromPitches doesn't return unique values when two diferent values are given")
        self.assertEqual([1,2,3,4,5], huv.HARM_takeOnlyUniqueValuesfromPitchClasses([1,3,2,4,5,5,4,3,2,1,1,1]), msg="HARM_takeOnlyUniqueValuesfromPitches doesn't return unique values")
    
    #test the function that finds all possible subset combintations out of the pitch classes of a chord
    def test_HARM_findSubsets(self):
        self.assertEqual([[0]], hfs.HARM_findSubsets([0]), msg="HARM_findSubsets doesn't return right if one value list is given")
        self.assertEqual([[0,5], [5], [0]], hfs.HARM_findSubsets([0,5]), msg="HARM_findSubsets doesn't return right subsets if two values in the list are given ")
        self.assertEqual([[0, 4, 7], [4, 7], [0, 7], [0, 4], [7], [4], [0]], hfs.HARM_findSubsets([0,4,7]), msg="HARM_findSubsets doesn't return right subsets for [0,4,7]")
        self.assertEqual([[0, 5, 9], [0, 9], [5, 9], [0, 5], [9], [0], [5]], hfs.HARM_findSubsets([5, 0, 9]), msg="HARM_findSubsets doesn't return right subs")
        self.assertEqual([[0, 5, 9, 10], [0, 9, 10], [5, 9, 10], [0, 5, 10], [0, 5, 9], [9, 10], [0, 10], [0, 9], [5, 10], [5, 9], [0, 5], [10], [9], [0], [5]], hfs.HARM_findSubsets([5, 0, 9, 10]), msg="HARM_")

    #test the function that finds the consonant subsets, so the consonant intervals between notes in a chord
    def test_HARMfindConsonantSequenceOfSubsets(self):
        self.assertEqual([[0, 4, 7], [4, 7], [0, 7], [0, 4], [7], [4], [0]], hcss.HARM_findConsonantSequencesOfSubsets(consWeights, [[0, 4, 7], [4, 7], [0, 7], [0, 4], [7], [4], [0]]), msg="HARM_findConsonantSequenceodSubsets doesn't find the consonat subsets")
        self.assertEqual([[0, 5, 9], [5, 9], [0, 5], [0, 9], [5], [9], [0]], hcss.HARM_findConsonantSequencesOfSubsets(consWeights, [[0, 5, 9], [5, 9], [0, 5], [0, 9], [5], [9], [0]]), msg = "HARM_findConsonantSequenceodSubsets doesn't find the consonat subsets")
        self.assertEqual([[3, 10], [0, 3], [3], [10], [0]], hcss.HARM_findConsonantSequencesOfSubsets(consWeights, [[0, 3, 10], [3, 10], [0, 3], [0, 10], [3], [10], [0]]), msg = "HARM_findConsonantSequenceodSubsets doesn't find the consonat subsets")

    #test the function that keeps only the longest of the consonant subsets, cause that's the chord type (without the extentions)
    def test_HARM_findMaximalConsonantSubsets(self):
        self.assertEqual([[0, 4, 7]], hmcs.HARM_findMaximalConsonantSubsets([[0, 4, 7], [4, 7], [0, 7], [0, 4], [7], [4], [0]]), msg = "HARM_findMaximalConsonantSubsets doesn't return maximal")
        self.assertEqual([[0, 5, 9]], hmcs.HARM_findMaximalConsonantSubsets([[0, 5, 9], [5, 9], [0, 5], [0, 9], [5], [9], [0]]), msg = "HARM_findMaximalConsonantSubsets doesn't return maximal")
        self.assertEqual([[3, 10], [0, 3]], hmcs.HARM_findMaximalConsonantSubsets([[3, 10], [0, 3], [3], [10], [0]]), msg = "HARM_findMaximalConsonantSubsets doesn't return maximal")

    #test the function that finds the extentions of the chord
    def test_HARM_findExtentions(self):
        self.assertEqual([[10]], fx.HARM_findExtentions([0,4,7,10],[[0,4,7]]), msg = "HARM_findExtentions doen't return extention")
        self.assertEqual([[2]], fx.HARM_findExtentions([0,2,4,7], [[0,4,7]]), msg = "HARM_findExtentions doesn't return extention")
        self.assertEqual([[5 ,8, 10, 17]], fx.HARM_findExtentions([1,2,5,7,8,10,17], [[1,2,7]]), msg="HARM_findExtentions doesn't return extentions")

    #test the function that creates the shortest form of the chord (the most "closed" form)
    def test_HARM_shortestFormOfSubsets(self):
        self.assertEqual([[[1,2,3]]], sf.HARM_shortestFormOfSubsets([[3,1,2]]), msg="HARM_shortestFormOfSubsets doesn't return the shortest form")
        self.assertEqual([[[10,1]]], sf.HARM_shortestFormOfSubsets([[1,10]]), msg = "HARM_shortestFormOfSubsets doesn't return the shortest form for two items")

    #

# run the tests in IDE
if __name__ == '__main__':
    unittest.main()