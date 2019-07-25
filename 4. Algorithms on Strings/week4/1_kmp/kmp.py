# python3
import sys

def ComputePrefixFunction(P):
  S=[0 for _ in range(len(P))]
  S[0]=0
  border=0
  for i in range(1,len(P)):
    while(border>0) and (P[i] !=P[border]):
      border=S[border-1]
    if P[i]==P[border]:
      border+=1
    else:
      border=0
    S[i]=border
  return S
def find_pattern(pattern, text):
  """
  Find all the occurrences of the pattern in the text
  and return a list of all positions in the text
  where the pattern starts in the text.
  """
    # Implement this function yourself
  new=pattern+'$'+text
  S=ComputePrefixFunction(new)
  result = []
  for i in range(len(pattern), len(new)):
    if S[i]==len(pattern):
      result.append(i-2*len(pattern))
  return result


if __name__ == '__main__':
  pattern = sys.stdin.readline().strip()
  text = sys.stdin.readline().strip()
  result = find_pattern(pattern, text)
  print(" ".join(map(str, result)))

