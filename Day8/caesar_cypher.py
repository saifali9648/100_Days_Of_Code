logo='''
           88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88                               
'''
print(logo)

alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# encrpted_list=[]
# def encrypt(orignal_text,shift_amount):
#     cypher_letter=""
#     for i in orignal_text:
#         index_number=alphabets.index(i)
#         shifted_index=index_number+shift_amount
#         shifted_index%=len(alphabets)
#         cypher_letter+=alphabets[shifted_index]
#     print(f"encrypted message is {cypher_letter}")
#     return cypher_letter
    #     encrpted_list.append(alphabets[shifted_index])
    #     # print(f"orignal index {index_number}")
    #     # print(f"shifted index {shifted_index}")
    # print(encrpted_list)
    # for j in encrpted_list:
    #     print(j)

def caesar(original_text,shift_amount,encode_decode):
    output_text=""
    if encode_decode=="decode":
                shift_amount*=-1
    for i in original_text:
        if i  not in alphabets:
            output_text+=i
        else:
            
            index_number=alphabets.index(i)
            shifted_letter=index_number+shift_amount
            shifted_letter%=len(alphabets)
            output_text+=alphabets[shifted_letter]
    print(f"Here is your {encode_decode}d message {output_text}")
should_continiue=True   
while should_continiue:
    direction=input("Type 'encode to encrypt', type decode to decrypt:\n").lower()
    text=input("Type your message:\n").lower()
    shift=int(input("Type the shift number:\n"))

    caesar(original_text=text,shift_amount=shift,encode_decode=direction)
    # print(f"this is printing after the function {encoded_text}")
    restart=input("if you want to continiue than type 'yes' other wise type 'no'").lower()
if restart=='no':
    should_continiue=False
    print("Good bye")


