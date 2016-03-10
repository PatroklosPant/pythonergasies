from bitarray import bitarray
import mmh3
iimport urllib 
 
class BloomFilter:
    
    def __init__(self, size, hash_count):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)
        
    def add(self, string):
        for seed in xrange(self.hash_count):
            result = mmh3.hash(string, seed) % self.size
            self.bit_array[result] = 1
            
    def lookup(self, string):
        for seed in xrange(self.hash_count):
            result = mmh3.hash(string, seed) % self.size
            if self.bit_array[result] == 0:
                return "--%s--" %(lista[i])
        return "Probably"
 
bf = BloomFilter(500000, 7)

urlsel="https://gunet2.cs.unipi.gr/modules/document/file.php/TMA111/american-english.txt"
keimeno = urllib.urlopen(urlsel).read()
file = open("american-english.txt","w")
file.write(keimeno)
file.close()
 
lines = open("/usr/share/dict/american-english").read().splitlines()
for line in lines:
    bf.add(line)
 

z=raw_input("To Arxeio sas:")
arxeio = open(z+".txt", 'r')
lista = []
dedomena = []
eswteriko = arxeio.readlines()

for i in range(len(eswteriko)):
	lista.extend(eswteriko[i].split[i])
for j in range(len(lista)):
	lista[i] = bf.lookup(lista[i])

print "".join(lista)