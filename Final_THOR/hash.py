import streamlit as st
import hashlib
import sys
from streamlit import cli as stcli
# import streamlit
def run():
    st.title("Hash Conversion")

    x=st.text_input("Enter hash")
    a=hashlib.algorithms_guaranteed
    # print(a)
    i=[j for j in a]
    option = st.selectbox('Hashing Algorithms',(i))
    if option == 'sha256':
        hash_object = hashlib.sha256(x.encode())
        hex_dig = hash_object.hexdigest()
        st.write(hex_dig)
    elif option == 'sha512':
        hash_object = hashlib.sha512(x.encode())
        hex_dig = hash_object.hexdigest()
        st.write(hex_dig)
    elif option == 'sm3':
        hash_object = hashlib.sm3(x.encode())
        hex_dig = hash_object.hexdigest()
        st.write(hex_dig)
    elif option == 'whirlpool':
        hash_object = hashlib.whirlpool(x.encode())
        hex_dig = hash_object.hexdigest()
        st.write(hex_dig)
    elif option == 'blake2s':
        hash_object = hashlib.blake2s(x.encode())
        hex_dig = hash_object.hexdigest()
        st.write(hex_dig)
    elif option == 'sha3_512':
        hash_object = hashlib.sha3_512(x.encode())
        hex_dig = hash_object.hexdigest()
        st.write(hex_dig)
    elif option == 'sha384':
        hash_object = hashlib.sha384(x.encode())
        hex_dig = hash_object.hexdigest()
        st.write(hex_dig)
    elif option == 'md5':
        hash_object = hashlib.md5(x.encode())
        hex_dig = hash_object.hexdigest()
        st.write(hex_dig)
    elif option == 'ripemd160':
        hash_object = hashlib.ripemd160(x.encode())
        hex_dig = hash_object.hexdigest()
        st.write(hex_dig)
    elif option == 'sha3_384':
        hash_object = hashlib.sha3_384(x.encode())
        hex_dig = hash_object.hexdigest()
        st.write(hex_dig)
    elif option == 'sha512_256':
        hash_object = hashlib.sha512_256(x.encode())
        hex_dig = hash_object.hexdigest()
        st.write(hex_dig)
    elif option == 'sha512':
        hash_object = hashlib.sha256(x.encode())
        hex_dig = hash_object.hexdigest()
        st.write(hex_dig)
    elif option == 'md5-sha1':
        hash_object = hashlib.md5-sha1(x.encode())
        hex_dig = hash_object.hexdigest()
        st.write(hex_dig)
    elif option == 'blake2b':
        hash_object = hashlib.blake2b(x.encode())
        hex_dig = hash_object.hexdigest()
        st.write(hex_dig)
    elif option == 'sha3_256':
        hash_object = hashlib.sha3_256(x.encode())
        hex_dig = hash_object.hexdigest()
        st.write(hex_dig)
    elif option == 'shake_256':
        hash_object = hashlib.shake_256(x.encode())
        hex_dig = hash_object.hexdigest()
        st.write(hex_dig)
    elif option == 'sha3_224':
        hash_object = hashlib.sha3_224(x.encode())
        hex_dig = hash_object.hexdigest()
        st.write(hex_dig)
    elif option == 'sha512_224':
        hash_object = hashlib.sha512_224(x.encode())
        hex_dig = hash_object.hexdigest()
        st.write(hex_dig)
    elif option == 'sha224':
        hash_object = hashlib.sha224(x.encode())
        hex_dig = hash_object.hexdigest()
        st.write(hex_dig)
    elif option == 'md4':
        hash_object = hashlib.md4(x.encode())
        hex_dig = hash_object.hexdigest()
        st.write(hex_dig)
    elif option == 'sha1':
        hash_object = hashlib.sha1(x.encode())
        hex_dig = hash_object.hexdigest()
        st.write(hex_dig)

if __name__ == '__main__':
    if st._is_running_with_streamlit:
        run()
    else:
        sys.argv = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())