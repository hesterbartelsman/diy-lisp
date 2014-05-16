# -*- coding: utf-8 -*-

from types import Environment, LispError, Closure
from ast import is_boolean, is_atom, is_symbol, is_list, is_closure, is_integer
from asserts import assert_exp_length, assert_valid_definition, assert_boolean
from parser import unparse

#definitely not final version. Haven't done anything with the environment yet...
"""
This is the Evaluator module. The `evaluate` function below is the heart
of your language, and the focus for most of parts 2 through 6.

A score of useful functions is provided for you, as per the above imports, 
making your work a bit easier. (We're supposed to get through this thing 
in a day, after all.)
"""

def evaluate(ast, env):
    """Evaluate an Abstract Syntax Tree in the specified environment."""
    left_value = ast.left.evaluate(env)
    right_value = self.right.evaluate(env)
    if is_boolean()
    if ast[0] == 'quote':
        return ast[1]
    if ast[0] == 'atom':
        return is_atom(ast[1])
    if ast[0] == 'eq':
        value = left_value == right_value
    if is_integer(left_value) and is_integer(right_value):
        if ast.op == '+':
            value = left_value + right_value
        elif ast.op == '-':
            value = left_value - right_value
        elif ast.op == '*':
            value = left_value * right_value
        elif ast.op == '/':
            value = left_value / right_value
        elif ast.op == '%'
            value = left_value % right_value
        elif ast.op == '>'
            value = left_value > right_value
    else:
        raise NotImplementedError("DIY")
    return value


def evaluate(ast, env):
    """Evaluate an Abstract Syntax Tree in the specified environment."""
    left_value = ast.left.evaluate(env)
    right_value = self.right.evaluate(env)
    if is_boolean()
    if ast[0] == 'quote':
        return ast[1]
    if ast[0] == 'atom':
        return is_atom(ast[1])
    if ast[0] == 'eq':
        value = ast[1] == ast[2]
    if is_integer(ast[1]) and is_integer(ast[2]):
        if ast.op == '+':
            value = ast[1] + ast[2]
        elif ast.op == '-':
            value = ast[1] - ast[2]
        elif ast.op == '*':
            value = ast[1] * ast[2]
        elif ast.op == '/':
            value = ast[1] / ast[2]
        elif ast.op == '%'
            value = ast[1] % ast[2]
        elif ast.op == '>'
            value = ast[1] > ast[2]
    else:
        raise NotImplementedError("DIY")
    return value