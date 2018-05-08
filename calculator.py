#! /usr/bin/python3

'''
Implement an expression evaluator which supports only addition and multiplication in Java (preferably), or another language.
The expression can have only digits, plus and multiplication symbols, and optional white-space.
Optionally consider optimizing the algorithm for better performance.
For example, calculate the result of “5 * 4 + 12”.
'''

import re

def f(e):
  rxm = r'([0-9]+\s\*\s[0-9]+)'
  rxa = r'(\+\s[0-9]+\s?\w[^*])'
  mt = 0
  at = 0
  
  p = re.compile(rxm)
  m = p.findall(e)

  for me in m:
    tmp = me.split('*')
    cmt = 1 
    print('tmpm=', tmp)
    
    for j in tmp:
      cmt *= int(j)
      
    mt += cmt
  
  p = re.compile(rxa)
  m = p.findall(e)
  me2s = []
  print('ms=', m)
  
  for me in m:
    me2s = me.split('+')

    for j in me2s:
      if len(j) > 0 and not j == ' ':
        at += int(j)
    print('at=', at)

  return mt + at

if __name__ == '__main__':
  print('SUM=', f('1 * 2 + 1000 + 2000 + 3 * 4 + 3000 + 5 * 6 + 4000 + 5000 ')) 
 
