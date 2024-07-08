#Test program for the encryption tool
import encrypt

def main():
    #creating the test cases
    tests = []

    tests.append(encrypt.caesar_cypher("The Amazon rainforest, known as the Earth's lungs, produces about 20% of the world's oxygen.", 5))
    tests.append(encrypt.caesar_cypher("During the school science fair, Maria's experiment on plant growth won first prize for its creativity.", 3))
    tests.append(encrypt.caesar_cypher("Space exploration has led to many discoveries, including evidence of water on Mars.", 3))
    tests.append(encrypt.caesar_cypher("Although dolphins are often seen playing in the ocean, they are actually very intelligent mammals.", 4))
    
    tests.append(encrypt.caesar_cypher("The pyramids of Egypt were constructed thousands of years ago, showcasing ancient engineering skills.", 6))
    tests.append(encrypt.caesar_cypher("Tornadoes are powerful storms that can cause significant damage, and they are most common in the central United States.", 3))
    tests.append(encrypt.caesar_cypher("The internet has revolutionized how people communicate, providing instant access to information worldwide.", 7))
    tests.append(encrypt.caesar_cypher("Renewable energy, such as wind and solar power, is essential for reducing our dependence on fossil fuels.", 4))

    #creating the expected results
    tests_results = []

    tests_results.append("Ymj Frfets wfnsktwjxy, pstbs fx ymj Jfwym'x qzslx, uwtizhjx fgtzy 20% tk ymj btwqi'x tcdljs.")
    tests_results.append("Gxulqj wkh vfkrro vflhqfh idlu, Pduld'v hashulphqw rq sodqw jurzwk zrq iluvw sulch iru lwv fuhdwlylwb.")
    tests_results.append("Vsdfh hasorudwlrq kdv ohg wr pdqb glvfryhulhv, lqfoxglqj hylghqfh ri zdwhu rq Pduv.")
    tests_results.append("Epxlsykl hsptlmrw evi sjxir wiir tpecmrk mr xli sgier, xlic evi egxyeppc zivc mrxippmkirx qeqqepw.")
   
    tests_results.append("Znk vexgsojy ul Kmevz ckxk iutyzxaizkj znuaygtjy ul ekgxy gmu, ynucigyotm gtioktz ktmotkkxotm yqorry.")
    tests_results.append("Wruqdgrhv duh srzhuixo vwrupv wkdw fdq fdxvh vljqlilfdqw gdpdjh, dqg wkhb duh prvw frpprq lq wkh fhqwudo Xqlwhg Vwdwhv.")
    tests_results.append("Aol pualyula ohz ylcvsbapvupglk ovd wlvwsl jvttbupjhal, wyvcpkpun puzahua hjjlzz av pumvythapvu dvyskdpkl.")
    tests_results.append("Viriaefpi irivkc, wygl ew amrh erh wspev tsaiv, mw iwwirxmep jsv vihygmrk syv hitirhirgi sr jswwmp jyipw.")


    #printing the test cases and comparing to the expected result
    for i in range(8):
        #if the test result and the test output don't line up -- say the test was failed
        #if not -- say the test was sucessful
        if(tests[i] != (tests_results[i])):
            print("Test Failed :(, please check your code again")
        #print the test output
        else:
            print("Test Passed!")

        #print test expected output
        print("Your result: " + tests[i])
        print("Expected result: " + tests_results[i]+ "\n")

main()
