alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
encrpted_list=[]
def encrypt(orignal_text,shift_amount):
    cypher_letter=""
    for i in orignal_text:
        index_number=alphabets.index(i)
        shifted_index=index_number+shift_amount
        shifted_index%=len(alphabets)
        print(f" shifted {shifted_index}")
        cypher_letter+=alphabets[shifted_index]
    print(f"encrypted message is {cypher_letter}")
    #     encrpted_list.append(alphabets[shifted_index])
    #     # print(f"orignal index {index_number}")
    #     # print(f"shifted index {shifted_index}")
    # print(encrpted_list)
    # for j in encrpted_list:
    #     print(j)
direction=input("Type 'encode to encrypt', type decode to decrypt:\n").lower()
text=input("Type your message:\n").lower()
shift=int(input("Type the shift number:\n"))

encrypt(text,shift)


