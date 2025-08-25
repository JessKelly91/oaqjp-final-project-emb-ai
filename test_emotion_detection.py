"""
Unit Tests for Emotion Detection Module

This module contains unit tests for the emotion_detector function to ensure
it correctly identifies dominant emotions in various text inputs.
"""

import unittest
from emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """
    Test cases for the emotion_detector function.
    
    This test class validates that the emotion detection function correctly
    identifies the dominant emotion for various emotional text inputs including
    joy, anger, disgust, sadness, and fear.
    """
    def test_emotion_detector(self):
        """
        Test the emotion_detector function with various emotional text inputs.
        
        This test verifies that the emotion_detector function correctly identifies
        the dominant emotion for different types of emotional expressions:
        - Joy: positive, happy expressions
        - Anger: mad, frustrated expressions  
        - Disgust: repulsed, disgusted expressions
        - Sadness: sad, melancholic expressions
        - Fear: afraid, scared expressions
        
        Each assertion checks that the dominant_emotion key in the returned
        dictionary matches the expected emotion for the given text.
        """
        self.assertEqual(emotion_detector('I am glad this happened').get('dominant_emotion'), 'joy')
        self.assertEqual(emotion_detector('I am really mad about this').get('dominant_emotion'), 'anger')
        self.assertEqual(emotion_detector('I feel disgusted just hearing about this').get('dominant_emotion'), 'disgust')
        self.assertEqual(emotion_detector('I am so sad about this').get('dominant_emotion'), 'sadness')
        self.assertEqual(emotion_detector('I am really afraid that this will happen').get('dominant_emotion'), 'fear')

if __name__ == '__main__':
    unittest.main()