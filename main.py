def showmenu():
  print("1. Citire lista")
  print("2. Afișarea părții întregi a tuturor numerelor din listă.")
  print("3. Să se afișeze toate numerele care aparțin unui interval deschis citit de la tastatură.")
  print("4. Afișarea tuturor numerelor a căror parte întreagă este divizor al părții fracționare")
  print("5. Afișarea listei obținute din lista inițială în care numerele sunt înlocuite cu un string format din cuvinte care le descriu caracter cu caracter.")




def read_list():
  floats_as_str = input("Dati o lista de float-uri separate prin spatiu")
  floats_as_list_of_str = floats_as_str.split(' ')
  floats = []
  for float_str in floats_as_list_of_str:
    floats.append(float(float_str))

  return floats


def parte_intreaga(list):
  """
  Determina afișarea părții întregi a tuturor numerelor din listă.
  :param list: lista de float-uri
  :return: o lista cu partea intreaga a nr
  """
  result=[]
  for i in list:
    elem=int(i)
    result.append(elem)
  return result






def interval_deschis(list,st,dr):
  """
  Determina afisarea tuturor nr care aparțin unui interval deschis citit de la tastatură.
  :param list: lista de float-uri
  :param st: capatul din stanga al intervalului
  :param dr: capatul din dreapta al intervalului
  :return: lista cu nr care apartin intervalului
  """
  result=[]
  for i in list:
    if i>st and i<dr:
      result.append(i)
  return result



def main():
  list=[]
  while True:
    showmenu()
    optiune = input("Alegeti optiune")
    if optiune == "1":
      list=read_list()
    elif optiune == "2":
      print(parte_intreaga(list))
    elif optiune == "3":
      st=int(input("Dati capatul din stanga"))
      dr=int(input("Dati capatul din dr"))
      print(interval_deschis(list,st,dr))
    elif optiune == "4":
      





if __name__ == '__main__':
  main()
