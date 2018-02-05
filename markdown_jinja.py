#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor
from jinja2 import Environment


class MarkdownJinja(Extension):
    def __init__(self, configs={}):
        self.config = {
            'context_file': ['', 'Default location of JSON file containing template context']
        }
        for key, value in configs.items():
            self.setConfig(key, value)

    def extendMarkdown(self, md, md_globals):
        md.preprocessors.add(
            'jinja', JinjaPreprocessor(md, self.getConfigs()), '_begin'
        )


class JinjaPreprocessor(Preprocessor):
    def __init__(self, md, config):
        super(JinjaPreprocessor, self).__init__(md)
        self.environment = Environment()
        self.context = json.load(open(config['context_file'])) if config['context_file'] else {}

    def run(self, lines):
        text = '\n'.join(lines)
        template = self.environment.from_string(text)
        new_text = template.render(self.context)
        return new_text.split('\n')


def makeExtension(*args,**kwargs):
    return MarkdownJinja(kwargs)
