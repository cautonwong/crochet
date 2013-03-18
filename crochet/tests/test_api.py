"""
Tests for the crochet APIs.
"""

import threading

from twisted.trial.unittest import TestCase
from twisted.internet.defer import succeed, Deferred

from crochet import _Crochet, DeferredResult


class DeferredResultTests(TestCase):
    """
    Tests for DeferredResult.
    """

    def test_success_result(self):
        """
        result() returns the value the Deferred fired with.
        """
        dr = DeferredResult(succeed(123))
        self.assertEqual(dr.result(), 123)

    def test_later_success_result(self):
        """
        result() returns the value the Deferred fired with, in the case where
        the Deferred is fired after result() is called.
        """
        d = Deferred()
        def fireSoon():
            import time; time.sleep(0.01)
            d.callback(345)
        threading.Thread(target=fireSoon).start()
        dr = DeferredResult(d)
        self.assertEqual(dr.result(), 345)

    def test_success_result_twice(self):
        """
        A second call to result() returns same value as the first call.
        """


class InEventLoopTests(TestCase):
    """
    Tests for the in_event_loop decorator.
    """
