"""Automated validation tests for Prachi Zala's Portfolio Website.

Validates semantic HTML5 structure, SEO/OpenGraph meta tags,
accessibility (a11y), and internal asset integrity using Python standard library.
"""

import os
import unittest
from html.parser import HTMLParser

PORTFOLIO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX_PATH = os.path.join(PORTFOLIO_DIR, "index.html")


class HTMLValidator(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        self.meta = {}
        self.images = []
        self.links = []
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        attr_dict = dict(attrs)
        self.tags.append((tag, attr_dict))

        if tag == "meta":
            name = attr_dict.get("name") or attr_dict.get("property")
            if name:
                self.meta[name.lower()] = attr_dict.get("content", "")

        if tag == "img":
            self.images.append(attr_dict)

        if tag == "a":
            self.links.append(attr_dict)

        if "id" in attr_dict:
            self.ids.add(attr_dict["id"])


class TestPortfolio(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not os.path.exists(INDEX_PATH):
            raise FileNotFoundError(f"index.html not found at {INDEX_PATH}")
        with open(INDEX_PATH, "r", encoding="utf-8") as f:
            cls.content = f.read()
        cls.parser = HTMLValidator()
        cls.parser.feed(cls.content)

    def test_index_file_exists_and_not_empty(self):
        self.assertGreater(len(self.content.strip()), 500, "index.html is unexpectedly small or empty")

    def test_essential_meta_tags(self):
        self.assertIn("viewport", self.parser.meta, "Missing responsive viewport meta tag")
        self.assertIn("description", self.parser.meta, "Missing description meta tag for SEO")
        self.assertIn("author", self.parser.meta, "Missing author meta tag")

    def test_open_graph_social_cards(self):
        self.assertIn("og:title", self.parser.meta, "Missing og:title OpenGraph tag")
        self.assertIn("og:description", self.parser.meta, "Missing og:description OpenGraph tag")
        self.assertIn("og:type", self.parser.meta, "Missing og:type OpenGraph tag")

    def test_semantic_sections_exist(self):
        tags = [t[0] for t in self.parser.tags]
        self.assertTrue("header" in tags or "nav" in tags, "Missing semantic header or nav element")
        self.assertTrue("main" in tags or "section" in tags, "Missing main or section tags")
        self.assertIn("footer", tags, "Missing semantic footer tag")

    def test_image_accessibility_alt_attributes(self):
        for img in self.parser.images:
            self.assertIn("alt", img, f"Image missing required alt attribute for screen readers: {img}")

    def test_internal_anchor_integrity(self):
        for link in self.parser.links:
            href = link.get("href", "")
            if href.startswith("#") and len(href) > 1:
                target_id = href[1:]
                self.assertIn(target_id, self.parser.ids, f"Internal anchor #{target_id} has no matching element ID")

    def test_resume_file_present(self):
        resume_path = os.path.join(PORTFOLIO_DIR, "resume.pdf")
        self.assertTrue(os.path.exists(resume_path), "resume.pdf file is missing from portfolio root")
        self.assertGreater(os.path.getsize(resume_path), 1000, "resume.pdf appears corrupt or empty")


if __name__ == "__main__":
    unittest.main()
