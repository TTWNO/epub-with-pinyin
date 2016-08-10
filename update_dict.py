import pynlpir
nlpir = pynlpir.nlpir

f = open('cedict_ts.u8')
pynlpir.open()
for line in f:
    line = line.rstrip('\n')
    nlpir.AddUserWord(bytes(line, encoding='utf-8'))
nlpir.SaveTheUsrDic()
pynlpir.close()
