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

#definitely handier to split functions and have the evaluator call the seperate funcitons
#I'll leave what I did for last assignment as it was though.


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
            value = evaluate(ast[1], env) + evaluate(ast[2], env)
        elif ast.op == '-':
            value = evaluate(ast[1], env) - evaluate(ast[2], env)
        elif ast.op == '*':
            value = evaluate(ast[1], env) * evaluate(ast[2], env)
        elif ast.op == '/':
            value = evaluate(ast[1], env) / evaluate(ast[2], env)
        elif ast.op == '%'
            value = evaluate(ast[1], env) % evaluate(ast[2], env)
        elif ast.op == '>'
            value = evaluate(ast[1], env) > evaluate(ast[2], env)
    if ast[0] == 'if':
        if not is_boolean(ast[1]):
            return 'Error: expected the statement to evaluate to a boolean'
        if is_boolean(ast[1]):
            if ast[2] == True:
                value = evaluate(ast[2], env)
            else:
                value = evaluate(ast[3], env)
    if ast[0] == 'def' :
        value = evalDef(ast[1:], env)
    if ast[0] == 'lambda' :
        value =
    else:
        raise NotImplementedError("DIY")

    return value

def
def

def evalDef(ast, env):
    assert_valid_definition(ast)
    symbol = ast[0]
    value = evaluate(ast[1],env)
    env.set(symbol,value)
    return symbol

def evalLam(ast, env)
#not sure how to do this...




    







    #for the conditional evaluation:
    #somehow that when the if statement does not evaluate to a boolean:
    #give error: expected a boolean for conditional statment
    #when if statement does evaluate to a boolean:
    #give: if conditional evaluates to true: evaluate second part of if statement
    #give: if conditional evaluate to false: evaluate third part of if statement