import unittest
import json
from app import app

class ApiAdnTest(unittest.TestCase):
    
    def testDnaNull(self):
        tester = app.test_client(self)
        response = tester.post("/mutant", json=dict(dna=None))
        statuscode = response.status_code
        self.assertEqual(statuscode,204)
        
    def testDnaEmpity(self):
        tester = app.test_client(self)
        response = tester.post("/mutant", json=dict(dna=[]))
        statuscode = response.status_code
        self.assertEqual(statuscode,204)
    
    def testMutanteFalse(self):
        tester = app.test_client(self)
        response = tester.post("/mutant", json=dict(dna=['ATGCGA','CAGTGC','TTATTT','AGACGG','GCGTCA','TCACTG']))
        statuscode = response.status_code
        self.assertEqual(statuscode,403)
        
    def testMutanteTrue(self):
        tester = app.test_client(self)
        response = tester.post("/mutant", json=dict(dna=["ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"]))
        statuscode = response.status_code
        self.assertEqual(statuscode,200)
        
    def testMutanteTrueHorizontal(self):
        tester = app.test_client(self)
        response = tester.post("/mutant", json=dict(dna=["TTTTTT","CAGTGC","TTATGT","AGATGG","CGCGTA","TCACTG"]))
        statuscode = response.status_code
        self.assertEqual(statuscode,200)  
        
    def testMutanteTrueVertical(self):
        tester = app.test_client(self)
        response = tester.post("/mutant", json=dict(dna=["ATCGATCGAT","ACTGCTGCTG","ATCGATCGAT","ATCGATCGAT","ATCGATCGAT","ATCGATCGAT","ATCGATCGAT","ATCGATCGAT","ATCGATCGAT","ATCGATCGAT"]))
        statuscode = response.status_code
        self.assertEqual(statuscode,200)
        
    def testMutanteTrueDiagLR(self):
        tester = app.test_client(self)
        response = tester.post("/mutant", json=dict(dna=["ACTGAC","GATTTT","CTATAC","GAGAXA","GCTCAC","TCGATA"]))
        statuscode = response.status_code
        self.assertEqual(statuscode,200)
    
    def testMutanteTrueDiagRL(self):
        tester = app.test_client(self)
        response = tester.post("/mutant", json=dict(dna=["ACTG","GTGG","CGAC","GGGG"]))
        statuscode = response.status_code
        self.assertEqual(statuscode,200)
    
    def testDnaMin(self):
        tester = app.test_client(self)
        response = tester.post("/mutant", json=dict(dna=["ACT","TGG","GAC","GGG"]))
        statuscode = response.status_code
        self.assertEqual(statuscode,403)
    
    def testCharacterBad(self):
        tester = app.test_client(self)
        response = tester.post("/mutant", json=dict(dna=["XXXA","TBGA","GACN","UGGG"]))
        statuscode = response.status_code
        self.assertEqual(statuscode,403)
        
    def testMatrizNoMatch(self):
        tester = app.test_client(self)
        response = tester.post("/mutant", json=dict(dna=["AC","GTG","CGAC","GTGGG"]))
        statuscode = response.status_code
        self.assertEqual(statuscode,403)
    
    def testStats(self):
        tester = app.test_client(self)
        response = tester.get("/stats")
        statuscode = response.status_code
        self.assertEqual(statuscode,200)
        
if __name__ == "__main__":
    unittest.main()