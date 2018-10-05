# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

import sys

from wolframclient.cli.utils import SimpleCommand
from wolframclient.utils.importutils import module_path
from wolframclient.utils.require import require


class Command(SimpleCommand):

    modules = ['wolframclient']

    def _module_args(self, *args):

        yield __file__  # autopep main is dropping the first argument

        for module in self.modules:
            yield module_path(module)

        for arg in args:
            yield arg

    @require(('autopep8', '1.4'), ('isort', '4.3.4'), ('autoflake', '1.2'))
    def handle(self, *args):

        # https://pypi.org/project/isort/

        from autoflake import main

        sys.argv = tuple(
            self._module_args(
                '--in-place',
                '--remove-duplicate-keys',
                '--expand-star-import',
                '--remove-all-unused-imports',
                '--recursive'))

        main()

        from isort.main import main

        sys.argv = list(
            self._module_args(
                '-rc',
                '--multi-line',
                '5',
                '-a',
                "from __future__ import absolute_import, print_function, unicode_literals"))

        main()

        from autopep8 import main

        sys.argv = tuple(
            self._module_args(
                '--in-place',
                '--aggressive',
                '--recursive'))

        main()