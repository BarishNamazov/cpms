#!/usr/bin/env python3

# Contest Practice Management System - https://github.com/BarishNamazov/cpms/
# Copyright © 2022 Abutalib Barish Namazov <abutalib.namazov@hotmail.com>
#
# Some code snippets have been taken and readapted from CMS. 
# For such pieces this copyright applies:
#
# Contest Management System - http://cms-dev.github.io/
# Copyright © 2016 Stefano Maggiolo <s.maggiolo@gmail.com>
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

"""C programming language definition."""

from cpms.grading import CompiledLanguage


__all__ = ["C11Gcc"]


class C11Gcc(CompiledLanguage):
    """This defines the C programming language, compiled with gcc (the
    version available on the system) using the C11 standard.

    """

    @property
    def name(self):
        """See Language.name."""
        return "C11 / gcc"

    @property
    def source_extensions(self):
        """See Language.source_extensions."""
        return [".c"]

    @property
    def header_extensions(self):
        """See Language.source_extensions."""
        return [".h"]

    @property
    def object_extensions(self):
        """See Language.source_extensions."""
        return [".o"]

    def get_compilation_commands(self,
                                 source_filenames, executable_filename,
                                 for_evaluation=True):
        """See Language.get_compilation_commands."""
        command = ["/usr/bin/gcc"]
        if for_evaluation:
            command += ["-DEVAL"]
        command += ["-std=gnu11", "-O2", "-pipe", "-static",
                    "-s", "-o", executable_filename]
        command += source_filenames
        command += ["-lm"]
        return [command]
