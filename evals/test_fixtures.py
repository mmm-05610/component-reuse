"""Checks synthetic evaluation facts, NOT an Agent/Skill behavior evaluation."""

import pathlib
import runpy
import unittest


class FixtureFacts(unittest.TestCase):
    def setUp(self):
        root = pathlib.Path(__file__).parent / "fixtures"
        self.upstream = runpy.run_path(str(root / "upstream.py"))
        self.consumer = runpy.run_path(str(root / "consumer.py"))

    def test_requires_external_initialization(self):
        with self.assertRaisesRegex(RuntimeError, "initialization required"):
            self.upstream["Store"]().put("key", "value")

    def test_instances_share_state(self):
        self.upstream["initialize_product"]()
        first, second = self.upstream["Store"](), self.upstream["Store"]()
        first.put("key", "first")
        self.assertEqual(second.get("key"), "first")

    def test_cancelled_write_still_has_a_side_effect(self):
        self.upstream["initialize_product"]()
        instance = self.upstream["Store"]()
        self.assertFalse(instance.put("cancelled", "value", cancelled=True))
        self.assertEqual(instance.get("cancelled"), "value")

    def test_close_does_not_revoke_writes(self):
        self.upstream["initialize_product"]()
        instance = self.upstream["Store"]()
        instance.close()
        self.assertTrue(instance.put("late", "value"))

    def test_pure_validation_is_independently_usable(self):
        self.assertEqual(self.upstream["validate_pair"]("a", "b"), ("a", "b"))
        with self.assertRaises(TypeError):
            self.upstream["validate_pair"]("a", 1)

    def test_unchanged_candidate_fails_the_actual_consumer(self):
        self.upstream["initialize_product"]()
        with self.assertRaises(AssertionError):
            self.consumer["exercise_required_behavior"](self.upstream["Store"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
