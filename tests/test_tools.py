import copy
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scripts'))
import progress
import validate

class ProgressTests(unittest.TestCase):
    def setUp(self):
        self.defs = progress.definitions()
        self.rows = progress.read_tracker(progress.ROOT/'progress/tracker.csv')
        # Tests are independent of the learner's current progress.
        for r in self.rows:
            r.update(status='not_started', evidence='', reason='', updated_at='')

    def test_initial_frontier(self):
        self.assertEqual(progress.ready_ids(self.rows,self.defs), ['L00'])

    def test_cannot_skip_prerequisite(self):
        with self.assertRaisesRegex(ValueError, 'prerequisites'):
            progress.updated_rows(self.rows,self.defs,'L08','in_progress')

    def test_completion_needs_evidence(self):
        with self.assertRaisesRegex(ValueError, 'evidence'):
            progress.updated_rows(self.rows,self.defs,'L00','completed')

    def test_waiver_is_auditable(self):
        with self.assertRaisesRegex(ValueError, 'reason'):
            progress.updated_rows(self.rows,self.defs,'L00','waived',evidence='old work')
        rows=progress.updated_rows(self.rows,self.defs,'L00','waived',evidence='old work',reason='diagnostic passed')
        self.assertIn('L01',progress.ready_ids(rows,self.defs))

    def test_reopen_cannot_invalidate_active_descendant(self):
        rows=progress.updated_rows(self.rows,self.defs,'L00','completed',evidence='scope')
        rows=progress.updated_rows(rows,self.defs,'L01','in_progress')
        with self.assertRaisesRegex(ValueError, 'prerequisites'):
            progress.updated_rows(rows,self.defs,'L00','not_started')

    def test_csv_roundtrip(self):
        rows=progress.updated_rows(self.rows,self.defs,'L00','in_progress',reason='Unicode café')
        with tempfile.TemporaryDirectory() as folder:
            path=Path(folder)/'tracker.csv'
            progress.save_tracker(path,rows)
            self.assertEqual(rows,progress.read_tracker(path))

    def test_table_dashboard_separates_core_and_optional(self):
        result=progress.markdown_progress(self.rows,self.defs)
        self.assertIn('| Core modules | 0 | 0 | 17 | 0% |',result)
        self.assertIn('| Optional modules | 0 | 0 | 2 | 0% |',result)
        self.assertIn('L00: Baseline Assessment and Product Scope',result)

class RepositoryTests(unittest.TestCase):
    def test_dangling_link_is_caught(self):
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder)
            (root/'README.md').write_text('[broken](missing.md)',encoding='utf-8')
            self.assertEqual(len(validate.markdown_links(root)[1]),1)

    def test_cycle_is_caught(self):
        with self.assertRaisesRegex(ValueError,'cycle'):
            validate.check_graph({'A':{'prerequisites':['B']},'B':{'prerequisites':['A']}})

    def test_repository_contract(self):
        self.assertEqual(validate.validate()['native_topics'],32)

if __name__=='__main__':
    unittest.main()
