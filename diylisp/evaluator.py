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

#definitely handier to split functions and have the evaluator call the separate funcitons
#I'll leave what I did for last assignment as it was though.
#I didn't do the tests all in order. I chose the ones I understand.

def evaluate(ast, env):
    """Evaluate an Abstract Syntax Tree in the specified environment."""

    if is_boolean(ast) or is_integer(ast):
        return = ast
    else:
        raise Error("Wrong input: input must be boolean or integer")
    if ast[0] == 'quote':
        value = ast[1]
    elif ast[0] == 'atom':
        value = is_atom(ast[1])
    elif ast[0] == 'eq':
        value = is_atom(evaluate(ast[1])) == is_atom(evaluate(ast[2]))
    elif is_integer(ast[1]) and is_integer(ast[2]):
        if ast.op == '+':
            value = evaluate(ast[1], env) + evaluate(ast[2], env)
        elif ast.op == '-':
            value = evaluate(ast[1], env) - evaluate(ast[2], env)
        elif ast.op == '*':
            value = evaluate(ast[1], env) * evaluate(ast[2], env)
        elif ast.op == '/':
            value = evaluate(ast[1], env) / evaluate(ast[2], env)
        elif ast.op == '%':
            value = evaluate(ast[1], env) % evaluate(ast[2], env)
        elif ast.op == '>':
            value = evaluate(ast[1], env) > evaluate(ast[2], env)
    elif ast[0] == 'if':
        if not is_boolean(ast[1]):
            return 'Error: expected the statement to evaluate to a boolean'
        if is_boolean(ast[1]):
            if ast[2] == True:
                value = evaluate(ast[2], env)
            else:
                value = evaluate(ast[3], env)
    elif ast[0] == 'def' :
        value = evalDef(ast[1:], env)
    elif ast[0] == 'lambda' :
        value = evalLam(ast[1:], env)
    elif ast[0] == 'cons':
        value = evalCons(ast[1:], env)
    elif ast[0] == 'head':
        value = evalHead(ast[1:], env)
    elif ast[0] == 'tail':
        value = evalTail(ast[1:], env)
    elif ast[0] == 'empty':
        value = evalEmpty(ast[1:], env)

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
    params = ast[0]
    body = ast[1]
    if is_list(params):
        #rest of function
        #should return some value..
    else:
        raise LispError("parameters not a list")

def evalCons(ast, env):



def evalHead(ast, env):
    headTail = evaluate(ast[0])
    return headTail[0]

def evalTail(ast, env):
    headTail = evaluate(ast[0])
    return headTail[1:]

def evalEmpty(ast, eng):
    emptyList = evaluate(ast[0])
    return emptyList == []

    







    #for the conditional evaluation:
    #somehow that when the if statement does not evaluate to a boolean:
    #give error: expected a boolean for conditional statment
    #when if statement does evaluate to a boolean:
    #give: if conditional evaluates to true: evaluate second part of if statement
    #give: if conditional evaluate to false: evaluate third part of if statement