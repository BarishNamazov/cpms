#!/usr/bin/env python3

# Contest Practice Management System - https://github.com/BarishNamazov/cpms/
# Copyright © 2022 Abutalib Barish Namazov <abutalib.namazov@hotmail.com>
#
# Some code snippets have been taken and readapted from CMS. 
# For such pieces this copyright applies:
#
# Contest Management System - http://cms-dev.github.io/
# Copyright © 2016-2017 Stefano Maggiolo <s.maggiolo@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""PHP programming language definition."""

from cpms.grading import Language


__all__ = ["Php"]


class Php(Language):
    """This defines the PHP programming language, interpreted with the
    standard PHP interpreter available in the system.

    """

    @property
    def name(self):
        """See Language.name."""
        return "PHP"

    @property
    def source_extensions(self):
        """See Language.source_extensions."""
        return [".php"]

    @property
    def executable_extension(self):
        """See Language.executable_extension."""
        return ".php"

    def get_compilation_commands(self,
                                 source_filenames, executable_filename,
                                 for_evaluation=True):
        """See Language.get_compilation_commands."""
        if source_filenames[0] != executable_filename:
            return [["/bin/cp", source_filenames[0], executable_filename]]
        else:
            # We need at least one command to collect execution stats.
            return [["/bin/true"]]

    def get_evaluation_commands(
            self, executable_filename, main=None, args=None):
        """See Language.get_evaluation_commands."""
        args = args if args is not None else []
        return [["/usr/bin/php", executable_filename] + args]
