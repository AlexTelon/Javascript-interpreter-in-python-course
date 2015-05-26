#!/usr/bin/env python3

import sys
import os
import subprocess

class TestFailedExecption(Exception):
  def __init__(self, testname, line, jspy_line, test_line, jspy_output):
    super().__init__("Test '{}' has failed at line {}:\n=================\n{}=================\n\nes.py: {}\ntest : {}".format(testname, line, jspy_output, jspy_line, test_line))

class Options:
  def __init__(self, executable, test_dir):
    self.executable = executable
    self.test_dir   = test_dir
    self.verbose    = True
    self.abort      = True
    
def runTest(test, options):
  print(test)
  
  proc = subprocess.Popen([options.executable, options.test_dir + "/" + test + ".js"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

  f = open(options.test_dir + "/" + test + ".txt")
  i = 1
  success = True
  jspy_output = ""
  
  for line in proc.stdout:
    jso           = line.decode("utf-8")
    jspy_output  += jso
    jso           = jso.strip('\n')
    tso           = f.readline().strip('\n')
    
    if(tso != jso):
      success = False
      if(options.verbose):
        print("Difference in ouptput at line: {}".format(i))
        print("es.py: {}".format(jso))
        print("test : {}".format(tso))
      if(options.abort):
        for line in proc.stdout:
          o             = line.decode("utf-8")
          jspy_output  += o
        raise TestFailedExecption(test, i, jso, tso, jspy_output)
    i += 1
  
  next_test_line = f.readline()
  
  if(len(next_test_line) != 0):
    success = False
    if(options.verbose):
      print("Test data has more than the script output!")
    if(options.abort):
      raise TestFailedExecption(test, i, "", next_test_line, jspy_output)
  for line in f:
    print(line[0])
  f.close()
  return success

def main(argv):
  exec = argv[1]
  lab  = argv[2]

  options = Options(argv[1], argv[2] + "/Tests")
  
  if(len(argv) == 4):
    runTest(argv[3], options)
  else:
    
    tests = []
    for root, dirs, files in os.walk( options.test_dir ):
      for f in files:
        full = (root + '/' + f)
        full = full[len(options.test_dir) + 1:]
        if(full.endswith(".txt")):
          testname = full[0:len(full)-4]
        elif(full.endswith(".js")):
          testname = full[0:len(full)-3]
        else:
          raise Exception("Invalid file: " + full)
        if(not testname in tests):
          tests.append(testname)
    if(len(tests) == 0):
      raise Exception("Empty test suite")

    tests.sort()

    for test in tests:
      runTest(test, options)

if __name__ == '__main__':
  main(sys.argv)
