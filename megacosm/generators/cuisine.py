#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Cuisine may be specific to a region or named after the creator. """

import logging
from megacosm.generators.generator import Generator
from megacosm.generators.npc import NPC
from megacosm.generators.region import Region


class Cuisine(Generator):

    """ What meals are common in your area? """

    def __init__(self, redis, features={}):
        Generator.__init__(self, redis, features)
        self.logger = logging.getLogger(__name__)

        # You never know if you'll want a creator for your meal

        if not hasattr(self, 'creator'):
            setattr(self, 'creator', NPC(self.redis))

        if not hasattr(self, 'region'):
            setattr(self, 'region', Region(self.redis))

        # Double parse the template to fill in templated template values.

        if not hasattr(self, 'text'):
            self.text = self.render_template(self.template)
            self.text = self.render_template(self.text)

        # remember to capitalize!

        self.text = self.text[0].capitalize() + self.text[1:]

    def __str__(self):
        return self.text
