#!/usr/bin/env python
# -*- coding: utf-8 -*-

import PyGithub

def issue_state(number,provider,issue_type):
  def _issue_state(func):
    return func(number,provider,issue_type)
  return _issue_state

