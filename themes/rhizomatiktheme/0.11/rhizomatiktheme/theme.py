# Created by duy on 2009-09-16.
# Copyright (c) 2009 duy. All rights reserved.

from trac.core import *

from themeengine.api import ThemeBase

class RhizomatikTheme(ThemeBase):
    """A theme for Trac based on http://www.oswd.org/design/information/id/3465."""

    template = htdocs = css = screenshot = True
    
