from queue import Queue
from time import time
data="38006F45291200"
_data="D2FE28"
data="EE00D40C823060"
_data = "A0016C880162017C3686B18A3D4780"
data="8A004A801A8002F478"
data="620080001611562C8802118E34"
data="C0015000016115A2E0802F182340"
data="A0016C880162017C3686B18A3D4780"
data="40541D900AEDC01A88002191FE2F45D1006A2FC2388D278D4653E3910020F2E2F3E24C007ECD7ABA6A200E6E8017F92C934CFA0E5290B569CE0F4BA5180213D963C00DC40010A87905A0900021B0D624C34600906725FFCF597491C6008C01B0004223342488A200F4378C9198401B87311A0C0803E600FC4887F14CC01C8AF16A2010021D1260DC7530042C012957193779F96AD9B36100907A00980021513E3943600043225C1A8EB2C3040043CC3B1802B400D3CA4B8D3292E37C30600B325A541D979606E384B524C06008E802515A638A73A226009CDA5D8026200D473851150401E8BF16E2ACDFB7DCD4F5C02897A5288D299D89CA6AA672AD5118804F592FC5BE8037000042217C64876000874728550D4C0149F29D00524ACCD2566795A0D880432BEAC79995C86483A6F3B9F6833397DEA03E401004F28CD894B9C48A34BC371CF7AA840155E002012E21260923DC4C248035299ECEB0AC4DFC0179B864865CF8802F9A005E264C25372ABAC8DEA706009F005C32B7FCF1BF91CADFF3C6FE4B3FB073005A6F93B633B12E0054A124BEE9C570004B245126F6E11E5C0199BDEDCE589275C10027E97BE7EF330F126DF3817354FFC82671BB5402510C803788DFA009CAFB14ECDFE57D8A766F0001A74F924AC99678864725F253FD134400F9B5D3004A46489A00A4BEAD8F7F1F7497C39A0020F357618C71648032BB004E4BBC4292EF1167274F1AA0078902262B0D4718229C8608A5226528F86008CFA6E802F275E2248C65F3610066274CEA9A86794E58AA5E5BDE73F34945E2008D27D2278EE30C489B3D20336D00C2F002DF480AC820287D8096F700288082C001DE1400C50035005AA2013E5400B10028C009600A74001EF2004F8400C92B172801F0F4C0139B8E19A8017D96A510A7E698800EAC9294A6E985783A400AE4A2945E9170"
bits = ""
lookup={
"0" : "0000",
"1" : "0001",
"2" : "0010",
"3" : "0011",
"4" : "0100",
"5" : "0101",
"6" : "0110",
"7" : "0111",
"8" : "1000",
"9" : "1001",
"A" : "1010",
"B" : "1011",
"C" : "1100",
"D" : "1101",
"E" : "1110",
"F" : "1111"
    }

bits = Queue()
for c in data:
    for b in lookup[c]:
        bits.put(b)

print(bits)


versions=[]    


def read_literal(q):
    s=""
    cont = "1"
    while cont == "1":
        cont = q.get_nowait()
        s+=q.get_nowait()
        s+=q.get_nowait()
        s+=q.get_nowait()
        s+=q.get_nowait()

    #while q.qsize()%4!=0:
     #    q.get_nowait()
   
    return int(s,2)


def read_to_int(q,length):
  
    s=""
    for _ in range(length):
        s+=q.get_nowait()


    
    i = int(s,2)

    return i


def read_packet(q, d=0):
    print("".join(q.queue))
    version = read_to_int(q, 3)
    versions.append(version)
    type_id = read_to_int(q, 3)
    print(" "*d, version, type_id)
    if type_id ==4:
        print(" "*d,"Literal:")
        value = read_literal(q)
        print(" "*d,value)    else:
        print(" "*d,"Operator:")
        length_type_id = q.get_nowait()
        if length_type_id == "0":
            
            total_length_in_bits = read_to_int(q,15)
            print(" "*d, "total_lenth",total_length_in_bits)
            sq = Queue()
            for _ in range(total_length_in_bits):
                sq.put(q.get_nowait())
            while not sq.empty():
  
                read_packet(sq, d+1)
        else:
            num_of_subpackets =  read_to_int(q,11)
            print(" "*d, "num_of_subpackets",num_of_subpackets)
            for _ in range(num_of_subpackets):
                read_packet(q, d+1)
             


read_packet(bits)    
print(versions)
print(sum(versions))
