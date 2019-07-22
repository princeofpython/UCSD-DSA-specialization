# python3
import sys
import numpy

def build_suffix_array(text):
  """
  Build suffix array of the string text and
  return a list result of the same length as the text
  such that the value result[i] is the index (0-based)
  in text where the i-th lexicographically smallest
  suffix of text starts.
  """
  result = []
  #for i in range(len(text)):
    #result.append(text[i:])
  # Implement this function yourself
  #return numpy.argsort(result)
  return [each[1] for each in sorted([(text[i:], i) for i in range(len(text))])]


if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  print(" ".join(map(str, build_suffix_array(text))))
